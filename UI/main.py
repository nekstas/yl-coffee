# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout.addWidget(self.add_btn)
        self.edit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_btn.setObjectName("edit_btn")
        self.horizontalLayout.addWidget(self.edit_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setObjectName("table")
        self.table.setColumnCount(7)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        self.verticalLayout.addWidget(self.table)
        Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Капучино"))
        self.add_btn.setText(_translate("Window", "Добавить запись"))
        self.edit_btn.setText(_translate("Window", "Редактировать запись"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Window", "ID"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Window", "Название сорта"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("Window", "Степень обжарки"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("Window", "Молотый/в зернах"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("Window", "Описание вкуса"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("Window", "Цена"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("Window", "Объем упаковки"))
