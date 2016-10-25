from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

app = QApplication(sys.argv)
window = QWidget()

grid = QGridLayout(window)

grid.addWidget(QPushButton("Button1") ,0,0)
grid.addWidget(QPushButton("Button2"),0,1)

grid.addWidget(QPushButton("Button3"),1,0)
grid.addWidget(QPushButton("Button4"),2,1)

grid.addWidget(QPushButton("Button5"),3,2)

grid.addWidget(QLineEdit(),0,2)

window.show()
app.exec_()