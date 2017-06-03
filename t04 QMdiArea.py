import sys
from PyQt5 import QtWidgets, QtGui, QtCore

_translate = QtCore.QCoreApplication.translate
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QMainWindow()
    window.resize(800, 600)
    window.setWindowTitle(_translate("MainWindow", "My Mdi Window"))

    area = QtWidgets.QMdiArea()

    for i in range(9):
        subWindow = QtWidgets.QMdiSubWindow()
        subWindow.resize(300, 400)

        # subWindow.setFixedSize(200,100)
        area.addSubWindow(subWindow)


    area.tileSubWindows()
    area.cascadeSubWindows()

    window.setCentralWidget(area)
    window.show()

    sys.exit(app.exec_())
