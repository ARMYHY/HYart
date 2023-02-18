'''
import sys
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Points')
        self.show()
        self.centralwidget = QWidget()
        self.screen = QLabel(self.centralwidget)
        self.screen.setPixmap(QPixmap("HOME.png"))



        # 마우스 드레그 이벤트
    def mouseMoveEvent(self, event):
            # event.x(),y() : 마우스의 절대좌표 값
        self.draw_Line(event.x(), event.y())

        # 마우스 릴리즈 이벤트
    def mouseReleaseEvent(self, event):
            # event.x(),y() : 마우스의 절대좌표 값
        self.draw_Line(event.x(), event.y())

    def draw_Line(self, x, y):
        self.img = QPixmap("HOME2.png")
        qp = QPainter(self.img)
        qp.begin(self)
        qp.setPen(QPen(Qt.black, 10, Qt.SolidLine))
        qp.drawLine(400, 300, x, y)
        qp.end()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''

import sys
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*


class MyApp(QMainWindow):




    def __init__(self):
        super().__init__()

        self.status_bar = self.statusBar()
        self.statusBar().showMessage('Ready')
        self.show()



    def mouseMoveEvent(self, event):
        mouse_pt = "Mouse Point : x={0},y={0}".format(event.x(), event.y())
        self.status_bar.showMessage(mouse_pt)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())