import threading
import os
import threading
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.utils import np_utils

TRAINED_MODELS_PATH: str = "trained_models/"
PLOTS_PATH = "results/plots/"


class Task:
    def __init__(self, embedding_method, batch_size, epochs, cnnFlag, filters, input1, input2, input3, num_units):
        self.t = None
        self.running = None
        self.num_classes = None
        self.filters = filters
        self.num_units = num_units
        self.embedding_method = embedding_method
        self.input1 = input1
        self.input2 = input2
        self.input3 = input3
        self.y_test_prob = None
        self.y_valid_prob = None
        self.y_valid = None
        self.y_test = None
        self.x_valid = None
        self.x_test = None
        self.y_train = None
        self.y_train_prob = None
        self.x_train = None
        from model.detectionModel import DetectionModel
        self.batch_size, self.epochs, self.cnnFlag = batch_size, epochs, cnnFlag
        self.model = DetectionModel()
        self.max_text_len = self.model.config['max_seq_len']
        self.acc_path = PLOTS_PATH + "ModelAcc.png"
        self.loss_path = PLOTS_PATH + "ModelLoss.png"
        self.model_path = TRAINED_MODELS_PATH + "Undefined/"

    # Returns an array with preprocessed texts
    def get_preprocessed_texts(self, texts):
        preprocessed_texts = []
        for text in texts:
            text_blocks = self.get_preprocessed_text(text)
            preprocessed_texts.extend(block for block in text_blocks)
        return preprocessed_texts

    # Returns preprocessed text
    def get_preprocessed_text(self, text):
        from model.preprocessing import clean_text
        preprocessed_text = clean_text(text)
        from model.preprocessing import separate_text_to_blocks
        text_blocks = separate_text_to_blocks(preprocessed_text, self.max_text_len)
        return text_blocks

    # Split data to train, validation and test
    def prepare_train_validation_test_sets(self, texts, y_expected):
        self.x_train, x, self.y_train, y = train_test_split(texts, y_expected, train_size=0.7)
        self.x_test, self.x_valid, self.y_test, self.y_valid = train_test_split(x, y, train_size=0.5)

    # Sets probabilities for each text
    def get_categorical_probabilities(self, y_test, y_train, y_valid):
        self.y_train_prob = np_utils.to_categorical(y_train)
        self.y_valid_prob = np_utils.to_categorical(y_valid)
        self.y_test_prob = np_utils.to_categorical(y_test)
        self.num_classes = self.y_train_prob.shape[1]

    # Calling train model method
    def run_train_model(self):
        self.model.build_model(self.num_classes, self.embedding_method, self.cnnFlag, self.filters, self.input1, self.input2, self.input3, self.num_units)
        self.model.fit_model(x_train=tf.constant(self.x_train), y_train_prob=self.y_train_prob,
                             x_valid=tf.constant(self.x_valid), y_valid_prob=self.y_valid_prob,
                             batch_size=self.batch_size, epochs=self.epochs)
        self.running = False

    def start_train_model(self):
        self.running = True     # Thread will be running until running = False
        self.t = threading.Thread(target=self.run_train_model)
        self.t.start()

    def save_model(self, model_name, replace=False):
        path = "../" + self.model_path + model_name + self.model.model_suffix
        if os.path.exists(path) and not replace:
            return False
        else:
            self.model.save_model(path)
            return True

    def test_model(self):
        self.model.test_model(x_test=tf.constant(self.x_test), y_test_prob=self.y_test_prob, y_test=self.y_test)

    def create_accuracy_graph(self):
        plt.figure(facecolor='#F0FFF0')
        plt.plot(self.model.history.history['accuracy'])
        plt.plot(self.model.history.history['val_accuracy'])
        plt.title('Model accuracy in epoch')
        plt.ylabel('Accuracy')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Validation'], loc='upper left')
        plt.savefig("../" + self.acc_path)

    def create_loss_graph(self):
        plt.figure(facecolor='#F0FFF0')
        plt.plot(self.model.history.history['loss'])
        plt.plot(self.model.history.history['val_loss'])
        plt.title('Model loss in epoch')
        plt.ylabel('Loss')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Validation'], loc='upper left')
        plt.savefig("../" + self.loss_path)
