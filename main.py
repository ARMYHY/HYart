
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


    def mousePressEvent(self, event):
        mouse_pt = "Mouse Point : sx={0},sy={1}".format(event.x(), event.y())

    def mouseReleaseEvent(self, event):
        mouse_pt2 = "Mouse Point : ex={0},ey={1}".format(event.x(), event.y())
        self.draw_Line(event.sx{0}, event.sy{1}, event.ex{2}, event.ey{3})

    def draw_Line(self,event.sx{0}, event.sy{1}, event.ex{2}, event.ey{3}):
        qp.setPen(QPen(Qt.black, 10, Qt.SolidLine))
        qp.drawLine(moust_pt,mouse_pt2)
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



    def mousePressEvent(self, event):
        mouse_pt = "Mouse Point : sx={0},sy={1}".format(event.x(), event.y())
        self.status_bar.showMessage(mouse_pt)
    def mouseReleaseEvent(self, event):
        mouse_pt2 = "Mouse Point : ex={0},ey={1}".format(event.x(), event.y())
        self.status_bar.showMessage(mouse_pt2)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''