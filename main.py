import sys
from random import randint
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor
from PyQt6.uic import loadUi
from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(749, 566)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 380, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 749, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.draw_circle)
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen()
        for center_x, center_y, radius, color in self.circles:
            brush = QBrush(color)
            painter.setPen(pen)
            painter.setBrush(brush)
            painter.drawEllipse(center_x - radius, center_y - radius, 2 * radius, 2 * radius)

    def draw_circle(self):
        diameter = randint(20, 100)
        center_x = randint(diameter // 2, self.width() - diameter // 2)
        center_y = randint(diameter // 2, self.height() - diameter // 2)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.circles.append((center_x, center_y, diameter // 2, color))
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())