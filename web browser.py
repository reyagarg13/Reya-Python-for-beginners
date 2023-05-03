import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyBrowser")
        self.setWindowIcon(QIcon("icons/python.png"))
        self.setGeometry(200,200, 900,600)

        toolbar = QToolBar()
        self.addToolBar(toolbar)


        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon('icons/back.png'))
        self.backButton.setIconSize(QSize(36,36))
        toolbar.addWidget(self.backButton)

        self.reloadButton = QPushButton()
        self.reloadButton.setIcon(QIcon('icons/reload.png'))
        self.reloadButton.setIconSize()
