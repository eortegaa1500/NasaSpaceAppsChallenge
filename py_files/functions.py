# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 22:59:20 2022

@author: MarthaHT
"""

from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtCore
from urllib.request import urlopen
import json
import pandas as pd
import random

from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2
import time
from PIL import ImageQt
from PIL import Image, ImageDraw
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

from ec import ec
from un import un

#open api link to database
with urlopen("https://opentdb.com/api.php?amount=50&category=18&difficulty=medium&type=multiple") as webpage:
    #read JSON file & extract data
    data = json.loads(webpage.read().decode())
    df = pd.DataFrame(data["results"])

#load 1 instance of questions & answers at a time from the database
def preload_data(idx):
    #idx parm: selected randomly time and again at function call
    question = df["question"][idx]
    correct = df["correct_answer"][idx]
    wrong = df["incorrect_answers"][idx]

    #fixing charecters with bad formatting
    formatting = [
        ("#039;", "'"),
        ("&'", "'"),
        ("&quot;", '"'),
        ("&lt;", "<"),
        ("&gt;", ">")
        ]

    #replace bad charecters in strings
    for tuple in formatting:
        question = question.replace(tuple[0], tuple[1])
        correct = correct.replace(tuple[0], tuple[1])
    #replace bad charecters in lists
    for tuple in formatting:
        wrong = [char.replace(tuple[0], tuple[1]) for char in wrong]

    #store local values globally
    parameters["question"].append(question)
    parameters["correct"].append(correct)

    all_answers = wrong + [correct]
    random.shuffle(all_answers)

    parameters["answer1"].append(all_answers[0])
    parameters["answer2"].append(all_answers[1])
    parameters["answer3"].append(all_answers[2])
    parameters["answer4"].append(all_answers[3])



#dictionary to store local pre-load parameters on a global level
parameters = {
    "question": [],
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "answer4": [],
    "correct": [],
    "score": [],
    "index": []
    }

#global dictionary of dynamically changing widgets
widgets = {
    "logo": [],
    "orig": [],
    "button": [],
    "score": [],
    "question": [],
    "question2": [],
    "button1": [],
    "opcion1": [],
    "opcion2": [],
    "opcion3": [],
    "opcion4": [],
    "opcion5": [],
    "opcion6": [],
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "answer4": [],
    "message": [],
    "message2": []
}

#initialliza grid layout
grid = QGridLayout()

def clear_widgets():
    ''' hide all existing widgets and erase
        them from the global dictionary'''
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

def clear_parameters():
    #clear the global dictionary of parameters
    for parm in parameters:
        if parameters[parm] != []:
            for i in range(0, len(parameters[parm])):
                parameters[parm].pop()
    #populate with initial index & score values
    parameters["index"].append(random.randint(0,49))
    parameters["score"].append(0)

def start_game():
    #start the game, reset all widgets and parameters
    clear_widgets()
    clear_parameters()
    preload_data(parameters["index"][-1])
    #display the game frame
    frame21()
    
def siguiente():
    #start the game, reset all widgets and parameters
    clear_widgets()
    clear_parameters()
    preload_data(parameters["index"][-1])
    #display the game frame
    frame31()

def opcion1():
    #start the game, reset all widgets and parameters
    clear_widgets()
    clear_parameters()
    preload_data(parameters["index"][-1])
    #display the game frame
    frameop1()

def opcion2():
    #start the game, reset all widgets and parameters
    clear_widgets()
    clear_parameters()
    preload_data(parameters["index"][-1])
    #display the game frame
    frameop2()

def opcion3():
    #start the game, reset all widgets and parameters
    clear_widgets()
    clear_parameters()
    preload_data(parameters["index"][-1])
    #display the game frame
    frameop3()

def opcion4():
    #start the game, reset all widgets and parameters
    clear_widgets()
    clear_parameters()
    preload_data(parameters["index"][-1])
    #display the game frame
    frameop4()

def opcion5():
    #start the game, reset all widgets and parameters
    clear_widgets()
    clear_parameters()
    preload_data(parameters["index"][-1])
    #display the game frame
    frameop5()

def create_buttons(answer, l_margin, r_margin):
    #create identical buttons with custom left & right margins
    button = QPushButton(answer)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(485)
    button.setStyleSheet(
        #setting variable margins
        "*{margin-left: " + str(l_margin) +"px;"+
        "margin-right: " + str(r_margin) +"px;"+
        '''
        border: 4px solid '#BC006C';
        color: white;
        font-family: 'shanti';
        font-size: 16px;
        border-radius: 25px;
        padding: 15px 0;
        margin-top: 20px;
        }
        *:hover{
            background: '#BC006C';
        }
        '''
    )
    button.clicked.connect()
    return button

def is_correct(btn):
    #a function to evaluate wether user answer is correct
    if btn.text() == parameters["correct"][-1]:
        # CORRECT ANSWER

        #update score (+10 points)
        temp_score = parameters["score"][-1]
        parameters["score"].pop()
        parameters["score"].append(temp_score + 10)

        #select a new random index and replace the old one
        parameters["index"].pop()
        parameters["index"].append(random.randint(0,49))
        #preload data for new index value
        preload_data(parameters["index"][-1])

        #update the text of all widgets with new data
        widgets["score"][-1].setText(str(parameters["score"][-1]))
        widgets["question"][0].setText(parameters["question"][-1])
        widgets["answer1"][0].setText(parameters["answer1"][-1])
        widgets["answer2"][0].setText(parameters["answer2"][-1])
        widgets["answer3"][0].setText(parameters["answer3"][-1])
        widgets["answer4"][0].setText(parameters["answer4"][-1])

        if parameters["score"][-1] == 100:
            # WON THE GAME
            clear_widgets()
            frame3()
    else:
        # WRONG ANSWER - LOST GAME
        clear_widgets()
        frame4()

#*********************************************
#                  FRAME 1
#*********************************************

def frame1():
    clear_widgets()
    #logo widget
    image = QPixmap("logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    widgets["logo"].append(logo)

    #button widget
    button = QPushButton("Comienza a crear")
    button.resize(400,400)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        '''
        *{
            border: 4px solid '#BC006C';
            border-radius: 45px;
            font-size: 35px;
            color: 'white';
            padding: 25px 0;
            margin: 100px 200px;
        }
        *:hover{
            background: '#BC006C';
        }
        '''
    )
    #button callback
    button.clicked.connect(start_game)
    widgets["button"].append(button)

    #place global widgets on the grid
    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 1, 0, 1, 2)

#*********************************************
#                  FRAME 2_1
#*********************************************
def cargarImagen():
    global filename
    filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
    return filename


def frame21():
    
    
    clear_widgets()
    #question widget
    question = QLabel("Selecciona la imagen que te gustaría procesar")
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        '''
        font-family: 'shanti';
        font-size: 25px;
        color: 'white';
        padding: 10px;
        '''
    )
    widgets["question"].append(question)
    
    #button widget
    button = QPushButton("Siguiente")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setGeometry(500, 150, 100, 40)
    button.adjustSize()
    button.setStyleSheet(
        '''
        *{
            border: 4px solid '#BC006C';
            border-radius: 45px;
            font-size: 35px;
            color: 'white';
            padding: 25px 70px;
            margin: 10px 50px;
        }
        *:hover{
            background: '#BC006C';
        }
        '''
    )
    #button callback
    widgets["button"].append(button)

    #button widget
    button1 = QPushButton("Siguiente")
    button1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    
    button1.setStyleSheet(
        '''
        *{
            border: 4px solid '#BC006C';
            border-radius: 45px;
            font-size: 35px;
            color: 'white';
            padding: 25px 70px;
            margin: 10px 50px;
        }
        *:hover{
            background: '#BC006C';
        }
        '''
    )
    
    #button callback    
    button.clicked.connect(siguiente)   
    filename=str(cargarImagen())
    widgets["button"].append(button)
    #logo widget
    image = QPixmap(filename)
    image2 = image.scaledToWidth(500)
    logo = QLabel()
    logo.setPixmap(image2)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 1px; margin-bottom: 1px;")
    widgets["logo"].append(logo)

    #place global widgets on the grid
    grid.addWidget(widgets["question"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["logo"][-1], 1, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 2, 0,1,2)
    

#*********************************************
#                  FRAME 31
#*********************************************

def frame31():

    #question widget
    question = QLabel("Selecciona el tipo de procesamiento que quieres realizar:")
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        '''
        font-family: 'shanti';
        font-size: 25px;
        color: 'white';
        padding: 1px;
        '''
    )
    widgets["question"].append(question)
    
    #button widget
    Bopcion1 = QPushButton("Ecualización")
    Bopcion1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    Bopcion1.setGeometry(500, 150, 100, 40)
    Bopcion1.adjustSize()
    Bopcion1.setStyleSheet(
        '''
        *{
            border: 4px solid '#BC006C';
            border-radius: 45px;
            font-size: 35px;
            color: 'white';
            padding: 25px 70px;
            margin: 10px 10px;
        }
        *:hover{
            background: '#BC006C';
        }
        '''
    )
    #button callback
    widgets["opcion1"].append(Bopcion1)
    
    #button widget
    Bopcion2 = QPushButton("Unsharped")
    Bopcion2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    Bopcion2.setGeometry(500, 150, 100, 40)
    Bopcion2.adjustSize()
    Bopcion2.setStyleSheet(
        '''
        *{
            border: 4px solid '#BC006C';
            border-radius: 45px;
            font-size: 35px;
            color: 'white';
            padding: 25px 25px;
            margin: 10px 10px;
        }
        *:hover{
            background: '#BC006C';
        }
        '''
    )
    #button callback
    widgets["opcion2"].append(Bopcion2)
    
    #button widget
    Bopcion3 = QPushButton("Filtro Difuso")
    Bopcion3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    Bopcion3.setGeometry(500, 150, 100, 40)
    Bopcion3.adjustSize()
    Bopcion3.setStyleSheet(
        '''
        *{
            border: 4px solid '#BC006C';
            border-radius: 45px;
            font-size: 35px;
            color: 'white';
            padding: 25px 25px;
            margin: 10px 10px;
        }
        *:hover{
            background: '#BC006C';
        }
        '''
    )
    #button callback
    widgets["opcion3"].append(Bopcion3)
    
    #button widget
    Bopcion4 = QPushButton("EMBH")
    Bopcion4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    Bopcion4.setGeometry(500, 150, 100, 40)
    Bopcion4.adjustSize()
    Bopcion4.setStyleSheet(
        '''
        *{
            border: 4px solid '#BC006C';
            border-radius: 45px;
            font-size: 35px;
            color: 'white';
            padding: 25px 25px;
            margin: 10px 10px;
        }
        *:hover{
            background: '#BC006C';
        }
        '''
    )
    #button callback
    widgets["opcion4"].append(Bopcion4)
    
    #button widget
    Bopcion5 = QPushButton("Combinar con arte")
    Bopcion5.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    Bopcion5.setGeometry(500, 150, 100, 40)
    Bopcion5.adjustSize()
    Bopcion5.setStyleSheet(
        '''
        *{
            border: 4px solid '#BC006C';
            border-radius: 45px;
            font-size: 35px;
            color: 'white';
            padding: 25px 25px;
            margin: 10px 50px;
        }
        *:hover{
            background: '#BC006C';
        }
        '''
    )
    #button callback
    widgets["opcion5"].append(Bopcion5)
    
    #button widget
    Bopcion6 = QPushButton("Escucha a Jupiter")
    Bopcion6.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    Bopcion6.setGeometry(500, 150, 100, 40)
    Bopcion6.adjustSize()
    Bopcion6.setStyleSheet(
        '''
        *{
            border: 4px solid '#BC006C';
            border-radius: 45px;
            font-size: 35px;
            color: 'white';
            padding: 25px 25px;
            margin: 10px 50px;
        }
        *:hover{
            background: '#BC006C';
        }
        '''
    )
    #button callback
    widgets["opcion6"].append(Bopcion6)
    
    #place global widgets on the grid
    grid.addWidget(widgets["question"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["opcion1"][-1], 1, 0) 
    grid.addWidget(widgets["opcion2"][-1], 1, 1)  
    grid.addWidget(widgets["opcion3"][-1], 2, 0) 
    grid.addWidget(widgets["opcion4"][-1], 2, 1)
    grid.addWidget(widgets["opcion5"][-1], 3, 0) 
    grid.addWidget(widgets["opcion6"][-1], 3, 1)
    
    Bopcion1.clicked.connect(opcion1) 
    Bopcion2.clicked.connect(opcion2) 
    Bopcion3.clicked.connect(opcion3) 
    Bopcion4.clicked.connect(opcion4) 
    Bopcion5.clicked.connect(opcion5) 

#*********************************************
#                  OPCION 1
#*********************************************

def frameop1():

    #question widget
    question = QLabel("Ecualización de histograma")
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        '''
        font-family: 'shanti';
        font-size: 25px;
        color: 'white';
        padding: 1px;
        '''
    )
    widgets["question"].append(question)
    salida = ec(filename)
    '''
    salida = ec(filename)
    qimage = ImageQt.ImageQt(salida).copy()
    pixmap = QtGui.QPixmap.fromImage(qimage)
    label = QtWidgets.QLabel()
    label.setPixmap(pixmap)
    '''
    '''
    Ah = salida.shape[0]
    w = salida.shape[1]
    ch = 3
    bytesPerLine = ch * w
    qImg = QImage(rgb_array.data, w, h, bytesPerLine, QImage.Format_RGB888)
    ''' 
    
    question2 = QLabel("Es un procesamiento que con base en el histograma de una imagen, \n realiza una transformación de los datos para \n obtener una representación de valores uniformes")
    question2.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question2.setStyleSheet(
        '''
        font-family: 'shanti';
        font-size: 15px;
        color: 'white';
        padding: 1px;
        '''
    )
    widgets["question2"].append(question2)
    salida = ec(filename)
    
    #logo widget
    image = QPixmap(filename)
    image2 = image.scaledToWidth(500)
    logo2 = QLabel()
    logo2.setPixmap(image2)
    logo2.setAlignment(QtCore.Qt.AlignCenter)
    logo2.setStyleSheet("margin-top: 10px;")
    widgets["orig"].append(logo2)
   
    #logo widget
    image = QPixmap("ec.jpg")
    image2 = image.scaledToWidth(500)
    logo = QLabel()
    logo.setPixmap(image2)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 10px;")
    widgets["logo"].append(logo)

    #place global widgets on the grid
    grid.addWidget(widgets["question"][-1], 0, 0)
    grid.addWidget(widgets["question2"][-1], 0, 1)
    grid.addWidget(widgets["orig"][-1], 1, 0)
    grid.addWidget(widgets["logo"][-1], 1, 1)

#*********************************************
#                  OPCION 2
#*********************************************

def frameop2():

    #question widget
    question = QLabel("Unsharped")
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        '''
        font-family: 'shanti';
        font-size: 25px;
        color: 'white';
        padding: 1px;
        '''
    )
    
    question2 = QLabel("Es un filtro que sirve para la mejora \n de nitidez en imagenes")
    question2.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question2.setStyleSheet(
        '''
        font-family: 'shanti';
        font-size: 15px;
        color: 'white';
        padding: 1px;
        '''
    )
    widgets["question2"].append(question2)
    salida = ec(filename)
    
    widgets["question"].append(question)
    salida = un(filename)
    '''
    salida = ec(filename)
    qimage = ImageQt.ImageQt(salida).copy()
    pixmap = QtGui.QPixmap.fromImage(qimage)
    label = QtWidgets.QLabel()
    label.setPixmap(pixmap)
    '''
    '''
    Ah = salida.shape[0]
    w = salida.shape[1]
    ch = 3
    bytesPerLine = ch * w
    qImg = QImage(rgb_array.data, w, h, bytesPerLine, QImage.Format_RGB888)
    ''' 
    #logo widget
    image = QPixmap(filename)
    image2 = image.scaledToWidth(500)
    logo2 = QLabel()
    logo2.setPixmap(image2)
    logo2.setAlignment(QtCore.Qt.AlignCenter)
    logo2.setStyleSheet("margin-top: 10px;")
    widgets["orig"].append(logo2)
   
    #logo widget
    image = QPixmap("un.jpg")
    image2 = image.scaledToWidth(500)
    logo = QLabel()
    logo.setPixmap(image2)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 10px;")
    widgets["logo"].append(logo)

    #place global widgets on the grid
    grid.addWidget(widgets["question"][-1], 0, 0)
    grid.addWidget(widgets["question2"][-1], 0, 1)
    grid.addWidget(widgets["orig"][-1], 1, 0)
    grid.addWidget(widgets["logo"][-1], 1, 1)

#*********************************************
#                  OPCION 3
#*********************************************

def frameop3():

    #question widget
    question = QLabel("Opcion3")
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        '''
        font-family: 'shanti';
        font-size: 25px;
        color: 'white';
        padding: 10px;
        '''
    )
    widgets["question"].append(question)

    #place global widgets on the grid
    grid.addWidget(widgets["question"][-1], 0, 0, 1, 2)
    
#*********************************************
#                  OPCION 4
#*********************************************

def frameop4():

    #question widget
    question = QLabel("Opcion4")
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        '''
        font-family: 'shanti';
        font-size: 25px;
        color: 'white';
        padding: 10px;
        '''
    )
    widgets["question"].append(question)

    #place global widgets on the grid
    grid.addWidget(widgets["question"][-1], 0, 0, 1, 2)

#*********************************************
#                  OPCION 5
#*********************************************

def frameop5():

    #question widget
    question = QLabel("Opcion5")
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        '''
        font-family: 'shanti';
        font-size: 25px;
        color: 'white';
        padding: 10px;
        '''
    )
    widgets["question"].append(question)

    #place global widgets on the grid
    grid.addWidget(widgets["question"][-1], 0, 0, 1, 2)
    
    
#*********************************************
#                  FRAME 2
#*********************************************

def frame2():
    #score widget
    score = QLabel(str(parameters["score"][-1]))
    score.setAlignment(QtCore.Qt.AlignRight)
    score.setStyleSheet(
        '''
        font-size: 35px;
        color: 'white';
        padding: 15px 10px;
        margin: 20px 200px;
        background: '#64A314';
        border: 1px solid '#64A314';
        border-radius: 35px;
        '''
    )
    widgets["score"].append(score)

    #question widget
    question = QLabel(parameters["question"][-1])
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        '''
        font-family: 'shanti';
        font-size: 25px;
        color: 'white';
        padding: 75px;
        '''
    )
    widgets["question"].append(question)

    #answer button widgets
    button1 = create_buttons(parameters["answer1"][-1], 85, 5)
    button2 = create_buttons(parameters["answer2"][-1], 5, 85)
    button3 = create_buttons(parameters["answer3"][-1], 85, 5)
    button4 = create_buttons(parameters["answer4"][-1], 5, 85)

    widgets["answer1"].append(button1)
    widgets["answer2"].append(button2)
    widgets["answer3"].append(button3)
    widgets["answer4"].append(button4)

    #logo widget
    image = QPixmap("logo_bottom.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 75px; margin-bottom: 30px;")
    widgets["logo"].append(logo)

    #place widget on the grid
    grid.addWidget(widgets["score"][-1], 0, 1)
    grid.addWidget(widgets["question"][-1], 1, 0, 1, 2)
    grid.addWidget(widgets["answer1"][-1], 2, 0)
    grid.addWidget(widgets["answer2"][-1], 2, 1)
    grid.addWidget(widgets["answer3"][-1], 3, 0)
    grid.addWidget(widgets["answer4"][-1], 3, 1)
    grid.addWidget(widgets["logo"][-1], 4, 0, 1,2)
    

#*********************************************
#             FRAME 3 - WIN GAME
#*********************************************

def frame3():
    #congradulations widget
    message = QLabel("Congradulations! You\nare a true programmer!\n your score is:")
    message.setAlignment(QtCore.Qt.AlignRight)
    message.setStyleSheet(
        "font-family: 'Shanti'; font-size: 25px; color: 'white'; margin: 100px 0px;"
        )
    widgets["message"].append(message)

    #score widget
    score = QLabel("100")
    score.setStyleSheet("font-size: 100px; color: #8FC740; margin: 0 75px 0px 75px;")
    widgets["score"].append(score)

    #go back to work widget
    message2 = QLabel("OK. Now go back to WORK.")
    message2.setAlignment(QtCore.Qt.AlignCenter)
    message2.setStyleSheet(
        "font-family: 'Shanti'; font-size: 30px; color: 'white'; margin-top:0px; margin-bottom:75px;"
        )
    widgets["message2"].append(message2)

    #button widget
    button = QPushButton('TRY AGAIN')
    button.setStyleSheet(
        "*{background:'#BC006C'; padding:25px 0px; border: 1px solid '#BC006C'; color: 'white'; font-family: 'Arial'; font-size: 25px; border-radius: 40px; margin: 10px 300px;} *:hover{background:'#ff1b9e';}"
        )
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.clicked.connect(frame1)

    widgets["button"].append(button)

    #logo widget
    pixmap = QPixmap('logo_bottom.png')
    logo = QLabel()
    logo.setPixmap(pixmap)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet(
        "padding :10px; margin-top:75px; margin-bottom: 20px;"
    )
    widgets["logo"].append(logo)

    #place widgets on the grid
    grid.addWidget(widgets["message"][-1], 2, 0)
    grid.addWidget(widgets["score"][-1], 2, 1)
    grid.addWidget(widgets["message2"][-1], 3, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 4, 0, 1, 2)
    grid.addWidget(widgets["logo"][-1], 5, 0, 2, 2)


#*********************************************
#                  FRAME 4 - FAIL
#*********************************************
def frame4():
    #sorry widget
    message = QLabel("Sorry, this answer \nwas wrong\n your score is:")
    message.setAlignment(QtCore.Qt.AlignRight)
    message.setStyleSheet(
        "font-family: 'Shanti'; font-size: 35px; color: 'white'; margin: 75px 5px; padding:20px;"
        )
    widgets["message"].append(message)

    #score widget
    score = QLabel(str(parameters["score"][-1]))
    score.setStyleSheet("font-size: 100px; color: white; margin: 0 75px 0px 75px;")
    widgets["score"].append(score)

    #button widget
    button = QPushButton('TRY AGAIN')
    button.setStyleSheet(
        '''*{
            padding: 25px 0px;
            background: '#BC006C';
            color: 'white';
            font-family: 'Arial';
            font-size: 35px;
            border-radius: 40px;
            margin: 10px 200px;
        }
        *:hover{
            background: '#ff1b9e';
        }'''
        )
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.clicked.connect(frame1)

    widgets["button"].append(button)

    #logo widget
    pixmap = QPixmap('logo_bottom.png')
    logo = QLabel()
    logo.setPixmap(pixmap)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet(
        "padding :10px; margin-top:75px;"
    )
    widgets["logo"].append(logo)

    #place widgets on the grid
    grid.addWidget(widgets["message"][-1], 1, 0)
    grid.addWidget(widgets["score"][-1], 1, 1)
    grid.addWidget(widgets["button"][-1], 2, 0, 1, 2)
    grid.addWidget(widgets["logo"][-1], 3, 0, 1, 2)