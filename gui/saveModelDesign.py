import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMessageBox


class Ui_SaveModelWindow(object):
    def __init__(self):
        self.save_label = None
        self.horizontalLayout = None
        self.verticalLayout = None
        self.inputName = None
        self.saveBtn = None
        self.messageBox = None
        self.centralWidget = None
        self.up_frame = None
        self.backBtn = None
        self.groupBox = None

    def setupUi(self, SaveModelWindow):
        SaveModelWindow.resize(860, 396)
        SaveModelWindow.setFixedSize(860, 396)

        self.centralWidget = QtWidgets.QWidget(SaveModelWindow)

        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(30, 0, 800, 370))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)

        self.up_frame = QtWidgets.QFrame(self.groupBox)
        self.up_frame.setGeometry(QtCore.QRect(0, 0, 800, 370))
        self.up_frame.setStyleSheet(
            "border-width: 2px;\n"
            "border-radius: 15px;\n"
            "border-style: solid;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: qlineargradient(spread:pad, x1:0.996, y1:0.0340909, x2:1, y2:0, stop:1\n"
            "rgb(240, 255, 240));\n")
        
        self.save_label = QtWidgets.QLabel(self.up_frame)
        self.save_label.setGeometry(QtCore.QRect(320, 5, 200, 100))
        self.save_label.setText('Save Model')
        self.save_label.setStyleSheet(
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "font : 30px Arial;\n")

        self.messageBox = QtWidgets.QMessageBox()
        self.messageBox.setWindowIcon(QtGui.QIcon('../icons/errIcon.png'))
        self.messageBox.setWindowTitle("Error Message")
        self.messageBox.setIcon(QMessageBox.Critical)
        self.messageBox.setStyleSheet("QLabel{font-size: 20px; color: black;}")

        self.saveBtn = QtWidgets.QPushButton(self.up_frame)
        self.saveBtn.setEnabled(True)
        self.saveBtn.setGeometry(QtCore.QRect(680, 290, 100, 80))
        self.saveBtn.setToolTip('save your model')
        self.saveBtn.setAcceptDrops(False)
        self.saveBtn.setAutoFillBackground(False)
        self.saveBtn.setCheckable(False)
        self.saveBtn.setAutoDefault(False)
        self.saveBtn.setDefault(False)
        self.saveBtn.setFlat(False)
        self.saveBtn.setCursor(Qt.PointingHandCursor)
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
        uploadSaveIcon = QtGui.QIcon()
        uploadSaveIcon.addPixmap(QtGui.QPixmap("../icons/555.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        size = QSize(60, 60)
        self.saveBtn.setIconSize(size)
        self.saveBtn.setIcon(uploadSaveIcon)

        self.backBtn = QtWidgets.QPushButton(self.up_frame)
        self.backBtn.setEnabled(True)
        self.backBtn.setGeometry(QtCore.QRect(0, 290, 100, 80))
        self.backBtn.setToolTip('Back to results')
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

        self.inputName = QtWidgets.QLineEdit()
        self.inputName.setAlignment(QtCore.Qt.AlignCenter)
        self.inputName.setStyleSheet(
            "border-width: 2px;\n"
            "border-radius: 5px;\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-style: solid;\n"
            "background-color: rgb(255, 255, 255);\n"
            "color: rgb(0, 0, 0);")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.up_frame)
        self.horizontalLayout = QtWidgets.QGridLayout(self.up_frame)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout.addWidget(self.inputName, 2, 0)

        SaveModelWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(SaveModelWindow)
        QtCore.QMetaObject.connectSlotsByName(SaveModelWindow)

    def retranslateUi(self, SaveModelWindow):
        _translate = QtCore.QCoreApplication.translate
        SaveModelWindow.setWindowTitle(_translate("SaveModelWindow", "Save Model"))
        SaveModelWindow.setWindowIcon(QtGui.QIcon('../icons/network-detection.png'))
        self.inputName.setPlaceholderText(_translate("SaveModelWindow", "Choose name for you new model..."))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    SaveModelWindow = QtWidgets.QMainWindow()
    ui = Ui_SaveModelWindow()
    ui.setupUi(SaveModelWindow)
    SaveModelWindow.show()
    sys.exit(app.exec_())
