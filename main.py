from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout, QPushButton
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt
from random import randint 


class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pushButton = QPushButton(self)
        self.pushButton.move(5, 5)
        self.pushButton.setText('Рисовать')
        self.pushButton.clicked.connect(self.circle)
        self.setGeometry(300, 300, 300, 300)
        self.label = QLabel(self)
        self.label.move(5, 50)
        self.label.resize(250, 200)
        canvas = QPixmap(290, 200)
        self.label.setPixmap(canvas)        

    def circle(self):
        x, y = [randint(1, 200) for i in range(2)]
        w, h = [randint(1, 200) for i in range(2)]        
        painter = QPainter(self.label.pixmap())  
        painter.setBrush(QColor(*[randint(0, 255) for i in range(3)]))
        painter.drawEllipse(x, y, w, h)
        painter.end()
        self.update()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())
