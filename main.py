import sys

import sqlite3
from UI import main, edit
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import QtWidgets


class Form(QtWidgets.QWidget, edit.Ui_Form):
    def __init__(self, parent, arg=None):
        super().__init__()
        if arg is None:
            arg = [-1] + [''] * 6
        self.setupUi(self)
        self.id = arg[0]
        self.initUI(arg)
        self.parent = parent

    def initUI(self, arg):
        self.lineEdit_2.setText(arg[1])
        self.lineEdit_3.setText(arg[2])
        self.lineEdit_4.setText(arg[3])
        self.lineEdit_5.setText(arg[4])
        self.lineEdit_6.setText(arg[5])
        self.lineEdit_7.setText(arg[6])
        self.pushButton.clicked.connect(self.cancel)
        self.pushButton_2.clicked.connect(self.ok)

    def cancel(self):
        self.parent.initUI()
        self.close()

    def ok(self):
        con = sqlite3.connect('data/coffee.sqlite')
        con.commit()
        con.cursor().execute(f'Delete from coffee\n'
                             f'where id = ' + str(self.id))
        a, b = "'id'," * (self.id != -1), f"{self.id}," * (self.id != -1),
        con.cursor().execute(f"INSERT INTO coffee({a} 'sort', 'degree of"
                             f" roast', 'ground','taste', 'price', '"
                             f"packing volume') VALUES("
                             f"{b}"
                             f"'{self.lineEdit_2.text()}',"
                             f"'{self.lineEdit_3.text()}',"
                             f"'{self.lineEdit_4.text()}',"
                             f"'{self.lineEdit_5.text()}',"
                             f"'{self.lineEdit_6.text()}',"
                             f"'{self.lineEdit_7.text()}')")
        con.commit()
        self.parent.initUI()
        self.close()


class MyWidget(QMainWindow, main.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.f = None

    def initUI(self):
        self.tableWidget.setRowCount(0)
        self.e = True
        self.setFixedSize(614, 481)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.itemDoubleClicked.connect(self.edit)
        self.pushButton.clicked.connect(self.crt)
        coffee = sqlite3.connect('data/coffee.sqlite').cursor().execute('Select * '
                                                                        'from coffee').fetchall()
        self.tableWidget.setColumnCount(7)
        for i, row in enumerate(coffee):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.setHorizontalHeaderLabels(['id', 'sort', 'degree of roast', 'ground',
                                                    'taste', 'price', 'packing volume'])

    def edit(self):
        if self.e:
            a = []
            for i in range(7):
                a.append(self.tableWidget.item(self.tableWidget.currentRow(), i).text())
            self.f = Form(self, a)
            self.f.show()
            self.e = False

    def crt(self):
        if self.e:
            self.f = Form(self)
            self.f.show()
            self.e = False

    def no(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
