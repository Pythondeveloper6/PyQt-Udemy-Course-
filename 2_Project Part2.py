from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Main(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.InitUi()



    def Menubar(self):
        ## Our MenuBar
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu('Edit')
        view = menubar.addMenu('View')

        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)

    def Toolbar(self):
        ## Our Toolbar
        self.newAction = QAction("New" , self)
        self.openAction = QAction("Open" , self)
        self.saveAction = QAction("Save" , self)


    def InitUi(self):
        ## Start With The GUI
        self.Toolbar()
        self.Menubar()
        self.setWindowTitle('Text Editor')

def main():
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    app.exec_()


if __name__ == "__main__" :
    main()