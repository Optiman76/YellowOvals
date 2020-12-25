import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.btn.clicked.connect(self.draw)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawOvals(qp)
            qp.end()

    def draw(self, qp):
        self.do_paint = True
        self.repaint()

    def drawOvals(self, qp):
        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(100, 100, 200, 200)
        for i in range(2):
            d = randint(10, 100)
            x = randint(0, self.width() - d)
            y = randint(0, self.height() - d)
            qp.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())