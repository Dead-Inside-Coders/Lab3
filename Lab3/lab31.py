from PyQt5 import QtWidgets
from Method import Ui_MainWindow
import sys
 
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setRowCount(4)
 
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())

from PyQt5.QtWidgets import QTableWidgetItem
 
from qtable import *
import sys
 
data = []
data.append(('Вес первой переменной', q1))
data.append(('Вес второй переменной', q2'))
data.append(('Вес третьей переменной',q3))
 
 
class mywindow(QtWidgets.QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
 
        self.ui.setupUi(self)
        self.ui.tableWidget.setRowCount(3)
        self.ui.tableWidget.setColumnCount(2)
 
        # очистка таблицы при клике на кнопку.
        self.ui.pushButton.clicked.connect(self.clear)
 
        row = 0
        for tup in data:
            col = 0
 
            for item in tup:
                cellinfo = QTableWidgetItem(item)
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
 
            row += 1
 
    def clear(self):
        self.ui.tableWidget.clear()
 
 
app = QtWidgets.QApplication([])
win = mywindow()
win.show()
 
sys.exit(app.exec())
from scipy.optimize import linprog 
c = [q1*(-30),q2*(-1),q3*6] #Функция целей, ранжированая по важности
A_ub = [[90,5]] #'1' 
b_ub = [10000]#'1' 
A_eq = [[3,-1]] #'2' 
b_eq = [0] #'2' 
print (linprog(c, A_ub, b_ub, A_eq, b_eq)) 