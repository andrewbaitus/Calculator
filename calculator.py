from PyQt5 import QtWidgets, QtCore, QtGui
from calcUI import Ui_MainWindow
import sys
import calcUI
import random

class myWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #бъявление переменных для хранения дополнительных данных
        self.number_a = 0.0
        self.number_b = 0.0
        self.number_c = 0.0
        self.oper = str()
        self.isclear = True #True - очищаем, False - не очищаем
        #создание обработчика событий для цифровых кнопок
        self.ui.btn1.clicked.connect(self.btn_number_click)
        self.ui.btn2.clicked.connect(self.btn_number_click)
        self.ui.btn3.clicked.connect(self.btn_number_click)
        self.ui.btn4.clicked.connect(self.btn_number_click)
        self.ui.btn5.clicked.connect(self.btn_number_click)
        self.ui.btn6.clicked.connect(self.btn_number_click)
        self.ui.btn7.clicked.connect(self.btn_number_click)
        self.ui.btn8.clicked.connect(self.btn_number_click)
        self.ui.btn9.clicked.connect(self.btn_number_click)
        self.ui.btn0.clicked.connect(self.btn_number_click)
        #создаем обработчик событий для кнопок арифметических действий
        self.ui.btn_plus.clicked.connect(self.btn_arifmetic_click)
        self.ui.btn_min.clicked.connect(self.btn_arifmetic_click)
        self.ui.btn_umnoz.clicked.connect(self.btn_arifmetic_click)
        self.ui.btn_del.clicked.connect(self.btn_arifmetic_click)
        self.ui.btn_pow.clicked.connect(self.btn_arifmetic_click)
        #создаем обработчик событий для кнопки =
        self.ui.btn_answer.clicked.connect(self.btn_answer_click)
        #создаем обработчик событий для кнопки clear
        self.ui.btn_clear.clicked.connect(self.btn_clear_click)
        #создаем обработчик событий для кнопки backspace
        self.ui.btn_backspace.clicked.connect(self.btn_backspace_click)
        #создаем обработчик событий для кнопки dot
        self.ui.btn_dot.clicked.connect(self.btn_dot_click)
        #создаем обработчик событий для кнопки sqrt
        self.ui.btn_sqrt.clicked.connect(self.btn_sqrt_click)

    def btn_number_click(self):
        btn = self.sender()
        if self.isclear == True:
            self.ui.input_number.setText("")
            self.isclear = False
        number = self.ui.input_number.text() + btn.text()
        self.ui.input_number.setText(number)

    def btn_arifmetic_click(self):
        btn = self.sender()
        self.oper = btn.text()
        self.isclear = True
        self.number_a = float(self.ui.input_number.text())

    def btn_answer_click(self):
        self.number_b = float(self.ui.input_number.text())
        if self.oper == "+":
            self.number_c = self.number_a + self.number_b
        elif self.oper == "-":
            self.number_c = self.number_a - self.number_b
        elif self.oper == "*":
            self.number_c = self.number_a * self.number_b
        elif self.oper == "/":
            if self.number_b == 0:
                self.number_c = 0
            else:
                self.number_c = self.number_a / self.number_b
        elif self.oper == "^":
            self.number_c = self.number_a ** self.number_b
        self.ui.input_number.setText(str(self.number_c))
        self.isclear = True
        
    def btn_clear_click(self):
        self.isclear = True
        self.number_a = 0
        self.number_b = 0
        self.number_c = 0
        self.oper = ""
        self.ui.input_number.setText("0")

    def btn_backspace_click(self):
        number = self.ui.input_number.text()
        if len(number) > 1:
            number = number[0: len(number)-1]
        else:
            number = "0"
            self.isclear = True
        self.ui.input_number.setText(number)

    def btn_dot_click(self):
        number = self.ui.input_number.text()
        if number.find(".") == -1:
            number += "."
            self.ui.input_number.setText(number)

    def btn_sqrt_click(self):
        self.number_a = float(self.ui.input_number.text())
        if self.number_a > 0:
            self.number_c = self.number_a ** (1/2)
        else:
            self.number_c = 0
        self.ui.input_number.setText(str(self.number_c))
        self.isclear = True
        

app = QtWidgets.QApplication([])
application = myWindow()
application.show()
sys.exit(app.exec())







