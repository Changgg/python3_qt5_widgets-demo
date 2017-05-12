import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5 import QtGui, QtPrintSupport, QtWidgets

"""
QComboBox 组件演示
"""


class Example(QtWidgets.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel("Ubuntu", self)

        self.combo = combo = QtWidgets.QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Red Hat")
        combo.addItem("Gentoo")

        combo.move(50, 50)
        self.label.move(50, 150)
        combo.activated.connect(self.onActivated)

        self.setGeometry(250, 200, 350, 250)
        self.setWindowTitle('QComboBox')

    def onActivated(self, index, *args, **kwargs):  # PyQt4 是直接传所属项的文本内容，PyQt5 是索引
        self.label.setText(self.combo.itemText(index))
        self.label.adjustSize()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
