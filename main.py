# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from __future__ import annotations
import sqlite3
import sys
from typing import Optional

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, \
    QWidget, QPushButton, QLineEdit, QSpinBox, QComboBox


class AddEditCoffeeForm(QWidget):
    title_input: QLineEdit
    degree_of_roasting_input: QLineEdit
    beans_select: QComboBox
    taste_description_input: QLineEdit
    price_input: QSpinBox
    volume_input: QSpinBox
    save_btn: QPushButton

    cid: int
    parent: Window

    def __init__(self, parent, data):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.form_init(parent, data)

    def form_init(self, parent, data):
        self.parent = parent
        self.cid = int(data[0])
        self.save_btn.clicked.connect(self.on_save)
        self.title_input.setText(data[1])
        self.degree_of_roasting_input.setText(data[2])
        self.beans_select.setCurrentIndex(int(data[3] == 'В зернах'))
        self.taste_description_input.setText(data[4])
        self.price_input.setValue(int(data[5]))
        self.volume_input.setValue(int(data[6]))

    def on_save(self):
        print((
            self.title_input.text(),
            self.degree_of_roasting_input.text(),
            bool(self.beans_select.currentIndex()),
            self.taste_description_input.text(),
            self.price_input.value(),
            self.volume_input.value()
        ))
        self.parent.on_save(self.cid, (
            self.title_input.text(),
            self.degree_of_roasting_input.text(),
            bool(self.beans_select.currentIndex()),
            self.taste_description_input.text(),
            self.price_input.value(),
            self.volume_input.value()
        ))
        self.close()


class Window(QMainWindow):
    table: QTableWidget
    add_btn: QPushButton
    edit_btn: QPushButton
    form: Optional[AddEditCoffeeForm]
    conn: sqlite3.Connection

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.program_init()

    def program_init(self):
        self.form = None
        self.conn = sqlite3.connect('coffee.sqlite')
        self.add_btn.clicked.connect(self.add)
        self.edit_btn.clicked.connect(self.edit)
        self.update_table()

    def add(self):
        self.form = AddEditCoffeeForm(self, (
            -1, '', '', '', '', 0, 1
        ))
        self.form.show()

    def edit(self):
        rows = self.table.selectedItems()
        if not rows:
            return
        row = rows[0].row()

        self.form = AddEditCoffeeForm(self, (
            self.table.item(row, 0).text(), self.table.item(row, 1).text(),
            self.table.item(row, 2).text(), self.table.item(row, 3).text(),
            self.table.item(row, 4).text(), self.table.item(row, 5).text(),
            self.table.item(row, 6).text()
        ))
        self.form.show()

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

    def on_save(self, cid, obj):
        cur = self.conn.cursor()

        if cid == -1:
            cur.execute(
                '''INSERT INTO coffee 
(title, degree_of_roasting, beans, taste_description, price, volume)
VALUES (?, ?, ?, ?, ?, ?)''',
                obj
            )
        else:
            cur.execute(
                '''UPDATE coffee SET
title=?, degree_of_roasting=?, beans=?, taste_description=?, price=?, volume=?
WHERE id=?''',
                (*obj, cid)
            )

        self.conn.commit()
        self.update_table()

    def closeEvent(self, _):
        self.conn.close()
        if self.form is not None:
            self.form.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
