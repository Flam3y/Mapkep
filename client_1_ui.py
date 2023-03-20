# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 140)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 559, 120))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Connect = QtWidgets.QPushButton(self.widget)
        self.Connect.setObjectName("Connect")
        self.gridLayout.addWidget(self.Connect, 2, 0, 1, 3)
        self.Ip = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Ip.setFont(font)
        self.Ip.setObjectName("Ip")
        self.gridLayout.addWidget(self.Ip, 1, 2, 1, 1)
        self.Name = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.gridLayout.addWidget(self.Name, 0, 1, 1, 1)
        self.Guide = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Guide.setFont(font)
        self.Guide.setObjectName("Guide")
        self.gridLayout.addWidget(self.Guide, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Маркер"))
        self.Connect.setText(_translate("MainWindow", "Подключиться"))
        self.Ip.setText(_translate("MainWindow", "localhost 6666"))
        self.Name.setText(_translate("MainWindow", "Маркер"))
        self.Guide.setText(_translate("MainWindow", "Введите IP и порт для подключения (через пробел)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

