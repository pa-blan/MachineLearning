# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt\ml.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_machinelearning(object):
    def setupUi(self, machinelearning):
        machinelearning.setObjectName("machinelearning")
        machinelearning.resize(867, 666)
        self.centralwidget = QtWidgets.QWidget(machinelearning)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("E+H Serif")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.bild = QtWidgets.QLabel(self.centralwidget)
        self.bild.setObjectName("bild")
        self.verticalLayout.addWidget(self.bild)
        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setObjectName("text")
        self.verticalLayout.addWidget(self.text)
        self.aufnehmen = QtWidgets.QPushButton(self.centralwidget)
        self.aufnehmen.setObjectName("aufnehmen")
        self.verticalLayout.addWidget(self.aufnehmen)
        self.einlernen = QtWidgets.QPushButton(self.centralwidget)
        self.einlernen.setObjectName("einlernen")
        self.verticalLayout.addWidget(self.einlernen)
        self.testen = QtWidgets.QPushButton(self.centralwidget)
        self.testen.setObjectName("testen")
        self.verticalLayout.addWidget(self.testen)
        machinelearning.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(machinelearning)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 867, 31))
        self.menubar.setObjectName("menubar")
        machinelearning.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(machinelearning)
        self.statusbar.setObjectName("statusbar")
        machinelearning.setStatusBar(self.statusbar)

        self.retranslateUi(machinelearning)
        QtCore.QMetaObject.connectSlotsByName(machinelearning)

    def retranslateUi(self, machinelearning):
        _translate = QtCore.QCoreApplication.translate
        machinelearning.setWindowTitle(_translate("machinelearning", "MainWindow"))
        self.label.setText(_translate("machinelearning", "machine learning"))
        self.bild.setText(_translate("machinelearning", "TextLabel"))
        self.text.setText(_translate("machinelearning", "TextLabel"))
        self.aufnehmen.setText(_translate("machinelearning", "Aufnehmen"))
        self.einlernen.setText(_translate("machinelearning", "Einlernen"))
        self.testen.setText(_translate("machinelearning", "Testen"))

