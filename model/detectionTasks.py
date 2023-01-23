from model.task import Task
import numpy as np

TRAINED_MODELS_PATH: str = "trained_models/"


class detectionTasks(Task):
    def __init__(self, tweet_dataset_file_path, embedding_method, batch_size, epochs, cnnFlag, filters, input1, input2,
                 input3, num_units):
        super().__init__(embedding_method, batch_size, epochs, cnnFlag, filters, input1, input2, input3, num_units)
        self.error = False
        text_col_name = 'text'
        label_col_name = 'label'
        fakes_label_val = '0'
        real_label_val = '1'
        try:
            news, labels = self.read_csv_file_into_array(tweet_dataset_file_path, text_col_name, label_col_name)
            texts, clean_labels = self.get_preprocessed_texts_for_one_file(news, labels, real_label_val,
                                                                           fakes_label_val)
        except:
            self.error = True
            return

        y_expected = self.get_classification_in_appropriate_format(clean_labels)  # split data to test, train and validation
        self.prepare_train_validation_test_sets(texts, y_expected)
        self.get_categorical_probabilities(self.y_test, self.y_train,self.y_valid)  # set probabilities for each text to belong for each label
        self.model_path = TRAINED_MODELS_PATH

    # Returns one array with tweets and one with labels
    @staticmethod
    def read_csv_file_into_array(file_name, text_column_name, label_column_name):
        import pandas as pd
        col_list = [text_column_name, label_column_name]
        df = pd.read_csv(file_name, usecols=col_list)
        texts_arr = df[text_column_name].values.tolist()
        labels_arr = df[label_column_name].values.tolist()
        return texts_arr, labels_arr

    # Returns one array with preprocessed texts and one with the corresponding labels
    def get_preprocessed_texts_for_one_file(self, texts, labels, real_label_val, fakes_label_val):
        clean_labels = []
        clean_texts = []
        j = 0
        label_is_integer = self.is_numeric(fakes_label_val) and self.is_numeric(real_label_val)
        for i, tweet in enumerate(texts):
            if isinstance(tweet, str):
                if label_is_integer:
                    if self.is_numeric(str(labels[i])) and self.is_one_of_labels(int(labels[i]), int(real_label_val),
                                                                                 int(fakes_label_val)):
                        j = self.update(clean_labels, clean_texts, j, labels[i], tweet)
                elif self.is_one_of_labels(labels[i], real_label_val, fakes_label_val):
                    j = self.update(clean_labels, clean_texts, j, labels[i], tweet)
        return clean_texts, clean_labels

    def update(self, clean_labels, clean_texts, j, label, tweet):
        tweet_blocks = self.get_preprocessed_text("" + tweet)
        clean_texts.extend(block for block in tweet_blocks)
        clean_labels.extend([label for x in range(j, j + len(tweet_blocks))])
        j = j + len(tweet_blocks)
        return j

    # returns array in appropriate format
    @staticmethod
    def get_classification_in_appropriate_format(clean_labels):
        y_expected = np.empty(len(clean_labels), int)
        y_expected[0:len(clean_labels)] = clean_labels[0:len(clean_labels)]
        return y_expected

    # Checks if the input is a number
    @staticmethod
    def is_numeric(num_str):
        return num_str.isnumeric() or num_str.replace('.', '').isdigit()
    # Checks the labels
    @staticmethod
    def is_one_of_labels(label, real_label_val, fakes_label_val):
        return label == fakes_label_val or label == real_label_val
