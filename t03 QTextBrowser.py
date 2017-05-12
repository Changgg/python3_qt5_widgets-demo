import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *

if __name__ == '__main__':
    class Form(QtWidgets.QDialog):
        def __init__(self):
            super(Form, self).__init__()

            self.browser = QtWidgets.QTextBrowser()
            self.lineedit = QtWidgets.QLineEdit('Type an expression')
            self.lineedit.selectAll()

            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(self.browser)
            layout.addWidget(self.lineedit)

            self.setLayout(layout)
            self.lineedit.setFocus()
            self.setWindowTitle('title')


    app = QtWidgets.QApplication(sys.argv)

    form = Form()
    form.browser.append('<div><h1 style="color:green">test</h1></div>')
    form.browser.append('<div><h1>test</h1></div>')
    form.show()

    sys.exit(app.exec())
