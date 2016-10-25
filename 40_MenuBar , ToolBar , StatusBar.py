from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
app = QApplication(sys.argv)

window = QMainWindow()

def status_bar():
    window.statusBar().showMessage('OPen Pressed')

menu = QMenuBar(window)

file_menu = menu.addMenu('File')
edit_menu = menu.addMenu('Edit')

new = QAction(QIcon('pyqt.png'),'New Project' , window)
new.setShortcut('ctrl+N')

open = QAction(QIcon('pyqt.png') , 'Open' , window)
open.triggered.connect(status_bar)
open.setShortcut('ctrl+O')


close = QAction(QIcon('Ruby.png'),'Close App' , window)
close.triggered.connect(window.close)
close.setShortcut('ctrl+s')

sub = QMenu("Open Recent")
sub.addAction(".py")
sub.addAction(".pyc")

file_menu.addAction(new)
file_menu.addAction(open)
file_menu.addMenu(sub)
file_menu.addAction(close)

window.toolbar = window.addToolBar('toolbar')
window.toolbar.addAction(close)
window.toolbar.addAction(open)
window.toolbar.addAction(new)

window.show()
app.exec_()