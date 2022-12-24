# import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit)
#
#
# class MyApp(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         grid = QGridLayout()
#         self.setLayout(grid)
#
#         grid.addWidget(QLabel('Title:'), 0, 0)
#         grid.addWidget(QLabel('Author:'), 1, 0)
#         grid.addWidget(QLabel('Review:'), 2, 0)
#         grid.addWidget(QLabel('1:'), 3, 0)
#
#         grid.addWidget(QLineEdit(), 0, 1)
#         grid.addWidget(QLineEdit(), 1, 1)
#         grid.addWidget(QTextEdit(), 2, 1)
#         grid.addWidget(QLineEdit(), 3, 1)
#
#
#         self.setWindowTitle('QGridLayout')
#         self.setGeometry(300, 300, 300, 200)
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('SETTING1'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        fileAction = QAction(QIcon('FILE1'), 'FILE', self)
        fileAction.setShortcut('Ctrl+A')
        fileAction.setStatusTip('FILE application')
        fileAction.triggered.connect(qApp.quit)

        homeAction = QAction(QIcon('HOME1'), 'HOME', self)
        homeAction.setShortcut('Ctrl+V')
        homeAction.setStatusTip('HOME application')
        homeAction.triggered.connect(qApp.quit)


        self.statusBar()

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.toolbar = self.addToolBar('FILE')
        self.toolbar.addAction(fileAction)

        self.toolbar = self.addToolBar('HOME')
        self.toolbar.addAction(homeAction)

        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())