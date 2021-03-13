from PyQt5 import QtCore, QtGui, QtWidgets
import os
from dotenv import load_dotenv
import hashlib
import binascii

from FirstPage import Ui_Dialog
from Report import Report_Dialog
from Predict import Ui_Dialog as Predict_Dialog
from login import Ui_Dialog as Login_Dialog

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pymongo

myserver = "mongodb+srv://admin:1234@cluster0.7voii.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority"
load_dotenv(dotenv_path='.env')
salt = os.getenv("SALT")


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):

        super(Login,self).__init__(parent)
        self.ui = Login_Dialog()

        self.ui.setupUi(self)
        self.oldPos = self.pos()

        self.setWindowIcon(QtGui.QIcon('src/python.png'))
        self.ui.pushButton.clicked.connect(self.trylogin)



    def close(self):
        self.hide()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def trylogin(self):
        with pymongo.MongoClient(myserver) as conn:
            try:
                db = conn.get_database("PyProject")
                found = db.Users.count_documents({"Username":self.ui.lineEdit.text()})

                if found > 0:
                    users = {}
                    cur = db.Users.find_one({"Username":self.ui.lineEdit.text()})
                    try:
                        newkey = hashlib.pbkdf2_hmac('sha256', self.ui.lineEdit_2.text().encode('utf-8'), salt.encode(), 100000)
                        if cur['Password'] == binascii.hexlify(newkey).decode():
                            msg = QtWidgets.QMessageBox()
                            msg.setIcon(QtWidgets.QMessageBox.Information)
                            msg.setWindowTitle("Success")
                            msg.setText(f"Login Complete! - Welcome {cur['Username']}")
                            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                            msg.exec_()

                            self.parent().ui.login = True
                            self.hide()

                        else:
                            msg = QtWidgets.QMessageBox()
                            msg.setIcon(QtWidgets.QMessageBox.Warning)
                            msg.setWindowTitle("Warnning")
                            msg.setText("Username / Password Incorrect")
                            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                            msg.exec_()

                    except Exception as e:
                        print(e)

                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setWindowTitle("Warnning")
                    msg.setText("Username / Password Incorrect")
                    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    msg.exec_()

            except Exception as e:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("Error")
                msg.setText(e)
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()




class Main(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Main,self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('src/python.png'))
        self.gotoLogin = Login(self)

        self.ui.pushButton.clicked.connect(self.checkLogin)
        self.ui.pushButton_2.clicked.connect(self.clicked)
        self.report = Report(self)

    def checkLogin(self):
        if self.ui.login:
            self.ui.AddtoDB()
        else:
            self.gotoLogin.show()




    def clicked(self):

        self.report.ui.label.setPixmap(QtGui.QPixmap("src/output.png"))
        self.report.show()


class Report(QtWidgets.QDialog):

    def __init__(self,parent=None):
        super(Report,self).__init__(parent)
        self.ui = Report_Dialog()
        self.predict = Predict(self)

        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.export_to_csv)
        self.ui.pushButton_3.clicked.connect(self.OpenPredict)

    def OpenPredict(self):
        self.predict.show()





    def export_to_csv(self):
        try:
           self.parent().ui.report_sum.reset_index().to_csv('output/output.csv')
           msg = QtWidgets.QMessageBox()
           msg.setIcon(QtWidgets.QMessageBox.Information)
           msg.setWindowTitle("Success!")
           msg.setText("CSV file export complete")
           msg.setInformativeText("Please check in output folder [output.csv]")
           msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
           msg.exec_()


        except Exception as e:
            print(e)


class Predict(QtWidgets.QDialog):


    def __init__(self,parent=None):
        super(Predict,self).__init__(parent)
        self.ui = Predict_Dialog()
        self.ui.setupUi(self)
        self.report_sum = self.parent().parent().ui.report_sum
        self.ui.comboBox.currentTextChanged.connect(self.Show)
        self.ui.pushButton_2.clicked.connect(self.to_csv)

        for i in self.report_sum.columns:
            if i != "Date":
                self.ui.comboBox.addItem(i)


        self.Show()



    def Show(self):
        try:
            X = pd.to_numeric(self.report_sum['Date']).values.reshape(-1, 1)
            y = self.report_sum[self.ui.comboBox.currentText()].values.reshape(-1, 1)

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
            reg = LinearRegression()
            reg.fit(X_train, y_train)
            y_pred = reg.predict(X_test)
            plt.figure(figsize=(5,5),dpi=100)
            plt.scatter(X, y, c='black')

            plt.plot(
                X_test,
                y_pred,
                c='blue',
                linewidth=2
            )
            plt.xlabel("Year")
            plt.ylabel("Revenue")


            plt.savefig("src/predict.png")

            self.ui.label_2.setText("Cofficeint : {0:.2f}".format(reg.coef_[0][0]))

            if reg.coef_[0][0] < 0 :
                self.ui.label_3.setText(f"Loss")
                self.ui.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 102, 0);")
            if reg.coef_[0][0] < -1:
                self.ui.label_3.setText(f"Very Loss")
                self.ui.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                              "background-color: rgb(255, 0, 0);")
            if reg.coef_[0][0] == 0:
                self.ui.label_3.setText(f"Natural")
                self.ui.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
                                              "background-color: rgb(255, 204, 153);")
            if reg.coef_[0][0] > 0:
                self.ui.label_3.setText(f"Slightly Gain ")
                self.ui.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                              "background-color: rgb(51, 204, 51);")
            if reg.coef_[0][0] > 0.7:
                self.ui.label_3.setText(f"Well Gain ")
                self.ui.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                              "background-color: rgb(0, 102, 0);")



            self.ui.label.setPixmap(QtGui.QPixmap("src/predict.png"))


        except Exception as e :
            print(e)

    def to_csv(self):

        report = {"Products":[],"Status":[],"Suggestion":[]}

        for i in self.report_sum.columns:
            if i != "Date":
                report['Products'].append(i)
                X = pd.to_numeric(self.report_sum['Date']).values.reshape(-1, 1)
                y = self.report_sum[i].values.reshape(-1, 1)

                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
                reg = LinearRegression()
                reg.fit(X_train, y_train)
                y_pred = reg.predict(X_test)

                status = ""
                sug = ""

                if reg.coef_[0][0] < 0:
                   status = "Loss"
                   sug = "Be aware in selling it next year"

                if reg.coef_[0][0] < -1:
                   status = "Very Loss"
                   sug = "Please Consider to cut loss"
                if reg.coef_[0][0] == 0:
                    status = "Natural"
                    sug = "Nothing to worry yet"
                if reg.coef_[0][0] > 0:
                    status = "Slightly Gain"
                    sug = "Please Consider to stock this product"

                if reg.coef_[0][0] > 0.7:
                    status = "Well Gain"
                    sug = "This product might make profit as well next year"

                report['Status'].append(status)
                report['Suggestion'].append(sug)

                df = pd.DataFrame(report, columns=['Products', 'Status','Suggestion'])

        df.reset_index().to_csv('output/predict.csv')
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Success!")
        msg.setText("CSV file export complete")
        msg.setInformativeText("Please check in output folder [predict.csv]")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()





if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    app.setStyle('Fusion')
    menu = Main()
    menu.show()
    app.exec_()
