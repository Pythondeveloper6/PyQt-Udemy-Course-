from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

app = QApplication(sys.argv)
tabs = QTabWidget()

tab1 = QWidget()
tab2 = QWidget()
tab3 = QWidget()

vbox = QVBoxLayout(tabs)
b1= QPushButton("Ok")
b2 = QPushButton("Cancel")
vbox.addWidget(b1)
vbox.addStretch()
vbox.addWidget(b2)
tab1.setLayout(vbox)

vbox2 = QVBoxLayout(tabs)
l1 = QLineEdit()
lb = QLabel("Welcome")
vbox2.addWidget(l1)
vbox2.addWidget(lb)
tab2.setLayout(vbox2)

hbox = QHBoxLayout(tabs)
lc = QLCDNumber()
d = QDial()
hbox.addWidget(lc)
hbox.addWidget(d)
tab3.setLayout(hbox)


tabs.addTab(tab1 , "File")
tabs.addTab(tab2 , "Save ")
tabs.addTab(tab3 , "Settings")

tabs.show()
app.exec_()