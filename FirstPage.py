# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo
import pandas as pd


myserver = "mongodb+srv://admin:1234@cluster0.7voii.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority"

class Ui_Dialog(object):
    def __init__(self):
        self.login = False


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(634, 354)
        Dialog.setWindowIcon(QtGui.QIcon('/src/python.png'))
        self.gridLayout_7 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidget, 0, 3, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(190, 250))
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 180, 81, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(20, 180, 81, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 140, 161, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 23, 13))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(20, 90, 161, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 24, 13))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(20, 40, 161, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 23, 13))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.groupBox, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_3, 0, 1, 1, 1)

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
        Dialog.setWindowTitle(_translate("Dialog", "Revenue Reporter - Main Menu"))
        self.groupBox.setTitle(_translate("Dialog", "Menu"))
        self.pushButton_2.setText(_translate("Dialog", "VIEW REPORT"))
        self.pushButton.setText(_translate("Dialog", "ADD/UPDATE"))
        self.label_3.setText(_translate("Dialog", "Price"))
        self.label_2.setText(_translate("Dialog", "Type"))
        self.label.setText(_translate("Dialog", "Date"))



    def AddtoDB(self):

        if not self.lineEdit_2.text().isnumeric():
            self.lineEdit_2.setText("0")

        if self.login:
            with pymongo.MongoClient(myserver) as conn:
                try:
                    db = conn.get_database("PyProject")
                    found = db.Revenue.count_documents({"Date": self.dateEdit.dateTime().toPyDateTime()})
                    if found > 0:
                        db.Revenue.update_one({"Date": self.dateEdit.dateTime().toPyDateTime()}, {"$set": {
                            self.comboBox.currentText(): float(self.lineEdit_2.text())
                        }})
                    else:
                        insert_data = {"Date": self.dateEdit.dateTime().toPyDateTime()}
                        for i in range(self.comboBox.count()):
                            if self.comboBox.itemText(i) == self.comboBox.currentText():
                                insert_data = {**insert_data, self.comboBox.itemText(i): float(self.lineEdit_2.text())}
                            else:
                                insert_data = {**insert_data, self.comboBox.itemText(i): 0}
                        try:
                            db.Revenue.insert_one(insert_data)
                        except Exception as e:
                            print("Data Incorrect")

                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Information)
                    msg.setWindowTitle("Success!")
                    msg.setText("Process Complete!")
                    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    msg.exec_()

                    try:
                        self.Display()
                    except Exception as e:
                        print(e)


                except Exception as e:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setWindowTitle("Error!")
                    msg.setText(e)
                    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    msg.exec_()

        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("Error!")
            msg.setText("Please Login!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()







    def Display(self):

        self.revenue = {'Date': [],
                        'Toys': [],
                        'Foods': [],
                        'Furniture': [],
                        'Clothes': [],
                        'Electronics': []
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

            df = pd.DataFrame(self.revenue, columns=['Date', 'Toys', 'Foods', 'Furniture', 'Clothes', 'Electronics'])
            year = df.Date.str[0:4]
            self.report_sum = df.groupby(year)[['Toys', 'Foods', 'Furniture', 'Clothes', 'Electronics']].sum()
            self.report_sum = self.report_sum.reset_index(level=['Date'])
            plot = self.report_sum.plot.bar(rot=0,x='Date')
            plot.set_xlabel("Years")
            fig = plot.get_figure()
            fig.savefig("src/output.png")



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
