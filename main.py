from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from FirstPage import Ui_Dialog
from Report import Report_Dialog



class Main(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Main,self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.clicked)
        self.report = Report(self)

    def clicked(self):
        self.report.ui.label.setPixmap(QtGui.QPixmap("output.png"))
        self.report.show()


class Report(QtWidgets.QDialog):

    def __init__(self,parent=None):
        super(Report,self).__init__(parent)
        self.ui = Report_Dialog()
        self.ui.setupUi(self)




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    menu = Main()
    menu.show()
    app.exec_()
