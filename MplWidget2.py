from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import random
import datetime
import random
import matplotlib.pyplot as plt

class MplWidget2(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        t = np.arange(0.0, 2.0, 0.01)
        s = 1 + np.sin(2 * np.pi * t)
        self.canvas = FigureCanvas(Figure())
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)
        self.canvas.axes.clear()
        self.canvas.draw()
