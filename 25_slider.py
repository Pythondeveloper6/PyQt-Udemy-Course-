__author__ = 'Mahmoud Ahmed'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
app = QApplication(sys.argv)
windo = QWidget()
windo.setWindowTitle('Hello PyQT')
windo.setWindowIcon(QIcon('pyqt.png'))
windo.setGeometry(50,50,600,400)

sl = QSlider(Qt.Horizontal ,windo)
sl.move(200,180)
sl.resize(180,20)
sl.setValue(30)

windo.show()
app.exec_()