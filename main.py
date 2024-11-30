import sys
from random import randint
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor
from PyQt6.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('UI.ui', self)
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