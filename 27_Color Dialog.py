__author__ = 'Mahmoud Ahmed'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
app = QApplication(sys.argv)
windo = QWidget()
windo.setWindowTitle('Hello PyQT')
windo.setWindowIcon(QIcon('pyqt.png'))
windo.setGeometry(50,50,600,400)

def show_colors():
    cd = QColorDialog.getColor()


bt = QPushButton(windo , text='Colors')
bt.move(200,180)
bt.resize(80,40)
bt.clicked.connect(show_colors)

windo.show()
app.exec_()