import os
import sys
import tkinter as tk
from tkinter import filedialog
from PyQt5 import QtWidgets
from controllers.checker import Checker, set_normal_style
from pathlib import Path

TRAINED_MODELS_PATH = "trained_models/"


class Main(Checker):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.lstmSet_flag = None
        self.cnnFlag = None
        self.num_units = 64
        self.filters = 128
        self.cnnSet_flag = 0
        self.filter_1 = 3
        self.filter_2 = 4
        self.filter_3 = 5
        self.task = None
        self.detectionFlag = None
        self.allOk = None
        self.window = None
        from gui.mainDesign import Ui_MainDesign
        self.ui = Ui_MainDesign()
        self.ui.setupUi(self)
        self.set_buttons_handlers()
        self.ui.radioBtn_main.setChecked(True)
        self.ui.cnnParam_BOX.setHidden(True)
        self.ui.lstmParam_BOX.setHidden(True)
        self.main_form()
        self.fillBERT_comboBox()
        self.fill_comboBox()
        self.clear_feedback()

    def set_buttons_handlers(self):
        self.ui.radioBtn_main.clicked.connect(self.main_form)
        self.ui.radioBtn_train.clicked.connect(self.training_form)
        self.ui.radioBtn_detection.clicked.connect(self.detection_form)
        self.ui.radioBtn_CNN.clicked.connect(self.cnn_form)
        self.ui.radioBtn_LSTM.clicked.connect(self.lstm_form)
        self.ui.train_btn.clicked.connect(self.train_pressed)
        self.ui.start_btn.clicked.connect(self.start_pressed)
        self.ui.uploadCsv_btn.clicked.connect(lambda: self.upload_file_pressed(widget=self.ui.csv_pathLine))
        self.ui.radioBtn_defaultCNN.clicked.connect(
            lambda: self.cnn_default(widget=self.ui.filters_input, widget1=self.ui.filter1, widget2=self.ui.filter2,
                                     widget3=self.ui.filter3))
        self.ui.radioBtn_defaultLSTM.clicked.connect(lambda: self.lstm_default(widget=self.ui.numUnits_input))
        self.ui.radioBtn_setParamsCNN.clicked.connect(self.cnn_setParams)
        self.ui.radioBtn_setParamsLSTM.clicked.connect(self.lstm_setParams)

    # Call when train button pressed
    def train_pressed(self):
        self.clear_feedback()
        self.detectionFlag = False
        epochs_widget = self.ui.epoch_input
        epochs = str(epochs_widget.text())
        batch_size_widget = self.ui.batchSize_input
        batch_size = str(batch_size_widget.text())
        file_path_widget = self.ui.csv_pathLine
        file_path = str(file_path_widget.text())
        embedding_method = self.ui.BERT_comboBox.currentText()  # Chosen pre-trained BERT model
        file_name = Path(file_path + ".csv")

        # Checks all user inputs

        if file_name.exists():
            self.invalid_input("• File is not in .csv format", file_path_widget)
        else:
            set_normal_style(file_path_widget)
        if not self.ui.radioBtn_CNN.isChecked() and not self.ui.radioBtn_LSTM.isChecked():
            self.model_not_selected("• select cnn or lstm")
        if batch_size == "":
            self.invalid_input("• Batch size field is empty", batch_size_widget)
        elif not batch_size.isnumeric() or int(batch_size) <= 0:
            self.invalid_input("• Invalid batch size entered", batch_size_widget)
        else:
            set_normal_style(batch_size_widget)
        if epochs == "":
            self.invalid_input("• Epochs field is empty", epochs_widget)
        elif not epochs.isnumeric() or int(epochs) <= 0:
            self.invalid_input("• Invalid epochs entered", epochs_widget)
        else:
            set_normal_style(epochs_widget)
        if str(file_path) == "":
            self.invalid_input("• File path is empty", file_path_widget)
        else:
            set_normal_style(file_path_widget)
            # CNN radio button pressed
        if self.cnnSet_flag == 1:
            filters_widget = self.ui.filters_input
            self.filters = str(filters_widget.text())
            filter1_widget = self.ui.filter1
            self.filter_1 = str(filter1_widget.text())
            filter2_widget = self.ui.filter2
            self.filter_2 = str(filter2_widget.text())
            filter3_widget = self.ui.filter3
            self.filter_3 = str(filter3_widget.text())
            if self.filters == "":
                self.invalid_input("• Number of CNN layers field is empty", filters_widget)
            elif not self.filters.isnumeric() or int(self.filters) <= 0:
                self.invalid_input("• Invalid Number of CNN layers entered", filters_widget)
            else:
                set_normal_style(filters_widget)
            if self.filter_1 == "":
                self.invalid_input("• first filter field is empty", filter1_widget)
            elif not self.filter_1.isnumeric() or int(self.filter_1) <= 0:
                self.invalid_input("• Invalid filter number entered", filter1_widget)
            else:
                set_normal_style(filter1_widget)
            if self.filter_2 == "":
                self.invalid_input("• second filter field is empty", filter2_widget)
            elif not self.filter_2.isnumeric() or int(self.filter_2) <= 0:
                self.invalid_input("• Invalid filter number entered", filter2_widget)
            else:
                set_normal_style(filter2_widget)
            if self.filter_3 == "":
                self.invalid_input("• third filter field is empty", filter3_widget)
            elif not self.filter_3.isnumeric() or int(self.filter_3) <= 0:
                self.invalid_input("• Invalid filter number entered", filter3_widget)
            else:
                set_normal_style(filter3_widget)
        # LSTM radio button pressed
        if self.lstmSet_flag == 1:
            numUnits_widget = self.ui.numUnits_input
            self.num_units = str(numUnits_widget.text())
            if self.num_units == "":
                self.invalid_input("• Hidden units field is empty", numUnits_widget)
            elif not self.num_units.isnumeric() or int(self.num_units) <= 0:
                self.invalid_input("• Invalid Number of hidden units entered", numUnits_widget)
            else:
                set_normal_style(numUnits_widget)
        # In case all inputs are in the right format, allows to start training process
        if self.allOk:
            from model.detectionTasks import detectionTasks
            self.task = detectionTasks(file_path, embedding_method, int(batch_size), int(epochs), bool(self.cnnFlag),
                                       int(self.filters), int(self.filter_1), int(self.filter_2), int(self.filter_3),
                                       int(self.num_units))
            if not self.task.error:
                self.close()
                from controllers.loadingWindow import LoadingWindow
                self.window = LoadingWindow(content="", model_name="", detectionFlag=self.detectionFlag, task=self.task)
                self.window.show()
            else:
                self.invalid_input("• File is not in CSV format", file_path_widget)

    @staticmethod
    def upload_file_pressed(widget):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        widget.setText(file_path)

    # Updates widgets for the maim page when chosen
    def main_form(self):
        self.clear_feedback()
        self.detectionFlag = False
        self.ui.main_BOX.setHidden(False)
        self.ui.train_BOX.setHidden(True)
        self.ui.detection_Box.setHidden(True)
        self.ui.radioBtn_detection.setChecked(False)
        self.ui.radioBtn_train.setChecked(False)
        self.ui.radioBtn_CNN.setChecked(False)
        self.ui.radioBtn_LSTM.setChecked(False)
        self.ui.radioBtn_main.setChecked(True)
        self.ui.radioBtn_setParamsCNN.setChecked(False)

    # Updates widgets for the train new model page when chosen
    def training_form(self):
        self.clear_feedback()
        self.detectionFlag = False
        self.ui.main_BOX.setHidden(True)
        self.ui.train_BOX.setHidden(False)
        self.ui.detection_Box.setHidden(True)
        self.ui.lstmParam_BOX.setHidden(True)
        self.ui.cnnParam_BOX.setHidden(True)
        self.ui.radioBtn_detection.setChecked(False)
        self.ui.radioBtn_train.setChecked(True)
        self.ui.radioBtn_CNN.setChecked(False)
        self.ui.radioBtn_LSTM.setChecked(False)
        self.ui.radioBtn_main.setChecked(False)
        self.ui.radioBtn_setParamsCNN.setChecked(False)

    def cnn_form(self):
        self.clear_feedback()
        self.cnnFlag = True
        self.lstmSet_flag = 0

        self.ui.main_BOX.setHidden(True)
        self.ui.train_BOX.setHidden(False)
        self.ui.detection_Box.setHidden(True)
        self.ui.lstmParam_BOX.setHidden(True)
        self.ui.cnnParam_BOX.setHidden(False)

        self.ui.radioBtn_main.setChecked(False)
        self.ui.radioBtn_train.setChecked(True)
        self.ui.radioBtn_detection.setChecked(False)

        self.ui.radioBtn_CNN.setChecked(True)
        self.ui.radioBtn_LSTM.setChecked(False)

        self.ui.radioBtn_defaultCNN.setChecked(True)
        self.ui.radioBtn_setParamsCNN.setChecked(False)
        self.ui.radioBtn_setParamsLSTM.setChecked(False)

        self.ui.filters_input.setText('128')
        self.ui.filters_input.setReadOnly(True)

        self.ui.filter1.setReadOnly(True)
        self.ui.filter1.setText('3')
        self.ui.filter2.setReadOnly(True)
        self.ui.filter2.setText('4')
        self.ui.filter3.setReadOnly(True)
        self.ui.filter3.setText('5')

    def cnn_setParams(self):
        self.clear_feedback()
        self.cnnSet_flag = 1
        self.ui.radioBtn_setParamsCNN.setChecked(True)

        self.ui.filters_input.setText('')
        self.ui.filters_input.setReadOnly(False)

        self.ui.filter1.setReadOnly(False)
        self.ui.filter1.setText('')
        self.ui.filter2.setReadOnly(False)
        self.ui.filter2.setText('')
        self.ui.filter3.setReadOnly(False)
        self.ui.filter3.setText('')

    def lstm_form(self):
        self.clear_feedback()
        self.cnnFlag = False
        self.cnnSet_flag = 0

        self.ui.main_BOX.setHidden(True)
        self.ui.train_BOX.setHidden(False)
        self.ui.detection_Box.setHidden(True)
        self.ui.cnnParam_BOX.setHidden(True)
        self.ui.lstmParam_BOX.setHidden(False)

        self.ui.radioBtn_main.setChecked(False)
        self.ui.radioBtn_train.setChecked(True)
        self.ui.radioBtn_detection.setChecked(False)

        self.ui.radioBtn_CNN.setChecked(False)
        self.ui.radioBtn_LSTM.setChecked(True)

        self.ui.radioBtn_defaultLSTM.setChecked(True)
        self.ui.radioBtn_setParamsCNN.setChecked(False)
        self.ui.radioBtn_setParamsLSTM.setChecked(False)

        self.ui.numUnits_input.setReadOnly(True)
        self.ui.numUnits_input.setText('64')

    def lstm_setParams(self):
        self.clear_feedback()
        self.lstmSet_flag = 1
        self.ui.radioBtn_setParamsCNN.setChecked(False)

        self.ui.radioBtn_setParamsLSTM.setChecked(True)
        self.ui.numUnits_input.setText('')
        self.ui.numUnits_input.setReadOnly(False)

    # Updates widgets for the tweet classification page when chosen
    def detection_form(self):
        self.clear_feedback()
        self.detectionFlag = True

        self.ui.main_BOX.setHidden(True)
        self.ui.train_BOX.setHidden(True)
        self.ui.detection_Box.setHidden(False)
        self.ui.lstmParam_BOX.setHidden(True)
        self.ui.cnnParam_BOX.setHidden(True)

        self.ui.radioBtn_main.setChecked(False)
        self.ui.radioBtn_train.setChecked(False)
        self.ui.radioBtn_detection.setChecked(True)

        self.ui.radioBtn_CNN.setChecked(False)
        self.ui.radioBtn_LSTM.setChecked(False)
        self.ui.radioBtn_setParamsCNN.setChecked(False)

    @staticmethod
    def cnn_default(widget, widget1, widget2, widget3):
        widget.setText('128')
        widget.setReadOnly(True)
        widget1.setText('3')
        widget1.setReadOnly(True)
        widget2.setText('4')
        widget2.setReadOnly(True)
        widget3.setText('5')
        widget3.setReadOnly(True)

    @staticmethod
    def lstm_default(widget):
        widget.setText('128')
        widget.setReadOnly(True)

    # Insert models into a combobox
    def fill_comboBox(self):
        self.ui.comboBox.clear()
        arr = os.listdir('../trained_models')
        models = []
        for item in arr:
            if item.split(".")[1] == "h5":
                models.append(item.rstrip(".h5"))
        self.ui.comboBox.addItems(models)

    # Insert pre-trained BERT models into a combobox
    def fillBERT_comboBox(self):
        self.ui.BERT_comboBox.clear()
        methods = ['Pre-trained small BERT', 'Pre-trained large BERT']
        self.ui.BERT_comboBox.addItems(methods)

    # Called when start detection button pressed
    def start_pressed(self):
        self.detectionFlag = True
        self.clear_feedback()
        tweet_widget = self.ui.tweet_textEdit
        set_normal_style(tweet_widget)
        tweet_str = str(tweet_widget.toPlainText())
        model_name = self.ui.comboBox.currentText()

        if tweet_str == "":
            self.invalid_input("• No tweet has been entered", tweet_widget)
        # In case tweet entered, open loading window and begin the detection process
        else:
            set_normal_style(tweet_widget)
            self.close()
            from controllers.loadingWindow import LoadingWindow
            self.window = LoadingWindow(content=tweet_str, model_name=model_name, detectionFlag=self.detectionFlag,
                                        task="")
            self.window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())
