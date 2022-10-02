# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 22:59:51 2022

@author: MarthaHT
"""

#GUI imports
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
#function imports
from functions import frame1, frame21,frame31, frameop5, frameop4, frameop3, frameop2, frameop1, grid

#initiallize GUI application
app = QApplication(sys.argv)

#window and settings
window = QWidget()
window.setWindowTitle("NASA Space Apps Challenge 2022")
window.setFixedWidth(1000)
window.setStyleSheet("background: #161219;")

#display frame 1
frame1()



window.setLayout(grid)

window.show()
sys.exit(app.exec()) #terminate the app widgets["button2"].append(button2)

