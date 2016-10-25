__author__ = 'Mahmoud Ahmed'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
app = QApplication(sys.argv)
windo = QWidget()
windo.setWindowTitle('Hello PyQT')
windo.setWindowIcon(QIcon('pyqt.png'))
windo.setGeometry(50,50,600,400)

checkbox = QCheckBox(windo , text='PyQT')
checkbox.move(200,200)
checkbox.setChecked(True)   #bool = true or false

checkbox2 = QCheckBox(windo , text='Kivy')
checkbox2.move(200,250)

windo.show()
app.exec_()