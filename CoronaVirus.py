from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import pandas as pd
from Form import Ui_MainWindow

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.df = pd.read_csv("worldometer_data.csv")

    def Country(self):
        selam = self.df["Country/Region"]
        print(selam)
        for i in selam:
            self.ui.comboBox.addItem(i)
            
def myAPP():
    myAPP = QtWidgets.QApplication(sys.argv)
    win = App()
    win.Country()
    win.show()
    sys.exit(myAPP.exec_())

myAPP()