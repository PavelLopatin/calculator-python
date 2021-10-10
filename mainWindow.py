import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot

import calculator
import design


class MainWindow(design.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.res = ''
        self.memory = ['0']
        self.previous_resutl = []
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_0_clicked(self):
        self.res += '0'
        self.result.setText(self.res)

    @pyqtSlot()
    def on_pushButton_1_clicked(self):
        self.res += '1'
        self.result.setText(self.res)

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        self.res += '2'
        self.result.setText(self.res)

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        self.res += '3'
        self.result.setText(self.res)

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        self.res += '4'
        self.result.setText(self.res)

    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        self.res += '5'
        self.result.setText(self.res)

    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        self.res += '6'
        self.result.setText(self.res)

    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        self.res += '7'
        self.result.setText(self.res)

    @pyqtSlot()
    def on_pushButton_8_clicked(self):
        self.res += '8'
        self.result.setText(self.res)

    @pyqtSlot()
    def on_pushButton_9_clicked(self):
        self.res += '9'
        self.result.setText(self.res)

    @pyqtSlot()
    def on_pushButton_Del_clicked(self):
        self.res = self.res[:-1]
        self.result.setText(self.res)

    @pyqtSlot()
    def on_pushButton_Del_2_clicked(self):
        self.res = ""
        self.result.setText(self.res)

    @pyqtSlot()
    def on_pushButton_delenie_clicked(self):
        self.res += '/'
        self.result.setText(self.res)

    @pyqtSlot()
    def on_pushButton_minus_clicked(self):
        self.res += '-'
        self.result.setText(self.res)

    @pyqtSlot()
    def on_pushButton_ravno_clicked(self):
        try:
            for i in '+-*/()':
                if i in self.res:
                    self.previous_resutl.append(self.res)
                    self.res = calculator.calculator(self.res)
                    self.res = f"{self.res:.{3}f}"
                    self.res = self.res.rstrip('0')
                    self.res = self.res.rstrip('.')
                    self.previous_resutl.append(self.res)
                    self.listWidget.addItem(f'{self.previous_resutl[-2]}={self.previous_resutl[-1]}')
                    self.result.setText(self.res)
        except:
            self.result.setText('Ошибка')
            self.res = ''

    @pyqtSlot()
    def on_pushButton_skobka1_clicked(self):
        self.res += '('
        self.result.setText(self.res)

    @pyqtSlot()
    def on_pushButton_skobka2_clicked(self):
        self.res += ')'
        self.result.setText(self.res)

    @pyqtSlot()
    def on_pushButton_sum_clicked(self):
        self.res += '+'
        self.result.setText(self.res)

    @pyqtSlot()
    def on_pushButton_umn_clicked(self):
        self.res += '*'
        self.result.setText(self.res)

    @pyqtSlot()
    def on_pushButton_float_clicked(self):
        self.res += '.'
        self.result.setText(self.res)

    @pyqtSlot()
    def on_pushButton_Clear_Memory_clicked(self):
        if self.memory != ['0']:
            self.memory = ['0']

    @pyqtSlot()
    def on_pushButton_add_memory_clicked(self):
        self.memory.append(self.res)

    @pyqtSlot()
    def on_pushButton_memory_call_clicked(self):
        self.res = ''
        self.memory[-1] = f"{float(self.memory[-1]):.{3}f}"
        self.memory[-1] = self.memory[-1].rstrip('0')
        self.memory[-1] = self.memory[-1].rstrip('.')
        self.res = self.memory[-1]
        self.result.setText(self.res)

    @pyqtSlot()
    def on_pushButton_sub_memory_clicked(self):
        self.res = calculator.to_tokens(self.res)
        if self.res[0] == '-':
            self.res = self.res[1]
            memory = calculator.calculator(f"{self.memory[-1]}+{self.res}")
        else:
            self.res = self.res[0]
            memory = calculator.calculator(f"{self.memory[-1]}-{self.res}")
        self.memory[-1] = memory[0]

    @pyqtSlot()
    def on_pushButton_sum_memory_clicked(self):
        self.res = calculator.to_tokens(self.res)
        if self.res[0] == '-':
            self.res = self.res[1]
            memory = calculator.calculator(f"{self.memory[-1]}-{self.res}")
        else:
            self.res = self.res[0]
            memory = calculator.calculator(f"{self.memory[-1]}+{self.res}")
        self.memory[-1] = memory[0]

    def on_listWidget_clicked(self):
        text = self.listWidget.currentItem().text()
        for i in text:
            if i != '=':
                text = text[1:]
            else:
                text = text[1:]
                break
        self.res = text
        self.result.setText(text)


main_window = QtWidgets.QApplication(sys.argv)
calc = MainWindow()
calc.show()
main_window.exec_()
