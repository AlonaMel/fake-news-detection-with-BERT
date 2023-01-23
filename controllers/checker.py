import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

#methods which are responsible for widgets design and error messages


def set_normal_style(widget):
    widget.setStyleSheet(
        "border-width: 1px;\n"
        "background-color: white;\n"
        "border-style: solid;\n"
        "font-family: monospace;\n"
        "font-weight: bolder;\n")
    widget.update()


def set_error_style(widget):
    widget.setStyleSheet(
        "border-width: 2px;\n"
        "border-radius: 2px;\n"
        "border-color: rgb(170, 0, 0);\n"
        "border-style: dotted;\n"
        "background-color: white;\n"
        "color: rgb(0, 0, 0);\n")
    widget.update()


class Checker(QMainWindow):
    def __init__(self, parent=None):
        super(Checker, self).__init__(parent)
        self.allOk = None

    def clear_feedback(self):
        self.allOk = True
        self.ui.messageBox.setText("")

    def model_not_selected(self, msg):
        self.allOk = False
        self.show_error_msg(msg)

    def invalid_input(self, msg, widget):
        self.allOk = False
        self.setFeedback(msg, widget)

    def setFeedback(self, msg, widget):
        self.show_error_msg(msg)
        set_error_style(widget)

    def show_error_msg(self, msg):
        curr_msg = self.ui.messageBox.text()
        if curr_msg != "":
            curr_msg += "\n"
        self.ui.messageBox.setText(curr_msg + msg)

        self.ui.messageBox.adjustSize()
        self.ui.messageBox.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Checker()
    MainWindow.show()
    sys.exit(app.exec_())
