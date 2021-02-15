from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import pandas as pd
from form import Ui_MainWindow

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.df = pd.read_csv("worldometer_data.csv")

    def Country(self):
        Countrys = self.df["Country/Region"]
        for i in Countrys:
            self.ui.comboBox.addItem(i)
        self.ui.pushButton.clicked.connect(self.on_clicked)
        
    def on_clicked(self):
        MyCountry = self.ui.comboBox.currentText()
        MC = self.df[self.df["Country/Region"] == MyCountry] ["TotalDeaths"].iloc[0]
        MyCountry = str(int(MC))
        self.ui.label_2.setText(MyCountry)


def myAPP():
    myAPP = QtWidgets.QApplication(sys.argv)
    win = App()
    win.Country()
    win.show()
    sys.exit(myAPP.exec_())

myAPP()