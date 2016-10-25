from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

app = QApplication(sys.argv)
window = QWidget()

grid = QGridLayout(window)


#lb = QLabel("title")
#grid.addWidget(lb , 0,0)
grid.addWidget(QLabel("Title"),0,0)
grid.addWidget(QLabel("Author"),1,0)
grid.addWidget(QLabel("Review"),2,0)


grid.addWidget(QLineEdit(),0,1)
grid.addWidget(QLineEdit(),1,1)
grid.addWidget(QTextEdit(),2,1)




window.show()
app.exec_()