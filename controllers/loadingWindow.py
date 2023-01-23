import os
import threading
import time
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal

TRAINED_MODELS_PATH: str = "../trained_models/"


class LoadingWindow(QMainWindow):
    progress_signal = pyqtSignal(int)  # Define a new signal for progress bar

    def __init__(self, content, model_name, detectionFlag, task, parent=None):
        super(LoadingWindow, self).__init__(parent)
        self.t = None
        self.t2 = None
        self.t1 = None
        self.detection = None
        self.window = None
        self.detectionFlag = detectionFlag
        self.progress_signal.connect(self.update_progress_bar)  # Connect the signal to a slot
        self.content = content
        self.model_name = model_name
        self.task = task
        from gui.loadingWindowDesign import Ui_LoadingWindowDesign
        self.ui = Ui_LoadingWindowDesign(detectionFlag)
        self.ui.setupUi(self)
        self.ui.resultsBtn.setHidden(True)
        self.task_progress = 0
        self.set_buttons_handlers()
        self.run_function()

    def run_function(self):
        if self.detectionFlag:
            # Threads for running detection process
            self.t1 = threading.Thread(target=self.run_detection, args=(self.content, self.model_name))
            self.t1.start()
            self.t2 = threading.Thread(target=self.run_waiting_detection)
            self.t2.start()
            self.progress_signal.emit(self.task_progress)  # Emit the signal with the current progress value
        else:
            # Threads for running training process
            self.task.start_train_model()
            self.t = threading.Thread(target=self.run_waiting_training)
            self.t.start()

    def run_detection(self, content, model_name):
        from model.tweetDetection import TweetDetection
        os.chdir("../")
        # Detecting on chosen model
        self.detection = TweetDetection(input=content, model_name=model_name + ".h5")
        os.chdir("controllers")

    # Updating progress bar
    def update_progress_bar(self, progress):
        self.ui.progress_bar.setValue(progress)

    def set_buttons_handlers(self):
        if self.detectionFlag:
            # Open detection results window after detecting process ends
            self.ui.resultsBtn.clicked.connect(self.open_detection_results)
        else:
            # Open training results window after training process ends
            self.ui.resultsBtn.clicked.connect(self.open_train_results)

    def run_waiting_detection(self):
        while self.t1.is_alive():  # Keep updating the progress bar as long as the thread is running
            self.task_progress += 1  # Increment the task progress by 1%
            time.sleep(0.15)
            self.progress_signal.emit(self.task_progress)  # Emit the signal with the current progress value
            self.ui.progress_bar.valueChanged.connect(self.update_progress_bar)
        time.sleep(0.1)
        self.ui.progress_bar.setValue(100)  # Set the value of the progress bar to the final progress value
        self.ui.resultsBtn.click()

    def run_waiting_training(self):
        while self.task.running:
            time.sleep(3)
        self.ui.resultsBtn.click()

    def open_detection_results(self):
        self.close()
        from controllers.detectionResults import Results
        self.window = Results(self.detection)
        self.window.show()

    def open_train_results(self):
        self.task.test_model()
        self.close()
        from controllers.trainResults import TrainResultsWinController
        self.window = TrainResultsWinController(self.task)
        self.window.show()
