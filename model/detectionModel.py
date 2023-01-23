import os
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import tensorflow_text as text
from keras.layers import LSTM
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns

config_tokens = {
    'max_seq_len': 128,
    'seq_len_block4': 74,
    'seq_len_block5': 14
}


class DetectionModel:
    def __init__(self):
        self.count_false_predicted = None
        self.count_well_predicted = None
        self.test_accuracy = None
        self.valid_accuracy = None
        self.train_accuracy = None
        self.model = None
        self.history = None
        self.config = config_tokens
        self.model_suffix = ".h5"

    def build_model(self, num_classes, embedding_method, cnnFlag, filters, input1, input2, input3, num_units):
        # Set parameters chosen by user
        if embedding_method == 'Pre-trained small BERT':
            encoder_name = 'BERT/encoder'
            preprocessor_name = 'BERT/preprocessor'
            dimension_size = 768
            sub_dimension_size = 128
        else:
            encoder_name = 'BERT/largeEncoder'
            preprocessor_name = 'BERT/largePreprocessor'
            dimension_size = 1024
            sub_dimension_size = 256
        x1 = self.config['max_seq_len'] - input1 + 1
        x3 = self.config['max_seq_len'] - input3 + 1
        x2 = self.config['max_seq_len'] - input2 + 1
        print(x1, x2, x3)
        y1 = (x1 - input1) / 5 + 1
        y2 = (x2 - input2) / 5 + 1
        y3 = (x3 - input3) / 5 + 1
        con_y = y1 + y2 + y3
        self.config['seq_len_block4'] = con_y - input3 + 1
        self.config['seq_len_block5'] = (self.config['seq_len_block4'] - input3) / 5 + 1

        # Load pre-trained BERT model
        input_layer = tf.keras.layers.Input(shape=(), dtype=tf.string, name='text')  # input layer
        os.chdir("../")
        preprocessor = hub.KerasLayer(preprocessor_name, name='preprocessing')  # load preprocessing
        encoder_inputs = preprocessor(input_layer)
        encoder = hub.KerasLayer(encoder_name, trainable=True, name='BE_encoder')
        outputs = encoder(encoder_inputs)
        embeddings = outputs["sequence_output"]  # [batch_size, seq_length, 768]
        os.chdir("./controllers")

        # In case CNN model was chosen
        if cnnFlag:
            conv1D_list = []
            kernel_sizes = [input1, input2, input3]

            # Loop for first 3 CNN layers
            for k in kernel_sizes:
                cnn = tf.keras.layers.Conv1D(filters, kernel_size=k, activation='relu',
                                             input_shape=(self.config['max_seq_len'], dimension_size))(embeddings)
                cnn = tf.keras.layers.MaxPooling1D(pool_size=5, strides=5)(cnn)
                conv1D_list.append(cnn)

            concatenated_layer = tf.keras.layers.concatenate(conv1D_list, axis=1)
            cnn_4 = tf.keras.layers.Conv1D(filters, kernel_size=5, activation='relu',
                                           input_shape=(self.config['seq_len_block4'], sub_dimension_size))(concatenated_layer)
            cnn_4 = tf.keras.layers.MaxPooling1D(pool_size=5, strides=5)(cnn_4)

            final_layer = tf.keras.layers.Conv1D(filters, kernel_size=5, activation='relu',
                                                 input_shape=(self.config['seq_len_block5'], sub_dimension_size))(cnn_4)
            final_layer = tf.keras.layers.MaxPooling1D(pool_size=5, strides=5)(final_layer)

        # In case LSTM model was chosen
        else:
            lstm_1 = LSTM(num_units, return_sequences=True, input_shape=(self.config['max_seq_len'], dimension_size),
                          dropout=0.2)(embeddings)
            lstm_2 = LSTM(num_units, return_sequences=True)(lstm_1)
            final_layer = LSTM(num_units, return_sequences=True)(lstm_2)

        flatten_layer = tf.keras.layers.Flatten()(final_layer)
        dropped = tf.keras.layers.Dropout(0.2)(flatten_layer)
        dense_layer = tf.keras.layers.Dense(sub_dimension_size, activation='relu')(dropped)
        dropped = tf.keras.layers.Dropout(0.2)(dense_layer)
        output_layer = tf.keras.layers.Dense(num_classes, activation='softmax')(dropped)

        self.model = tf.keras.models.Model(input_layer, output_layer)
        self.model.summary()
        self.model.compile(loss='categorical_crossentropy', metrics=['accuracy'],
                           optimizer=tf.keras.optimizers.Adadelta(0.001))

    # To train the model
    def fit_model(self, x_train, y_train_prob, x_valid, y_valid_prob, batch_size, epochs):
        self.history = self.model.fit(x=x_train, y=y_train_prob, validation_data=(x_valid, y_valid_prob),
                                      batch_size=batch_size, epochs=epochs)
        _, self.train_accuracy = self.model.evaluate(x_train, y_train_prob, verbose=0)
        _, self.valid_accuracy = self.model.evaluate(x_valid, y_valid_prob, verbose=0)

    # Test the trained model on new unseen data and calculates the accuracy
    def test_model(self, x_test, y_test_prob, y_test):
        _, self.test_accuracy = self.model.evaluate(x_test, y_test_prob, verbose=0)

        Y_predicted_prob = self.model.predict(tf.constant(x_test))
        Y_predicted = np.argmax(Y_predicted_prob, -1)

        self.count_well_predicted = np.count_nonzero([y_test == Y_predicted])
        self.count_false_predicted = Y_predicted.shape[0] - self.count_well_predicted

        # Convert predictions to binary labels
        Y_predicted = np.round(Y_predicted)
        matrix = confusion_matrix(y_test, Y_predicted)
        print(classification_report(y_test, Y_predicted))

        # Confusion matrix plot
        sns.heatmap(matrix, annot=True, fmt='d', cmap='Greens')
        plt.xlabel('Predicted Labels')
        plt.ylabel('True Labels')
        plt.title('Confusion Matrix')
        plt.show()

    def save_model(self, model_path):
        self.model.save(model_path)

    def load_model(self, model_path):
        self.model = tf.keras.models.load_model(model_path, custom_objects={'KerasLayer': hub.KerasLayer})

    # To generate the predicted labels for the test data
    def predict(self, input):
        return self.model.predict(x=input)
