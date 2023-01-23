import csv
import matplotlib.pyplot as plt
from pathlib import Path
from model.detection import Detection

PLOTS_PATH = "results/plots/"
CSV_RESULTS = "results/CSV_results/"


class TweetDetection(Detection):
    def __init__(self, input, model_name):
        super().__init__(input=input, model_name=model_name)
        results_csv_path = CSV_RESULTS + str(model_name).rstrip(".h5") + '- Detection results.csv'
        self.write_results_to_file(file_path=results_csv_path, text=input, real_percent=self.real_percent)
        self.pie_plot_path = PLOTS_PATH + "ModelAcc2.png"

    # create plot for detection results
    def create_distribution_plot(self):
        data = [self.real_percent, self.fake_percent]
        myLabels = ["Real", "Fake"]

        def func(pct):
            return "{:.1f}%\n".format(pct)

        plt.subplots(figsize=(7, 5))
        plt.figure(facecolor='honeydew')
        ax = plt.axes()
        wedges, texts, autotexts = ax.pie(data,
                                          autopct=lambda pct: func(pct),
                                          explode=(0, 0.1),
                                          shadow=True,
                                          labels=myLabels,
                                          pctdistance=0.7,
                                          colors=("#00FF7F", "#FF4500"),
                                          startangle=270,
                                          wedgeprops={'linewidth': 1, 'edgecolor': "honeydew"},
                                          textprops=dict(color="black", size=12))
        plt.legend(['Real', 'Fake'])
        plt.setp(autotexts, size=17)
        plt.savefig("../" + self.pie_plot_path)
        plt.close()

    # Creates CSV file and inserts the results to the file. Each row represents new checked tweet
    @staticmethod
    def write_results_to_file(file_path, text, real_percent):
        file_exist = Path(file_path).exists()
        with open(file_path, 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            if not file_exist:
                header = ['text', 'reliable news percent', 'real classification (if exist)']
                writer.writerow(header)
            data = [text, "This tweet {:.1f}%".format(real_percent) + ' real']
            writer.writerow(data)
