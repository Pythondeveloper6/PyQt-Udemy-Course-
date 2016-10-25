__author__ = 'Mahmoud Ahmed'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
app = QApplication(sys.argv)
windo = QWidget()
windo.setWindowTitle('Hello PyQT')
windo.setWindowIcon(QIcon('pyqt.png'))
windo.setGeometry(50,50,600,400)

cm = QComboBox(windo)
cm.move(200,200)
cm.resize(200,50)
cm.addItem('PyQT')
cm.addItem('Kivy')
cm.addItem('wx')
cm.addItem('PySide')
cm.setCurrentIndex(2)

windo.show()
app.exec_()