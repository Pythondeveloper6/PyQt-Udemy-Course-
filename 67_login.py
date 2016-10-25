from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


from window import Ui_Form


class main(QWidget,Ui_Form):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

        self.lineEdit.setPlaceholderText('Enter Your Name')
        self.lineEdit_2.setPlaceholderText("Enter Password")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.pushButton.clicked.connect(self.login)

    def login(self):
        if self.lineEdit.text() == 'admin' and self.lineEdit_2.text() == 'admin' :
            print('Welcome')



app = QApplication(sys.argv)
window = main()
window.show()
app.exec_()