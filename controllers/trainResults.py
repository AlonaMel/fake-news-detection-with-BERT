from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox

TRAINED_MODELS_PATH: str = "trained_models/"
PLOTS_PATH = "results/plots/"


class TrainResultsWinController(QMainWindow):
    def __init__(self, task, parent=None):
        super(TrainResultsWinController, self).__init__(parent)
        self.window = None
        self.task = task
        from gui.trainResultsDesign import Ui_TrainResultsWindow
        self.ui = Ui_TrainResultsWindow()
        self.ui.setupUi(self)
        self.update_ui_with_data()
        self.set_buttons_handlers()

    # Update and display training plot results
    def update_ui_with_data(self):
        self.task.create_accuracy_graph()
        self.task.create_loss_graph()

        self.set_graph(widget=self.ui.accLabel, plot_path=self.task.acc_path)
        self.set_graph(widget=self.ui.lossLabel, plot_path=self.task.loss_path)

        text = "• True predicted: " + str(self.task.model.count_well_predicted) + "\n" \
               + "• False predicted: " + str(self.task.model.count_false_predicted) + "\n" \
               + "• Total test accuracy " + "{:.1f}%".format(self.task.model.test_accuracy * 100.0) + "\n" \
               + "• Train accuracy: " + "{:.1f}%".format(self.task.model.train_accuracy * 100.0) + "\n" \
               + "• Validation accuracy: " + "{:.1f}%".format(self.task.model.valid_accuracy * 100.0)
        self.ui.result_title.setText(text)

    def set_buttons_handlers(self):
        self.ui.backBtn.clicked.connect(self.train_again_pressed)
        self.ui.saveBtn.clicked.connect(self.save_pressed)

    @staticmethod
    def set_graph(widget, plot_path):
        pixmap = QtGui.QPixmap("../" + plot_path)
        pixmap_small = pixmap.scaled(620, 420)
        widget.setPixmap(pixmap_small)

    # Warning message pop up when exit before saving the new model
    def train_again_pressed(self):
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setWindowIcon(QIcon('../icons/exclamation.png'))
        msg.setText("Are you sure you want to leave without saving?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Cancel)
        msg.setInformativeText("The trained model will be lost")
        msg.buttonClicked.connect(self.pop_up_action)
        msg.exec_()

    def pop_up_action(self, i):
        if i.text() == 'OK':
            self.close()
            from controllers.main import Main
            self.window = Main()
            self.window.show()

    # To open save new model window
    def save_pressed(self):
        self.close()
        from controllers.saveModel import SaveModelWinController
        self.window = SaveModelWinController(self.task)
        self.window.show()
