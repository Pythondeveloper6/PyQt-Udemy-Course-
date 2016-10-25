__author__ = 'Mahmoud Ahmed'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
app = QApplication(sys.argv)
windo = QWidget()
windo.setWindowTitle('Hello PyQT')
windo.setWindowIcon(QIcon('pyqt.png'))
windo.setGeometry(50,50,600,400)

def show_font():
    fd = QFontDialog.getFont()

bt = QPushButton(windo , text='Fonts')
bt.move(200,180)
bt.clicked.connect(show_font)

windo.show()
app.exec_()