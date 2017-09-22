# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PrimeiraWindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(732, 600)
        MainWindow.setMinimumSize(QtCore.QSize(732, 600))
        MainWindow.setMaximumSize(QtCore.QSize(732, 600))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_cad_cliente = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cad_cliente.setGeometry(QtCore.QRect(10, 10, 111, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_cad_cliente.setFont(font)
        self.btn_cad_cliente.setDefault(False)
        self.btn_cad_cliente.setFlat(False)
        self.btn_cad_cliente.setObjectName("btn_cad_cliente")
        self.btn_reg_consulta = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reg_consulta.setGeometry(QtCore.QRect(130, 10, 111, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.btn_reg_consulta.setFont(font)
        self.btn_reg_consulta.setObjectName("btn_reg_consulta")
        self.btn_cad_dentista = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cad_dentista.setGeometry(QtCore.QRect(250, 10, 111, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.btn_cad_dentista.setFont(font)
        self.btn_cad_dentista.setObjectName("btn_cad_dentista")
        self.btn_bus_cliente = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bus_cliente.setGeometry(QtCore.QRect(370, 10, 111, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.btn_bus_cliente.setFont(font)
        self.btn_bus_cliente.setObjectName("btn_bus_cliente")
        self.btn_bus_consulta = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bus_consulta.setGeometry(QtCore.QRect(490, 10, 111, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.btn_bus_consulta.setFont(font)
        self.btn_bus_consulta.setObjectName("btn_bus_consulta")
        self.btn_bus_dentista = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bus_dentista.setGeometry(QtCore.QRect(610, 10, 111, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.btn_bus_dentista.setFont(font)
        self.btn_bus_dentista.setObjectName("btn_bus_dentista")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 100, 471, 471))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Views/src/logo_main.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema Dentista"))
        self.btn_cad_cliente.setText(_translate("MainWindow", "Cadastrar \n"
"Cliente"))
        self.btn_reg_consulta.setText(_translate("MainWindow", "Registrar\n"
"Consulta"))
        self.btn_cad_dentista.setText(_translate("MainWindow", "Cadastrar\n"
"Dentista"))
        self.btn_bus_cliente.setText(_translate("MainWindow", "Buscar\n"
"Cliente"))
        self.btn_bus_consulta.setText(_translate("MainWindow", "Buscar\n"
"Consulta"))
        self.btn_bus_dentista.setText(_translate("MainWindow", "Buscar\n"
"Dentista"))

