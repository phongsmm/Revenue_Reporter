# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(515, 424)

        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/Phos/Desktop/index222.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 4)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 0);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Revenue Reporter - Predict Menu"))
        self.label_2.setText(_translate("Dialog", "coefficient = -21"))
        self.label_3.setText(_translate("Dialog", "Very Loss"))
        self.pushButton_2.setText(_translate("Dialog", "Export to CSV"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
