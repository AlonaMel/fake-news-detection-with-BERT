import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt


class Ui_ResultsDesign(object):
    def __init__(self):
        self.result_input = None
        self.result_title = None
        self.horizontal = None
        self.detection_plot = None
        self.vertical = None
        self.backBtn = None
        self.messageBox = None
        self.up_frame = None
        self.redBOX = None
        self.frame = None
        self.centralWidget = None
        self.groupBox = None

    def setupUi(self, results):
        results.resize(800, 730)
        results.setFixedSize(800, 730)

        self.centralWidget = QtWidgets.QWidget(results)

        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(30, 0, 740, 700))
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

        self.detection_plot = QtWidgets.QLabel(self.groupBox)
        self.detection_plot.setGeometry(QtCore.QRect(60, 20, 620, 500))
        self.detection_plot.setStyleSheet(
            "border-color: black;\n"
            "border-width: 1px;\n"
            "border-style: solid;\n"
            "background-color: qlineargradient(spread:pad, x1:0.996, y1:0.0340909, x2:1, y2:0, stop:1\n"
            "rgba(143,188,143, 1));\n")

        self.result_title = QtWidgets.QLabel(self.groupBox)
        self.result_title.setGeometry(QtCore.QRect(165, 570, 240, 30))
        self.result_title.setStyleSheet(
            "border-width: 0px;\n"
            "font : 25px Arial;"
            "border-style: solid;\n"
            "background: transparent;\n")

        self.result_input = QtWidgets.QLineEdit(self.groupBox)
        self.result_input.setGeometry(QtCore.QRect(395, 570, 170, 30))
        self.result_input.setStyleSheet(
            "border-width: 0px;\n"
            "background-color: white;\n"
            "border-style: solid;\n"
            "font-family: monospace;\n"
            "background: transparent;\n"
            "font : 25px Arial;")

        self.fakeFact_image = QtWidgets.QPushButton(self.groupBox)
        self.fakeFact_image.setGeometry(QtCore.QRect(430, 400, 300, 300))
        self.fakeFact_image.setStyleSheet(
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "font-family: monospace;\n"
            "background: transparent;\n")
        imageIcon = QtGui.QIcon()
        imageIcon.addPixmap(QtGui.QPixmap("../icons/d.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        size = QSize(300, 300)
        self.fakeFact_image.setIconSize(size)
        self.fakeFact_image.setIcon(imageIcon)

        self.backBtn = QtWidgets.QPushButton(self.groupBox)
        self.backBtn.setEnabled(True)
        self.backBtn.setGeometry(QtCore.QRect(0, 600, 100, 80))
        self.backBtn.setMinimumSize(QSize(100, 100))
        self.backBtn.setToolTip('Back to the main page')
        self.backBtn.setAcceptDrops(False)
        self.backBtn.setAutoFillBackground(False)
        self.backBtn.setCheckable(False)
        self.backBtn.setAutoDefault(False)
        self.backBtn.setDefault(False)
        self.backBtn.setFlat(False)
        self.backBtn.setCursor(Qt.PointingHandCursor)
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
        uploadIcon = QtGui.QIcon()
        uploadIcon.addPixmap(QtGui.QPixmap("../icons/backBtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        size = QSize(70, 70)
        self.backBtn.setIconSize(size)
        self.backBtn.setIcon(uploadIcon)

        results.setCentralWidget(self.centralWidget)

        self.retranslateUi(results)
        QtCore.QMetaObject.connectSlotsByName(results)

    def retranslateUi(self, results):
        _translate = QtCore.QCoreApplication.translate
        results.setWindowIcon(QtGui.QIcon('../icons/network-detection.png'))
        results.setWindowTitle("Detection Results")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    results = QtWidgets.QMainWindow()
    ui = Ui_ResultsDesign()
    ui.setupUi(results)
    results.show()
    sys.exit(app.exec_())
