__author__ = 'Mahmoud Ahmed'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
app = QApplication(sys.argv)
windo = QWidget()
windo.setWindowTitle('Hello PyQT')
windo.setWindowIcon(QIcon('pyqt.png'))
windo.setGeometry(50,50,600,400)

lineedit = QLineEdit(windo)
lineedit.resize(200,50)
lineedit.move(200,100)
## lineedit.setText('PyQt On Udemy')
lineedit.setPlaceholderText('Enter Your Name')
lineedit.setEchoMode(QLineEdit.Password)


windo.show()
app.exec_()