import sys

import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import QtWidgets


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.itemDoubleClicked.connect(self.edit)
        coffee = sqlite3.connect('coffee.sqlite').cursor().execute('Select * from coffee').fetchall()
        self.tableWidget.setColumnCount(7)
        for i, row in enumerate(coffee):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.setHorizontalHeaderLabels(['id', 'sort', 'degree of roast', 'ground',
                                                    'taste', 'price', 'packing volume'])

    def edit(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
