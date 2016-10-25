__author__ = 'Mahmoud Ahmed'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
app = QApplication(sys.argv)
windo = QWidget()
windo.setWindowTitle('Hello PyQT')
windo.setWindowIcon(QIcon('pyqt.png'))
windo.setGeometry(50,50,600,400)


############                   (qwidget , title , question , controls , desfault value)
message = QMessageBox.question(windo , 'Message box' , 'Do You Want to Exit ?' , QMessageBox.Yes|QMessageBox.No ,QMessageBox.No)

## information , critical , question . warning , about
windo.show()
app.exec_()