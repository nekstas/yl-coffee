# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem


class Window(QMainWindow):
    table: QTableWidget
    conn: sqlite3.Connection

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.program_init()

    def program_init(self):
        self.conn = sqlite3.connect('coffee.sqlite')
        self.update_table()

    def update_table(self):
        cur = self.conn.cursor()
        result = cur.execute(f'SELECT * FROM coffee;').fetchall()
        result = [*map(
            lambda x: x[:3] + ('В зернах' if x[3] else 'Молотый', ) + x[4:],
            result
        )]
        self.table.setRowCount(len(result))

        for i, row in enumerate(result):
            for j, column in enumerate(row):
                item = QTableWidgetItem(str(column))
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                self.table.setItem(i, j, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
