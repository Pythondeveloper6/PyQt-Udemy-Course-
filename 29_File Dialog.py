__author__ = 'Mahmoud Ahmed'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Open File Dialog')
window.resize(500,500)


def upload():
    open_file = QFileDialog.getOpenFileName(window,"OPen File" , '/')
    print(open_file)
    print()
    print('ــــــــــــــــــــــــ')

    with open(open_file , 'r') as f :
        print(f.read())


bt = QPushButton(window , text="Upload A File")
bt.clicked.connect(upload)
bt.move(200,200)

window.show()
app.exec_()