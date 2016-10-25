from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

app = QApplication(sys.argv)
window = QWidget()

button = QPushButton(window , text='Login')
button.move(80,100)
button.resize(90,60)

slider = QSlider(window)
slider.move(190,100)
slider.setValue(30)

def button_clicked():
    print('Button Clicked')
    slider.setValue(50)


button.clicked.connect(button_clicked)

window.show()
app.exec_()