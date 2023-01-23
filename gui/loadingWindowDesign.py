from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QMovie
import sys


class Ui_LoadingWindowDesign(QObject):
    def __init__(self, detectionFlag):
        super(Ui_LoadingWindowDesign, self).__init__()
        self.detectionFlag = detectionFlag
        self.progress_bar = None
        self.waitText = None
        self.horizontal = None
        self.waitLabel = None
        self.frame = None
        self.vertical = None
        self.loadingGif = None
        self.loadinLabel = None
        self.resultsBtn = None
        self.groupBox = None
        self.centralWidget = None

    def update_progress_bar(self, progress):
        self.progress_bar.setValue(progress)  # Set the value of the progress bar

    def setupUi(self, LoadingWindow):
        LoadingWindow.resize(860, 396)
        LoadingWindow.setFixedSize(860, 396)

        self.centralWidget = QtWidgets.QWidget(LoadingWindow)

        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setGeometry(QtCore.QRect(30, 0, 800, 370))

        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 370))
        self.frame.setStyleSheet(
            "border-width: 2px;\n"
            "border-radius: 15px;\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-style: solid;\n"
            "font: 8pt \"Sitka Small\";\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: qlineargradient(spread:pad, x1:0.996, y1:0.0340909, x2:1, y2:0, stop:1\n"
            "rgba(240,255,240, 1));\n")

        self.resultsBtn = QtWidgets.QPushButton(self.centralWidget)

        if not self.detectionFlag:
            self.waitText = "Training process is running"
        else:
            self.waitText = "Detection process is running"

            self.progress_bar = QtWidgets.QProgressBar(self.frame)  # Create a progress bar widget
            self.progress_bar.setGeometry(QtCore.QRect(150, 300, 500, 30))  # left, high, width, shape high
            self.progress_bar.setRange(0, 99)  # Set the range of the progress bar to be from 0% to 100%
            self.progress_bar.setStyleSheet(
                "QProgressBar"
                "{"
                "text-align: center;"
                " color: black; "
                "font : 20px Arial;"
                "border: 2px solid #98FB98;"
                "border-radius: 5px;"
                "background-color: transparent;"
                "}"
                "QProgressBar::chunk "
                "{background-color: #98FB98;"
                "width: 10px;"
                "margin: 0.5px;"
                "border-radius :1px;"
                "}")

        self.loadinLabel = QtWidgets.QLabel(self.frame)
        self.loadinLabel.setGeometry(QtCore.QRect(250, 130, 240, 121))
        self.loadinLabel.setMinimumSize(QSize(300, 150))
        self.loadinLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loadinLabel.setStyleSheet("border-color: transparent;")
        self.loadingGif = QMovie("../icons/35771931234507.564a1d2403b3a.gif")
        self.loadinLabel.setMovie(self.loadingGif)
        self.loadingGif.start()

        self.waitLabel = QtWidgets.QLabel()
        self.waitLabel.setText(self.waitText)
        self.waitLabel.setStyleSheet(
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "font : 30px Arial;\n")

        self.vertical = QtWidgets.QVBoxLayout(self.frame)
        self.horizontal = QtWidgets.QGridLayout(self.frame)

        self.vertical.addLayout(self.horizontal)
        self.horizontal.setContentsMargins(200, 0, 160, 250)

        self.horizontal.addWidget(self.waitLabel)

        LoadingWindow.setCentralWidget(self.centralWidget)
        self.reTranslateUi(LoadingWindow)
        QtCore.QMetaObject.connectSlotsByName(LoadingWindow)

    def reTranslateUi(self, LoadingWindow):
        _translate = QtCore.QCoreApplication.translate
        LoadingWindow.setWindowIcon(QtGui.QIcon('../icons/network-detection.png'))
        LoadingWindow.setWindowTitle("Loading")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LoadingWindow = QtWidgets.QMainWindow()
    ui = Ui_LoadingWindowDesign()
    ui.setupUi(LoadingWindow)
    LoadingWindow.show()
    sys.exit(app.exec_())
