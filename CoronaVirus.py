from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import pandas as pd

df = pd.read_csv("worldometer_data.csv")
result = df.head(10)
print(result)
