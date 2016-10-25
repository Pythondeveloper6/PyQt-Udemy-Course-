__author__ = 'Mahmoud Ahmed'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
app = QApplication(sys.argv)
windo = QWidget()
windo.setWindowTitle('Hello PyQT')
windo.setWindowIcon(QIcon('pyqt.png'))
windo.setGeometry(50,50,600,400)

pb = QProgressBar(windo)
pb.move(200,180)
pb.resize(300,50)
pb.setValue(20)
pb.setAlignment(Qt.AlignCenter)

windo.show()
app.exec_()