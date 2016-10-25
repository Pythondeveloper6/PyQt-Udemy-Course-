from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

app = QApplication(sys.argv)
window = QWidget()

b1 = QPushButton(window , text='button1')
b2 = QPushButton(window , text='button2')

vbox = QVBoxLayout(window)
vbox.addWidget(b1)
vbox.addStretch()
vbox.addWidget(b2)

hbox = QHBoxLayout()
b3 = QPushButton(window , text='button3')
b4 = QPushButton(window , text='button4')

hbox.addWidget(b3)
hbox.addStretch()
hbox.addWidget(b4)

vbox.addLayout(hbox)

window.show()
app.exec_()