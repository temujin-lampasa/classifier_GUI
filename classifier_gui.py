import sys
from PyQt5 import QtWidgets, QtGui
from mainwindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.clear_btn.clicked.connect(self.clear_drawing)
    
    def clear_drawing(self):
        self.drawing.pixmap().fill(QtGui.QColor('white'))
        self.drawing.update()

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()