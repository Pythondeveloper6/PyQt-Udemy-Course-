__author__ = 'Mahmoud Ahmed'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


app = QApplication(sys.argv)
windo = QWidget()
windo.setWindowTitle('Hello PyQT')
windo.setWindowIcon(QIcon('pyqt.png'))

#windo.resize(600,400)
#windo.move(50,50)

#windo.setGeometry((move)(resize))
windo.setGeometry(50,50,600,400)

windo.show()
app.exec_()