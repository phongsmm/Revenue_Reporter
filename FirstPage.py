# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo
import pandas as pd
import matplotlib as plt


myserver = "mongodb+srv://admin:1234@cluster0.7voii.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority"


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(577, 414)
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(20, 70, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 220, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 260, 111, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 47, 13))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 180, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 130, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(150, 10, 411, 381))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.comboBox.addItem("Toys")
        self.comboBox.addItem("Foods")
        self.comboBox.addItem("Furniture")
        self.comboBox.addItem("Clothes")
        self.comboBox.addItem("Electronics")

        self.Display()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "ADD/UPDATE"))
        self.pushButton_2.setText(_translate("Dialog", "VIEW REPORT"))
        self.label.setText(_translate("Dialog", "Date"))
        self.label_2.setText(_translate("Dialog", "Type"))
        self.label_3.setText(_translate("Dialog", "Price"))
        self.pushButton.clicked.connect(self.AddtoDB)





    def AddtoDB(self):
        with pymongo.MongoClient(myserver) as conn:
            try:
                db = conn.get_database("PyProject")
                found = db.Revenue.count_documents({"Date": self.dateEdit.dateTime().toPyDateTime()})
                if found > 0:
                    db.Revenue.update_one({"Date":self.dateEdit.dateTime().toPyDateTime()},{"$set":{
                        self.comboBox.currentText():float(self.lineEdit_2.text())
                    }})
                    print(self.comboBox.currentText())
                    print(float(self.lineEdit_2.text()))
                    print("Update")
                else:
                    db.Revenue.insert_one({})
                    print("insert")

                self.Display()

            except Exception as e:
                print(e)



    def Display(self):

        self.revenue = {'Date': [],
                'Toys': [],
                'Foods':[],
                'Furniture':[],
                'Clothes':[],
                'Electronics':[]
                }


        with pymongo.MongoClient(myserver) as conn:
            db = conn.get_database("PyProject")
            cur = db.Revenue.find({}).sort([('Date', -1)])
            found = db.Revenue.count_documents({})

            self.tableWidget.setRowCount(found)
            self.tableWidget.setColumnCount(6)

            for i, v in enumerate(cur):
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(v['Date'].date())))
                self.revenue['Date'].append(str(v['Date'].date()))
                print(v['Date'])
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(v['Toys'])))
                self.revenue['Toys'].append(v['Toys'])
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(v['Foods'])))
                self.revenue['Foods'].append(v['Foods'])
                self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(v['Furniture'])))
                self.revenue['Furniture'].append(v['Furniture'])
                self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(v['Clothes'])))
                self.revenue['Clothes'].append(v['Clothes'])
                self.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(v['Electronics'])))
                self.revenue['Electronics'].append(v['Electronics'])

            df = pd.DataFrame(self.revenue,columns=['Date','Toys','Furniture','Clothes','Electronics'])

            year = df.Date.str[0:4]

            sum = df.groupby(year)['Clothes'].sum()
            print(sum)

            plot = df.plot()
            fig = plot.get_figure()
            fig.savefig("output.png")




        header1 = QtWidgets.QTableWidgetItem("Date")
        header2 = QtWidgets.QTableWidgetItem("Toys")
        header3 = QtWidgets.QTableWidgetItem("Foods")
        header4 = QtWidgets.QTableWidgetItem("Furniture")
        header5 = QtWidgets.QTableWidgetItem("Clothes")
        header6 = QtWidgets.QTableWidgetItem("Electronics")

        self.tableWidget.setHorizontalHeaderItem(0, header1)
        self.tableWidget.setHorizontalHeaderItem(1, header2)
        self.tableWidget.setHorizontalHeaderItem(2, header3)
        self.tableWidget.setHorizontalHeaderItem(3, header4)
        self.tableWidget.setHorizontalHeaderItem(4, header5)
        self.tableWidget.setHorizontalHeaderItem(5, header6)









if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())