import sys

from random import random
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QColor, QPainter
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(527, 422)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 83, 22))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Button"))


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
            qp.setBrush(QColor(int(255 * random()), int(255 * random()), int(255 * random())))
            a = int(250 * random())
            qp.drawEllipse(int(527 * random()), int(422 * random()), a, a)
        else:
            self.b = True



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
