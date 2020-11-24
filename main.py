import sys

from random import random
from PyQt5.QtGui import QColor, QPainter
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.b = False
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.paint)


    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()


    def paint(self):
        self.repaint()


    def draw_flag(self, qp):
        if self.b:
            qp.setBrush(QColor(255, 255, 0))
            a = 200 * random()
            qp.drawEllipse(int(527 * random()), int(422 * random()), a, a)
        else:
            self.b = True



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
