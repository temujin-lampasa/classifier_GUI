from PyQt5 import QtGui, QtWidgets

class paintWidget(QtWidgets.QLabel):
    
    def __init__(self, *args, **kwargs):
        super(paintWidget, self).__init__(*args, **kwargs)
        self.height = 200
        self.width = 200

        self.setPixmap(QtGui.QPixmap(self.height, self.width))
        self.pixmap().fill(QtGui.QColor('white'))
        self.pen = QtGui.QPen()
        self.pen.setWidth(5)

        self.last_x = None
        self.last_y = None
    
    def mouseMoveEvent(self, e):
        if not self.last_x:
            self.last_x = e.x()
            self.last_y = e.y()
        
        painter = QtGui.QPainter(self.pixmap())
        painter.setPen(self.pen)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        self.last_x = e.x()
        self.last_y = e.y()
    
    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None
