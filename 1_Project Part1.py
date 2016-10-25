from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Main(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)




def main():
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    app.exec_()


if __name__ == "__main__" :
    main()