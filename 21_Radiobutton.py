__author__ = 'Mahmoud Ahmed'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
app = QApplication(sys.argv)
windo = QWidget()
windo.setWindowTitle('Hello PyQT')
windo.setWindowIcon(QIcon('pyqt.png'))
windo.setGeometry(50,50,600,400)

rd = QRadioButton(windo , text='PyQT')
rd.move(200,150)

rd2 = QRadioButton(windo , text='kivy')
rd2.move(200,190)

checkbox = QCheckBox(windo , text='PyQT')
checkbox.move(280,150)

checkbox2 = QCheckBox(windo , text='Kivy')
checkbox2.move(280,190)


windo.show()
app.exec_()