# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddEditCoffeeForm(object):
    def setupUi(self, AddEditCoffeeForm):
        AddEditCoffeeForm.setObjectName("AddEditCoffeeForm")
        AddEditCoffeeForm.resize(642, 254)
        self.verticalLayout = QtWidgets.QVBoxLayout(AddEditCoffeeForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(AddEditCoffeeForm)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.title_input = QtWidgets.QLineEdit(AddEditCoffeeForm)
        self.title_input.setObjectName("title_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.title_input)
        self.label_2 = QtWidgets.QLabel(AddEditCoffeeForm)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.degree_of_roasting_input = QtWidgets.QLineEdit(AddEditCoffeeForm)
        self.degree_of_roasting_input.setObjectName("degree_of_roasting_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.degree_of_roasting_input)
        self.label_3 = QtWidgets.QLabel(AddEditCoffeeForm)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.beans_select = QtWidgets.QComboBox(AddEditCoffeeForm)
        self.beans_select.setObjectName("beans_select")
        self.beans_select.addItem("")
        self.beans_select.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.beans_select)
        self.label_4 = QtWidgets.QLabel(AddEditCoffeeForm)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.taste_description_input = QtWidgets.QLineEdit(AddEditCoffeeForm)
        self.taste_description_input.setObjectName("taste_description_input")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.taste_description_input)
        self.label_5 = QtWidgets.QLabel(AddEditCoffeeForm)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(AddEditCoffeeForm)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.price_input = QtWidgets.QSpinBox(AddEditCoffeeForm)
        self.price_input.setMaximum(10000)
        self.price_input.setObjectName("price_input")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.price_input)
        self.volume_input = QtWidgets.QSpinBox(AddEditCoffeeForm)
        self.volume_input.setMinimum(1)
        self.volume_input.setMaximum(10000)
        self.volume_input.setObjectName("volume_input")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.volume_input)
        self.verticalLayout.addLayout(self.formLayout)
        self.save_btn = QtWidgets.QPushButton(AddEditCoffeeForm)
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout.addWidget(self.save_btn)

        self.retranslateUi(AddEditCoffeeForm)
        QtCore.QMetaObject.connectSlotsByName(AddEditCoffeeForm)

    def retranslateUi(self, AddEditCoffeeForm):
        _translate = QtCore.QCoreApplication.translate
        AddEditCoffeeForm.setWindowTitle(_translate("AddEditCoffeeForm", "Добавление/Редактирование"))
        self.label.setText(_translate("AddEditCoffeeForm", "Название сорта"))
        self.label_2.setText(_translate("AddEditCoffeeForm", "Степень обжарки"))
        self.label_3.setText(_translate("AddEditCoffeeForm", "Молотый/в зернах:"))
        self.beans_select.setItemText(0, _translate("AddEditCoffeeForm", "Молотый"))
        self.beans_select.setItemText(1, _translate("AddEditCoffeeForm", "В зернах"))
        self.label_4.setText(_translate("AddEditCoffeeForm", "Описание вкуса"))
        self.label_5.setText(_translate("AddEditCoffeeForm", "Цена"))
        self.label_6.setText(_translate("AddEditCoffeeForm", "Объем упаковки"))
        self.save_btn.setText(_translate("AddEditCoffeeForm", "Сохранить"))
