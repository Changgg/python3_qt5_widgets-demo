import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5 import QtGui, QtPrintSupport, QtWidgets

"""
QSplitter 组件演示
"""


class Example(QtWidgets.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.ui_init()

    def ui_init(self):
        hbox = QtWidgets.QHBoxLayout(self)

        topleft = QtWidgets.QFrame(self)
        topleft.setMinimumWidth(75)
        topleft.setMaximumWidth(75)  # 最大宽度
        topleft.setMinimumHeight(100)
        topleft.setFrameShape(QtWidgets.QFrame.StyledPanel)

        topmid = QtWidgets.QFrame(self)
        topmid.setMinimumWidth(200)
        topmid.setMaximumWidth(250)
        topmid.setFrameShape(QtWidgets.QFrame.StyledPanel)

        topright = QtWidgets.QFrame(self)
        topright.setMinimumWidth(400)
        topright.setMaximumWidth(500)
        topright.setFrameShape(QtWidgets.QFrame.StyledPanel)

        splitter1 = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topmid)
        splitter1.addWidget(topright)
        splitter1.setMinimumHeight(200)

        bottom = QtWidgets.QFrame(self)
        bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)

        splitter2 = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setWindowTitle('QSplitter PyQt5 Python3 组件演示')

        QtWidgets.QApplication.setStyle(
            QtWidgets.QStyleFactory.create('Cleanlooks')
        )  # 使用 Cleanlooks 样式。 在某些样式中，框架是不可见的。

        self.setGeometry(250, 200, 700, 500)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
