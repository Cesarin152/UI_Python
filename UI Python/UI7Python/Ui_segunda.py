# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\cesar\OneDrive\Documentos\Interfaz Grafica\UI7Python\segunda.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_segunda(object):
    def setupUi(self, segunda):
        segunda.setObjectName("segunda")
        segunda.resize(427, 361)
        self.centralwidget = QtWidgets.QWidget(segunda)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 40, 91, 51))
        self.label.setObjectName("label")
        segunda.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(segunda)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 427, 21))
        self.menubar.setObjectName("menubar")
        segunda.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(segunda)
        self.statusbar.setObjectName("statusbar")
        segunda.setStatusBar(self.statusbar)

        self.retranslateUi(segunda)
        QtCore.QMetaObject.connectSlotsByName(segunda)

    def retranslateUi(self, segunda):
        _translate = QtCore.QCoreApplication.translate
        segunda.setWindowTitle(_translate("segunda", "MainWindow"))
        self.label.setText(_translate("segunda", "Segunda Ventana"))
