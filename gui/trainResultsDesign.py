import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt


class Ui_TrainResultsWindow(object):
    def __init__(self):
        self.result_title = None
        self.result_input = None
        self.resultText = None
        self.lossLabel = None
        self.accLabel = None
        self.saveBtn = None
        self.backBtn = None
        self.groupBox = None
        self.centralWidget = None

    def setupUi(self, TrainResultsWindow):
        TrainResultsWindow.resize(1400, 730)
        TrainResultsWindow.setFixedSize(1400, 730)

        self.centralWidget = QtWidgets.QWidget(TrainResultsWindow)

        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(30, 0, 1340, 700))
        self.groupBox.setStyleSheet("color: rgb(1, 1, 1);")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setStyleSheet(
            "border-width: 2px;\n"
            "border-radius: 15px;\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-style: solid;\n"
            "font: 8pt \"Sitka Small\";\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: qlineargradient(spread:pad, x1:0.996, y1:0.0340909, x2:1, y2:0, stop:1\n"
            "rgba(240, 255, 240, 1));\n")

        self.accLabel = QtWidgets.QLabel(self.groupBox)
        self.accLabel.setGeometry(QtCore.QRect(30, 20, 620, 460))
        self.accLabel.setStyleSheet(
            "border-color: black;\n"
            "border-width: 1px;\n"
            "border-style: solid;\n"
            "background-color: qlineargradient(spread:pad, x1:0.996, y1:0.0340909, x2:1, y2:0, stop:1\n"
            "rgba(143,188,143, 1));\n")

        self.lossLabel = QtWidgets.QLabel(self.groupBox)
        self.lossLabel.setGeometry(QtCore.QRect(690, 20, 620, 460))
        self.lossLabel.setStyleSheet(
            "border-color: black;\n"
            "border-width: 1px;\n"
            "border-style: solid;\n"
            "background-color: qlineargradient(spread:pad, x1:0.996, y1:0.0340909, x2:1, y2:0, stop:1\n"
            "rgba(143,188,143, 1));\n"
        )

        self.result_title = QtWidgets.QLabel(self.groupBox)
        self.result_title.setGeometry(QtCore.QRect(570, 515, 320, 160))
        self.result_title.setStyleSheet(
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "padding: 10px;\n"
            "font : 22px serif;\n"
            "color: rgb(47,79,79);\n"
            "background: transparent;\n")

        self.result_input = QtWidgets.QLineEdit(self.groupBox)
        self.result_input.setGeometry(QtCore.QRect(395, 570, 170, 30))
        self.result_input.setStyleSheet(
            "border-width: 0px;\n"
            "background-color: white;\n"
            "border-style: solid;\n"
            "font-family: monospace;\n"
            "background: transparent;\n"
            "font : 18px Arial;")

        self.backBtn = QtWidgets.QPushButton(self.groupBox)
        self.backBtn.setEnabled(True)
        self.backBtn.setGeometry(QtCore.QRect(0, 600, 240, 80))
        self.backBtn.setMinimumSize(QSize(100, 100))
        self.backBtn.setToolTip('Back to the main page')
        self.backBtn.setAcceptDrops(False)
        self.backBtn.setAutoFillBackground(False)
        self.backBtn.setCheckable(False)
        self.backBtn.setAutoDefault(False)
        self.backBtn.setDefault(False)
        self.backBtn.setFlat(False)
        self.backBtn.setCursor(Qt.PointingHandCursor)
        uploadIcon = QtGui.QIcon()
        uploadIcon.addPixmap(QtGui.QPixmap("../icons/backBtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        size = QSize(70, 70)
        self.backBtn.setIconSize(size)
        self.backBtn.setIcon(uploadIcon)
        self.backBtn.setStyleSheet(
            "QPushButton"
            "{"
            "background-color: rgba(0, 0, 0, 0);\n"
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

        self.saveBtn = QtWidgets.QPushButton(self.groupBox)
        self.saveBtn.setToolTip('Save trained model')
        self.saveBtn.setEnabled(True)
        self.saveBtn.setGeometry(QtCore.QRect(1100, 600, 240, 60))
        self.saveBtn.setMinimumSize(QSize(100, 100))
        self.saveBtn.setAcceptDrops(False)
        self.saveBtn.setAutoFillBackground(False)
        self.saveBtn.setCheckable(False)
        self.saveBtn.setAutoDefault(False)
        self.saveBtn.setDefault(False)
        self.saveBtn.setFlat(False)
        self.saveBtn.setCursor(Qt.PointingHandCursor)
        uploadSaveIcon = QtGui.QIcon()
        uploadSaveIcon.addPixmap(QtGui.QPixmap("../icons/555.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        size = QSize(60, 60)
        self.saveBtn.setIconSize(size)
        self.saveBtn.setIcon(uploadSaveIcon)
        self.saveBtn.setStyleSheet(
            "QPushButton"
            "{"
            "background-color: rgba(0, 0, 0, 0);\n"
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

        TrainResultsWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(TrainResultsWindow)
        QtCore.QMetaObject.connectSlotsByName(TrainResultsWindow)

    def retranslateUi(self, TrainResultsWindow):
        _translate = QtCore.QCoreApplication.translate
        TrainResultsWindow.setWindowTitle("Training Results")
        TrainResultsWindow.setWindowIcon(QtGui.QIcon('../icons/network-detection.png'))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    TrainResultsWindow = QtWidgets.QMainWindow()
    ui = Ui_TrainResultsWindow()
    ui.setupUi(TrainResultsWindow)
    TrainResultsWindow.show()
    sys.exit(app.exec_())
