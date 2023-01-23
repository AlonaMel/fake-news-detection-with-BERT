import numpy as np
import tensorflow as tf
from model.detectionModel import DetectionModel

TRAINED_MODELS_PATH: str = "trained_models/"
PLOTS_PATH = "results/plots/"


class Detection:
    def __init__(self, input, model_name):
        self.model = DetectionModel()
        self.model.load_model(TRAINED_MODELS_PATH + model_name)  # Loads chosen model
        input_texts = self.get_preprocessed_text(input, max_text_len=self.model.config['max_seq_len'])  # Separate input into chunks in size 128 tokens
        self.number_of_chunks = len(input_texts)
        self.probabilities, self.predictions = self.get_prediction(input_texts)
        self.real_percent, self.fake_percent = self.get_distribution()

    @staticmethod
    def get_preprocessed_text(input, max_text_len):
        input_texts = []
        from model.preprocessing import clean_text
        preprocessed_input = clean_text(input)
        from model.preprocessing import separate_text_to_blocks
        input_blocks = separate_text_to_blocks(preprocessed_input, max_text_len)
        input_texts.extend((block for block in input_blocks))
        return input_texts

    # Get prediction for input chunks
    def get_prediction(self, input):
        predicted_probs = self.model.predict(tf.constant(input))
        predictions_array = np.argmax(predicted_probs, -1)
        return predicted_probs, predictions_array

    # Get distributions in percentage
    def get_distribution(self):
        all1 = np.size(self.predictions)
        if all1 == 1:
            fake_percent = 100.0 * self.probabilities[0][0]
            real_percent = 100.0 * self.probabilities[0][1]
        else:
            fake_percent = 100.0 * sum(self.probabilities[:, 0]) / all1
            real_percent = 100.0 * sum(self.probabilities[:, 1]) / all1

        return real_percent, fake_percent
