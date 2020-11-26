# import hệ thống
import sys

from PyQt5 import QtCore # import vào thư viện pyqt5 
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic

class AppWindow(QDialog):
    def __init__(self):
        super(AppWindow,self).__init__()
        self.ui = uic.loadUi('demoLCD.ui', self)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showlcd)
        timer.start(1000)
        self.showlcd()

    def showlcd(self):
        time = QtCore.QTime.currentTime()
        text = time.toString('mm:ss')
        self.ui.lcdNumber.display(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())
