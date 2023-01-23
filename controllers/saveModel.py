from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMessageBox
from controllers.checker import Checker, set_normal_style


class SaveModelWinController(Checker):
    def __init__(self, task, parent=None):
        super(SaveModelWinController, self).__init__(parent)
        self.msgIcon = None
        self.name_widget_str = None
        self.window = None
        self.msgTitle = None
        self.msgContent = None
        self.msgWindowIcon = None
        self.task = task
        from gui.saveModelDesign import Ui_SaveModelWindow
        self.ui = Ui_SaveModelWindow()
        self.ui.setupUi(self)
        self.ui.inputName.setPlaceholderText("Enter a name for your model...")
        self.set_buttons_handlers()
        self.allOk = True

    def set_buttons_handlers(self):
        self.ui.backBtn.clicked.connect(self.back_pressed)
        self.ui.saveBtn.clicked.connect(self.save_pressed)

    def back_pressed(self):
        self.close()
        from controllers.trainResults import TrainResultsWinController
        self.window = TrainResultsWinController(self.task)
        self.window.show()

    def save_pressed(self):
        name_widget = self.ui.inputName
        self.name_widget_str = name_widget.text()
        # Checking new model name to save
        if self.name_widget_str == "":
            self.invalid_input("The model must be named", name_widget)
        else:
            set_normal_style(name_widget)
            if self.task.save_model(self.name_widget_str):
                self.massage()
            else:
                reply = QMessageBox.question(self, 'Clarification',
                                             "The destination already has a file named '" + self.name_widget_str + "'\n\nDo you want to replace the file in the destination?",
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    if self.task.save_model(model_name=self.name_widget_str, replace=True):
                        self.massage()

    def back_to_main_win(self):
        self.close()
        from controllers.main import Main
        self.window = Main()
        self.window.show()

    # A pop-up massage says model saved successfully
    def massage(self):
        size = QtCore.QSize(80, 80)
        msg = QMessageBox()
        msg.setWindowTitle('Confirmation')
        msg.setText('Your model successfully saved')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setIconPixmap(QPixmap('../icons/8316656.png').scaled(size))
        msg.setWindowIcon(QIcon('../icons/v.png'))
        msg.exec_()
        self.back_to_main_win()
