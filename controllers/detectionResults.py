import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow


class Results(QMainWindow):
    def __init__(self, detection, parent=None):
        super(Results, self).__init__(parent)
        self.window = None
        from gui.detectionResultsDesign import Ui_ResultsDesign
        self.ui = Ui_ResultsDesign()
        self.ui.setupUi(self)
        self.detection = detection
        self.update_ui_with_data(detection)
        self.set_buttons_handlers()

    def set_buttons_handlers(self):
        self.ui.backBtn.clicked.connect(self.back_pressed)

    def back_pressed(self):
        self.close()
        from controllers.main import Main
        self.window = Main()
        self.window.show()

    # Update and display detection plot results
    def update_ui_with_data(self, detection):
        detection.create_distribution_plot()
        self.set_graph(widget=self.ui.detection_plot, plot_path=detection.pie_plot_path)
        if self.detection.real_percent > self.detection.fake_percent:
            text1 = "real"
            self.ui.fakeFact_image.setHidden(True)
        else:
            text1 = "real"
            self.ui.fakeFact_image.setHidden(False)
        text = "This tweet is " + "{:.1f}%".format(self.detection.real_percent)
        self.ui.result_title.setText(text)
        self.ui.result_input.setText(text1)
        self.ui.result_input.setReadOnly(True)


    @staticmethod
    def set_graph(widget, plot_path):
        pixmap = QtGui.QPixmap("../" + plot_path)
        pixmap_small = pixmap.scaled(620, 420)
        widget.setPixmap(pixmap_small)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Results()
    MainWindow.show()
    sys.exit(app.exec_())
