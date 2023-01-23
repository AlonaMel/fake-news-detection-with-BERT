import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMessageBox


class Ui_MainDesign(object):
    def __init__(self):
        self.title = None
        self.header_title1 = None
        self.header_title2 = None
        self.header_title3 = None
        self.backgroundImg = None
        self.lstmParam_BOX = None
        self.filter3 = None
        self.filter2 = None
        self.filter1 = None
        self.kernelSize_title = None
        self.filters_input = None
        self.radioBtn_setParamsCNN = None
        self.radioBtn_defaultCNN = None
        self.fakeFact_image = None
        self.BERTCombo_title = None
        self.BERT_comboBox = None
        self.radioBtn_setParamsLSTM = None
        self.radioBtn_defaultLSTM = None
        self.cnnParam_BOX = None
        self.horizontal_cnnLstm = None
        self.numUnits_input = None
        self.numOfFilters_title = None
        self.radioBtn_main = None
        self.main_BOX = None
        self.cnnLSTM_title = None
        self.radioBtn_LSTM = None
        self.radioBtn_CNN = None
        self.messageBox = None
        self.horizontalTweet = None
        self.horizontal_combobox = None
        self.start_btn = None
        self.tweet_textEdit = None
        self.comboBox = None
        self.selectModel_title = None
        self.horizontal_start = None
        self.detection_Box = None
        self.vertical_detection = None
        self.uploadCSV_title = None
        self.horizontal_epochBatch = None
        self.horizontal_upload = None
        self.horizontal_trainBtn = None
        self.verticalEpoBat = None
        self.stackLayout = None
        self.train_btn = None
        self.batchSize_input = None
        self.batchSize_title = None
        self.epoch_title = None
        self.epoch_input = None
        self.uploadCsv_btn = None
        self.emptyLine = None
        self.csv_pathLine = None
        self.vertical_train = None
        self.radioBtn_detection = None
        self.radioBtn_train = None
        self.leftSide_layout = None
        self.centerWidget = None
        self.main_frame = None
        self.groupBox = None
        self.train_BOX = None

    def setupUi(self, MainWindow):
        MainWindow.resize(858, 598)
        MainWindow.setFixedSize(858, 598)

        self.centerWidget = QtWidgets.QWidget(MainWindow)

        self.groupBox = QtWidgets.QGroupBox(self.centerWidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(30, 0, 800, 570))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setStyleSheet(
            "border-width: 1px;\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-style: solid;\n"
            "font: 8pt \"Sitka Small\";\n"
            "background-color: rgba(spread:pad, x1:0.996, y1:0.0340909, x2:1, y2:0, stop:1\n"
            "rgba(255, 204, 255, 1));\n")

        self.main_frame = QtWidgets.QFrame(self.groupBox)
        self.main_frame.setGeometry(QtCore.QRect(0, 0, 800, 570))
        self.main_frame.setStyleSheet(
            "border-width: 2px;\n"
            "background-color: qlineargradient(spread:pad, x1:0.996, y1:0.0340909, x2:1, y2:0, stop:1\n"
            "rgba(143,188,143, 1));\n")

        self.main_BOX = QtWidgets.QGroupBox(self.main_frame)
        self.main_BOX.setStyleSheet(
            "border-width: 0px;\n"
            "border-radius: 15px;\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-style: solid;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: qlineargradient(spread:pad, x1:0.996, y1:0.0340909, x2:1, y2:0, stop:1\n"
            "rgba(204, 229, 255, 1));\n")

        self.title = QtWidgets.QLabel(self.main_BOX)
        self.title.setGeometry(QtCore.QRect(30, 30, 200, 200))
        self.title.setText("WELCOME")
        self.title.setStyleSheet(
            "border-width: 2px;\n"
            "font : 18px Arial;"
            "border-style: solid;\n"
            "background: transparent;\n")

        self.backgroundImg = QtWidgets.QLabel(self.main_BOX)
        self.backgroundImg.setGeometry(QtCore.QRect(0, 0, 770, 429))
        self.backgroundImg.setPixmap(QtGui.QPixmap("../icons/backgroundBox.png"))
        self.backgroundImg.setScaledContents(True)
        self.backgroundImg.setStyleSheet(
            "border-width: 1px;\n"
            "border-radius: 1px;\n")

        self.messageBox = QtWidgets.QMessageBox()
        self.messageBox.setWindowIcon(QtGui.QIcon('../icons/errIcon.png'))
        self.messageBox.setWindowTitle("Error Message")
        self.messageBox.setIcon(QMessageBox.Critical)
        self.messageBox.setStyleSheet("QLabel{font-size: 20px; color: black;}")

        self.fakeFact_image = QtWidgets.QPushButton(self.main_BOX)
        self.fakeFact_image.setGeometry(QtCore.QRect(120, 230, 550, 200))
        self.fakeFact_image.setStyleSheet(
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "font-family: monospace;\n"
            "background: transparent;\n")
        imageIcon = QtGui.QIcon()
        imageIcon.addPixmap(QtGui.QPixmap("../icons/b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        size = QSize(500, 500)
        self.fakeFact_image.setIconSize(size)
        self.fakeFact_image.setIcon(imageIcon)

        self.leftSide_layout = QtWidgets.QGridLayout(self.main_frame)

        self.train_BOX = QtWidgets.QGroupBox(self.main_frame)
        self.train_BOX.setStyleSheet(
            "border-width: 1px;\n"
            "border-radius: 15px;\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-style: solid;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: qlineargradient(spread:pad, x1:0.996, y1:0.0340909, x2:1, y2:0, stop:1\n"
            "rgba(204, 229, 255, 1));\n")

        self.title = QtWidgets.QLabel(self.main_BOX)
        self.title.setGeometry(QtCore.QRect(260, 10, 270, 40))
        self.title.setText("WELCOME!")
        self.title.setStyleSheet(
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "font : 45px Georgia, serif;\n"
            "color: rgb(0, 100, 0);\n"
            "background: transparent;\n")
        self.header_title1 = QtWidgets.QLabel(self.main_BOX)
        self.header_title1.setGeometry(QtCore.QRect(170, 50, 450, 40))
        self.header_title1.setText("Are you ready to know the truth?")
        self.header_title1.setStyleSheet(
            "border-width: 0px;\n"
            "font : 30px Georgia, serif;"
            "border-style: solid;\n"
            "color: rgb(46,139,87);\n"
            "background: transparent;\n")
        self.header_title2 = QtWidgets.QLabel(self.main_BOX)
        self.header_title2.setGeometry(QtCore.QRect(10, 100, 800, 55))
        self.header_title2.setText("• Select the 'Tweet Classification' option and enter your text to detect whether\n   it is real or fake")
        self.header_title2.setStyleSheet(
            "border-width: 0px;\n"
            "font : 22px Calibri;"
            "border-style: solid;\n"
            "color: rgb(47,79,79);\n"
            "background: transparent;\n")
        self.header_title3 = QtWidgets.QLabel(self.main_BOX)
        self.header_title3.setGeometry(QtCore.QRect(10, 170, 800, 60))
        self.header_title3.setText("• You have the option to choose from pre-trained models or create your own\n   by selecting the 'Train New Model' option")
        self.header_title3.setStyleSheet(
            "border-width: 0px;\n"
            "font : 22px Calibri;"
            "color: rgb(47,79,79);\n"
            "border-style: solid;\n"
            "background: transparent;\n")

        self.backgroundImg = QtWidgets.QLabel(self.train_BOX)
        self.backgroundImg.setGeometry(QtCore.QRect(0, 0, 770, 429))
        self.backgroundImg.setPixmap(QtGui.QPixmap("../icons/backgroundBox.png"))
        self.backgroundImg.setScaledContents(True)
        self.backgroundImg.setStyleSheet(
            "border-width: 1px;\n"
            "border-radius: 1px;\n")

        self.radioBtn_main = QtWidgets.QRadioButton(self.groupBox)
        self.radioBtn_main.setAutoFillBackground(False)
        self.radioBtn_main.setText("Main page")
        self.radioBtn_main.setStyleSheet(
            "QRadioButton"
            "{"
            "font : 25px Arial;"
            "color: rgb(0, 0, 51);"
            "border-style: none;"
            "}"
            "QRadioButton::indicator::checked"
            "{"
            "border: 3px solid;"
            "border-color: white;"
            "border-radius: 6px;"
            "background-color: lightgreen;"
            "}")

        self.radioBtn_train = QtWidgets.QRadioButton(self.groupBox)
        self.radioBtn_train.setText("Train new model")
        self.radioBtn_train.setStyleSheet(
            "QRadioButton"
            "{"
            "font : 25px Arial;"
            "color: rgb(0, 0, 51);"
            "border-style: none;"
            "}"
            "QRadioButton::indicator::checked"
            "{"
            "border: 3px solid;"
            "border-color: white;"
            "border-radius: 6px;"
            "background-color: lightgreen;"
            "}")

        self.radioBtn_detection = QtWidgets.QRadioButton(self.groupBox)
        self.radioBtn_detection.setText("Tweet classification")
        self.radioBtn_detection.setStyleSheet(
            "QRadioButton"
            "{"
            "font : 25px Arial;"
            "color: rgb(0, 0, 51);"
            "border-style: none;"
            "}"
            "QRadioButton::indicator::checked"
            "{"
            "border: 3px solid;"
            "border-color: white;"
            "border-radius: 6px;"
            "background-color: lightgreen;"
            "}"
        )

        self.uploadCSV_title = QtWidgets.QLabel(self.train_BOX)
        self.uploadCSV_title.setGeometry(QtCore.QRect(10, 15, 130, 30))
        self.uploadCSV_title.setText("Upload CSV file:")
        self.uploadCSV_title.setStyleSheet(
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "background: transparent;\n"
            "font-family: monospace;\n")

        self.csv_pathLine = QtWidgets.QLineEdit(self.train_BOX)
        self.csv_pathLine.setGeometry(QtCore.QRect(150, 15, 550, 30))
        self.csv_pathLine.setReadOnly(True)
        self.csv_pathLine.setStyleSheet(
            "border-width: 1px;\n"
            "border-radius: 5px;\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-style: solid;\n"
            "background-color: rgb(255, 255, 255);\n"
            "color: rgb(0, 0, 0);\n"
            "background: transparent;\n"
            "font: 8pt \"Sitka Small\";\n")

        self.uploadCsv_btn = QtWidgets.QToolButton(self.train_BOX)
        self.uploadCsv_btn.setGeometry(QtCore.QRect(700, 15, 50, 30))
        self.uploadCsv_btn.setCursor(Qt.PointingHandCursor)
        self.uploadCsv_btn.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "border-width: 0px;\n"
            "border-radius: 0px;\n"
            "border-color: rgb(1, 1, 1);\n"
            "background: transparent;\n"
            "border-style: solid;\n")
        uploadIcon = QtGui.QIcon()
        uploadIcon.addPixmap(QtGui.QPixmap("../icons/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        size = QSize(25, 25)
        self.uploadCsv_btn.setIconSize(size)
        self.uploadCsv_btn.setIcon(uploadIcon)

        self.BERTCombo_title = QtWidgets.QLabel(self.train_BOX)
        self.BERTCombo_title.setGeometry(QtCore.QRect(10, 60, 155, 30))
        self.BERTCombo_title.setText("Embedding method:")
        self.BERTCombo_title.setStyleSheet(
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "background: transparent;\n"
            "font-family: monospace;\n")

        self.BERT_comboBox = QtWidgets.QComboBox(self.train_BOX)
        self.BERT_comboBox.setGeometry(QtCore.QRect(170, 60, 230, 30))
        self.BERT_comboBox.setStyleSheet(
            "background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,stop:0 honeydew, stop:1 honeydew);\n"
            "border-width: 2px;\n"
            "border-radius: 5px;\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-style: solid;\n")

        self.epoch_title = QtWidgets.QLabel(self.train_BOX)
        self.epoch_title.setGeometry(QtCore.QRect(10, 100, 80, 30))
        self.epoch_title.setText("Epoch:")
        self.epoch_title.setStyleSheet(
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "background: transparent;\n"
            "font-family: monospace;\n")

        self.epoch_input = QtWidgets.QLineEdit(self.train_BOX)
        self.epoch_input.setGeometry(QtCore.QRect(90, 100, 80, 30))
        self.epoch_input.setPlaceholderText("15")
        self.epoch_input.setStyleSheet(
            "border-width: 1px;\n"
            "background-color: white;\n"
            "border-style: solid;\n"
            "font-family: monospace;\n"
            "background: transparent;\n"
            "font-weight: bolder;\n")

        self.batchSize_title = QtWidgets.QLabel(self.train_BOX)
        self.batchSize_title.setGeometry(QtCore.QRect(10, 140, 80, 30))
        self.batchSize_title.setText("Batch size:")
        self.batchSize_title.setStyleSheet(
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "background: transparent;\n"
            "font-family: monospace;\n")

        self.batchSize_input = QtWidgets.QLineEdit(self.train_BOX)
        self.batchSize_input.setGeometry(QtCore.QRect(90, 140, 80, 30))
        self.batchSize_input.setPlaceholderText("10")
        self.batchSize_input.setStyleSheet(
            "border-width: 1px;\n"
            "background-color: white;\n"
            "border-style: solid;\n"
            "font-family: monospace;\n"
            "background: transparent;\n"
            "font-weight: bolder;\n")

        self.cnnLSTM_title = QtWidgets.QLabel(self.train_BOX)
        self.cnnLSTM_title.setGeometry(QtCore.QRect(10, 180, 160, 30))
        self.cnnLSTM_title.setText("Choose model type:")
        self.cnnLSTM_title.setStyleSheet(
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "background: transparent;\n"
            "font-family: monospace;\n")

        self.radioBtn_CNN = QtWidgets.QRadioButton(self.train_BOX)
        self.radioBtn_CNN.setGeometry(QtCore.QRect(170, 180, 160, 30))
        self.radioBtn_CNN.setText("CNN")
        self.radioBtn_CNN.setStyleSheet(
            "QRadioButton"
            "{"
            "font : 25px Arial;"
            "color: rgb(0, 0, 51);"
            "background: transparent;"
            "border-style: none;"
            "}"
            "QRadioButton::indicator::checked"
            "{"
            "border: 3px solid;"
            "border-color: black;"
            "border-radius: 6px;"
            "background-color: lightgreen;"
            "}"
        )

        self.radioBtn_LSTM = QtWidgets.QRadioButton(self.train_BOX)
        self.radioBtn_LSTM.setGeometry(QtCore.QRect(280, 180, 160, 30))
        self.radioBtn_LSTM.setText("LSTM")
        self.radioBtn_LSTM.setStyleSheet(
            "QRadioButton"
            "{"
            "font : 25px Arial;"
            "color: rgb(0, 0, 51);"
            "background: transparent;"
            "border-style: none;"
            "}"
            "QRadioButton::indicator::checked"
            "{"
            "border: 3px solid;"
            "border-color: black;"
            "border-radius: 6px;"
            "background-color: lightgreen;"
            "}"
        )

        self.cnnParam_BOX = QtWidgets.QGroupBox(self.train_BOX)
        self.cnnParam_BOX.setGeometry(QtCore.QRect(10, 230, 370, 180))
        self.cnnParam_BOX.setStyleSheet(
            "border-width: 1px;\n"
            "border-radius: 15px;\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-style: solid;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: qlineargradient(spread:pad, x1:0.996, y1:0.0340909, x2:1, y2:0, stop:1\n"
            "rgba(240,255,240, 1));\n")

        self.radioBtn_defaultCNN = QtWidgets.QRadioButton(self.cnnParam_BOX)
        self.radioBtn_defaultCNN.setGeometry(QtCore.QRect(10, 5, 100, 30))
        self.radioBtn_defaultCNN.setText("Default")
        self.radioBtn_defaultCNN.setStyleSheet(
            "QRadioButton"
            "{"
            "font : 18px Arial;"
            "color: rgb(0, 0, 51);"
            "border-style: none;"
            "}"
            "QRadioButton::indicator::checked"
            "{"
            "border: 3px solid;"
            "border-color: black;"
            "border-radius: 6px;"
            "background-color: lightgreen;"
            "width: 7px; "
            "height: 7px;"
            "}"
        )

        self.radioBtn_setParamsCNN = QtWidgets.QRadioButton(self.cnnParam_BOX)
        self.radioBtn_setParamsCNN.setGeometry(QtCore.QRect(10, 40, 250, 30))
        self.radioBtn_setParamsCNN.setText("Set your own parameters")
        self.radioBtn_setParamsCNN.setStyleSheet(
            "QRadioButton"
            "{"
            "font : 18px Arial;"
            "color: rgb(0, 0, 51);"
            "border-style: none;"
            "}"
            "QRadioButton::indicator::checked"
            "{"
            "border: 3px solid;"
            "border-color: black;"
            "border-radius: 6px;"
            "background-color: lightgreen;"
            "width: 7px; "
            "height: 7px;"
            "}"
        )

        self.numOfFilters_title = QtWidgets.QLabel(self.cnnParam_BOX)
        self.numOfFilters_title.setGeometry(QtCore.QRect(10, 80, 140, 30))
        self.numOfFilters_title.setText("Number of filters:")
        self.numOfFilters_title.setStyleSheet(
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "font-family: monospace;\n")

        self.filters_input = QtWidgets.QLineEdit(self.cnnParam_BOX)
        self.filters_input.setGeometry(QtCore.QRect(150, 80, 50, 30))
        self.filters_input.setToolTip('Number of filters')
        self.filters_input.setStyleSheet(
            "border-width: 1px;\n"
            "background-color: white;\n"
            "border-style: solid;\n"
            "font-family: monospace;\n"
            "font-weight: bolder;\n")

        self.kernelSize_title = QtWidgets.QLabel(self.cnnParam_BOX)
        self.kernelSize_title.setGeometry(QtCore.QRect(10, 120, 140, 30))
        self.kernelSize_title.setText("Kernel sizes:")
        self.kernelSize_title.setStyleSheet(
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "font-family: monospace;\n")

        self.filter1 = QtWidgets.QLineEdit(self.cnnParam_BOX)
        self.filter1.setGeometry(QtCore.QRect(150, 120, 50, 30))
        self.filter1.setToolTip('kernel size for first layer')
        self.filter1.setStyleSheet(
            "border-width: 1px;\n"
            "background-color: white;\n"
            "border-style: solid;\n"
            "font-family: monospace;\n"
            "font-weight: bolder;\n")

        self.filter2 = QtWidgets.QLineEdit(self.cnnParam_BOX)
        self.filter2.setGeometry(QtCore.QRect(210, 120, 50, 30))
        self.filter2.setToolTip('kernel size for second layer')
        self.filter2.setStyleSheet(
            "border-width: 1px;\n"
            "background-color: white;\n"
            "border-style: solid;\n"
            "font-family: monospace;\n"
            "font-weight: bolder;\n")

        self.filter3 = QtWidgets.QLineEdit(self.cnnParam_BOX)
        self.filter3.setGeometry(QtCore.QRect(270, 120, 50, 30))
        self.filter3.setToolTip('kernel size for third layer')
        self.filter3.setStyleSheet(
            "border-width: 1px;\n"
            "background-color: white;\n"
            "border-style: solid;\n"
            "font-family: monospace;\n"
            "font-weight: bolder;\n")

        self.lstmParam_BOX = QtWidgets.QGroupBox(self.train_BOX)
        self.lstmParam_BOX.setGeometry(QtCore.QRect(10, 230, 370, 180))
        self.lstmParam_BOX.setStyleSheet(
            "border-width: 1px;\n"
            "border-radius: 15px;\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-style: solid;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: qlineargradient(spread:pad, x1:0.996, y1:0.0340909, x2:1, y2:0, stop:1\n"
            "rgba(240,255,240, 1));\n")

        self.radioBtn_defaultLSTM = QtWidgets.QRadioButton(self.lstmParam_BOX)
        self.radioBtn_defaultLSTM.setGeometry(QtCore.QRect(5, 5, 100, 30))
        self.radioBtn_defaultLSTM.setText("Default")
        self.radioBtn_defaultLSTM.setStyleSheet(
            "QRadioButton"
            "{"
            "font : 18px Arial;"
            "color: rgb(0, 0, 51);"
            "border-style: none;"
            "}"
            "QRadioButton::indicator::checked"
            "{"
            "border: 3px solid;"
            "border-color: black;"
            "border-radius: 6px;"
            "background-color: lightgreen;"
            "width: 7px; "
            "height: 7px;"
            "}"
        )

        self.radioBtn_setParamsLSTM = QtWidgets.QRadioButton(self.lstmParam_BOX)
        self.radioBtn_setParamsLSTM.setGeometry(QtCore.QRect(5, 40, 250, 30))
        self.radioBtn_setParamsLSTM.setText("Set your own parameters")
        self.radioBtn_setParamsLSTM.setStyleSheet(
            "QRadioButton"
            "{"
            "font : 18px Arial;"
            "color: rgb(0, 0, 51);"
            "border-style: none;"
            "}"
            "QRadioButton::indicator::checked"
            "{"
            "border: 3px solid;"
            "border-color: black;"
            "border-radius: 6px;"
            "background-color: lightgreen;"
            "width: 7px; "
            "height: 7px;"
            "}"
        )

        self.numOfFilters_title = QtWidgets.QLabel(self.lstmParam_BOX)
        self.numOfFilters_title.setGeometry(QtCore.QRect(5, 80, 180, 30))
        self.numOfFilters_title.setText("Number of hidden units:")
        self.numOfFilters_title.setStyleSheet(
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "font-family: monospace;\n")

        self.numUnits_input = QtWidgets.QLineEdit(self.lstmParam_BOX)
        self.numUnits_input.setGeometry(QtCore.QRect(190, 80, 50, 30))
        self.numUnits_input.setStyleSheet(
            "border-width: 1px;\n"
            "background-color: white;\n"
            "border-style: solid;\n"
            "font-family: monospace;\n"
            "font-weight: bolder;\n")

        self.train_btn = QtWidgets.QPushButton(self.train_BOX)
        self.train_btn.setGeometry(QtCore.QRect(670, 340, 100, 80))
        self.train_btn.setCursor(Qt.PointingHandCursor)
        self.train_btn.setEnabled(True)
        self.train_btn.setStyleSheet(
            "QPushButton"
            "{"
            "background-color: transparent;\n"
            "border-width: 0px;\n"
            "}"
            "QToolTip"
            "{"
            "background-color: white;"
            "color: black;"
            "border: #8ad4ff solid 1px"
            "}")
        self.train_btn.setToolTip('Start training')
        trainIcon = QtGui.QIcon()
        trainIcon.addPixmap(QtGui.QPixmap("../icons/startBtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        size = QSize(70, 70)
        self.train_btn.setIconSize(size)
        self.train_btn.setIcon(trainIcon)

        # ---------------------------------- Train Window ----------------------------------#

        self.vertical_train = QtWidgets.QVBoxLayout(self.train_BOX)

        self.horizontal_upload = QtWidgets.QGridLayout(self.train_BOX)
        self.horizontal_epochBatch = QtWidgets.QGridLayout(self.train_BOX)
        self.horizontal_cnnLstm = QtWidgets.QGridLayout(self.train_BOX)

        self.vertical_train.addLayout(self.horizontal_upload)
        self.vertical_train.setContentsMargins(10, 0, 10, 0)

        self.vertical_train.addLayout(self.horizontal_epochBatch)
        self.horizontal_epochBatch.setContentsMargins(0, 0, 600, 150)

        self.vertical_train.addLayout(self.horizontal_cnnLstm)
        self.horizontal_cnnLstm.setContentsMargins(0, 0, 400, 0)

        self.leftSide_layout.addWidget(self.radioBtn_main, 0, 0)
        self.leftSide_layout.addWidget(self.radioBtn_train, 1, 0)
        self.leftSide_layout.addWidget(self.radioBtn_detection, 2, 0)

        self.leftSide_layout.addWidget(self.main_BOX)
        self.leftSide_layout.addWidget(self.train_BOX)

        # ---------------------------------- Detection Window ----------------------------------#

        self.detection_Box = QtWidgets.QGroupBox(self.main_frame)
        self.detection_Box.setStyleSheet(
            "border-width: 1px;\n"
            "border-radius: 15px;\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-style: solid;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: qlineargradient(spread:pad, x1:0.996, y1:0.0340909, x2:1, y2:0, stop:1\n"
            "rgba(204, 229, 255, 1));\n")

        self.backgroundImg = QtWidgets.QLabel(self.detection_Box)
        self.backgroundImg.setGeometry(QtCore.QRect(0, 0, 770, 429))
        self.backgroundImg.setPixmap(QtGui.QPixmap("../icons/backgroundBox.png"))
        self.backgroundImg.setScaledContents(True)
        self.backgroundImg.setStyleSheet(
            "border-width: 1px;\n"
            "border-radius: 1px;\n")

        self.selectModel_title = QtWidgets.QLabel()
        self.selectModel_title.setText("Select preferred model:")
        self.selectModel_title.setStyleSheet(
            "border-width: 0px;\n"
            "border-style: none;\n"
            "background: transparent;\n"
            "font-family: monospace;\n")

        self.comboBox = QtWidgets.QComboBox(self.detection_Box)
        self.comboBox.setStyleSheet(
            "background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,stop:0 whitesmoke, stop:1 darkseagreen		);\n"
            "border-width: 2px;\n"
            "border-radius: 5px;\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-style: solid;\n")

        self.tweet_textEdit = QtWidgets.QPlainTextEdit(self.detection_Box)
        self.tweet_textEdit.setPlaceholderText("Please enter your text here...")
        self.tweet_textEdit.setTabChangesFocus(False)
        self.tweet_textEdit.setOverwriteMode(False)
        self.tweet_textEdit.setStyleSheet(
            "border-width: 2px;\n"
            "border-radius: 5px;\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-style: solid;\n"
            "background-color: rgb(255,250,250);\n"
            "color: rgb(0, 0, 0);")

        self.start_btn = QtWidgets.QPushButton()
        self.start_btn.setToolTip('Check')
        self.start_btn.setCursor(Qt.PointingHandCursor)
        self.start_btn.setEnabled(True)
        self.start_btn.setGeometry(QtCore.QRect(530, 479, 240, 60))
        self.start_btn.setAcceptDrops(False)
        self.start_btn.setAutoFillBackground(False)
        self.start_btn.setCheckable(False)
        self.start_btn.setAutoDefault(False)
        self.start_btn.setDefault(False)
        self.start_btn.setFlat(False)
        self.start_btn.setStyleSheet(
            "QPushButton"
            "{"
            "background-color: transparent;\n"
            "border-width: 0px;\n"
            "border-radius: 0px;\n"
            "border-color: rgb(1, 1, 1);\n"
            "border-style: solid;\n"
            "}"
            "QToolTip"
            "{"
            "background-color: white;"
            "color: black;"
            "border: #8ad4ff solid 1px"
            "}")
        startIcon = QtGui.QIcon()
        startIcon.addPixmap(QtGui.QPixmap("../icons/startBtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        size = QSize(70, 70)
        self.start_btn.setIconSize(size)
        self.start_btn.setIcon(startIcon)

        self.vertical_detection = QtWidgets.QVBoxLayout(self.detection_Box)

        self.horizontal_start = QtWidgets.QHBoxLayout(self.detection_Box)
        self.horizontal_combobox = QtWidgets.QGridLayout(self.detection_Box)
        self.horizontalTweet = QtWidgets.QGridLayout(self.detection_Box)

        self.vertical_detection.addLayout(self.horizontal_combobox)
        self.vertical_detection.addLayout(self.horizontal_start)

        self.horizontal_combobox.addWidget(self.selectModel_title, 0, 0)
        self.horizontal_combobox.addWidget(self.comboBox, 1, 0)
        self.horizontal_combobox.addWidget(self.tweet_textEdit, 2, 0)
        self.horizontal_start.addWidget(self.start_btn)
        self.leftSide_layout.addWidget(self.detection_Box)

        MainWindow.setCentralWidget(self.centerWidget)
        self.reTranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def reTranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        self.csv_pathLine.setPlaceholderText(_translate("TrainNewsModelWindow", "/.."))
        MainWindow.setWindowIcon(QtGui.QIcon('../icons/network-detection.png'))
        MainWindow.setWindowTitle("Text Classification")

    @property
    def input1(self):
        return self.filter1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainDesign()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
