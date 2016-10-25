__author__ = 'Mahmoud Ahmed'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
app = QApplication(sys.argv)
windo = QWidget()
windo.setWindowTitle('Hello PyQT')
windo.setWindowIcon(QIcon('pyqt.png'))
windo.setGeometry(50,50,600,400)

lb = QLabel(windo , text='UserName')
lb.move(100, 180)

lb2 = QLabel(windo , text='Password')
lb2.move(100 ,220)

le = QLineEdit(windo )
le.move(180 , 180)

le2 = QLineEdit(windo)
le2.move(180,220)
le2.setEchoMode(QLineEdit.Password)


windo.show()
app.exec_()