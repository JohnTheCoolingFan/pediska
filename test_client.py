#! /usr/bin/python3

from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('clientui/main.ui', self)
        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.button.clicked.connect(self.printButtonPressed)

        self.show()

    def printButtonPressed(self):
        # This is executed when the button is pressed
        print('printButtonPressed')
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
