from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Main(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.InitUi()
        self.filename = ""



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
        self.newAction.triggered.connect(self.new)
        self.newAction.setShortcut("ctrl+N")

        self.openAction = QAction("Open" , self)
        self.openAction.triggered.connect(self.open)
        self.openAction.setShortcut('ctrl+O')

        self.saveAction = QAction("Save" , self)
        self.saveAction.triggered.connect(self.save)
        self.saveAction.setShortcut('ctrl+S')

    def Formatbar(self):
        fontbox = QFontComboBox(self)
        fontbox.currentFontChanged.connect(lambda font: self.text.setCurrentFont(font))
        fontsize = QSpinBox(self)
        fontsize.setSuffix(" pt")
        fontsize.valueChanged.connect(lambda size: self.text.setFontPointSize(size))
        fontsize.setValue(14)

        fontcolors = QAction(QIcon("icons/font-color.png") , "Change Font Color" , self)
        bold = QAction(QIcon("icons/bold.png"),"Change Font To Bold" , self)
        italic = QAction(QIcon("icons/italic.png"),"Change Font To Italic" , self)
        underline = QAction(QIcon("icons/underline.png"),"Put A Line Under Words" , self)
        strike = QAction(QIcon("icons/strike.png") , "Put A Line On Your Words" , self)

        aligh_left = QAction(QIcon("icons/align-left.png") , "Align Words To Left" , self)
        align_right =QAction(QIcon("icons/align-right.png") , "Align Words To Right" , self)
        align_center = QAction(QIcon("icons/align-center.png") , "Align Words To Center" , self)
        justify = QAction(QIcon("icons/align-justify.png") , "Justify Your Words" , self)


        self.formatbar = self.addToolBar("Format")
        self.formatbar.addWidget(fontbox)
        self.formatbar.addWidget(fontsize)
        self.formatbar.addSeparator()

        self.formatbar.addAction(fontcolors)
        self.formatbar.addAction(bold)
        self.formatbar.addAction(italic)
        self.formatbar.addAction(underline)
        self.formatbar.addAction(strike)
        self.formatbar.addSeparator()

        self.formatbar.addAction(aligh_left)
        self.formatbar.addAction(align_center)
        self.formatbar.addAction(align_right)
        self.formatbar.addAction(justify)
        self.formatbar.addSeparator()

    def new(self):
        window = Main(self)
        window.show()

    def open(self):
        self.filename = QFileDialog.getOpenFileName(self,"OPen File" , '.' , "(*.txt)")

        if self.filename:
            with open(self.filename ,"rt") as file :
                self.text.setText(file.read())

    def save(self):
        if not self.filename:
            self.filename = QFileDialog.getSaveFileName(self , "Save File")

        if not self.filename.endswith(".txt"):
            self.filename += ".txt"

        with open(self.filename , "wt") as file :
            file.write(self.text.toHtml())


    def InitUi(self):
        ## Start With The GUI
        self.text = QTextEdit(self)
        self.Toolbar()
        self.Formatbar()
        self.Menubar()
        self.setWindowTitle('Text Editor')
        self.setCentralWidget(self.text)
        self.setGeometry(100,100,900,600)

def main():
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    app.exec_()


if __name__ == "__main__" :
    main()