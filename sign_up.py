import os
from os import listdir

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sign_up(object):
    def setupUi(self, Sign_up):
        Sign_up.setObjectName("Sign_up")
        Sign_up.resize(628, 430)
        Sign_up.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Sign_up)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 80, 151, 41))
        self.label.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 160, 141, 41))
        self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.User_name = QtWidgets.QLineEdit(self.centralwidget)
        self.User_name.setGeometry(QtCore.QRect(230, 80, 231, 41))
        self.User_name.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.User_name.setText("")
        self.User_name.setObjectName("User_name")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(230, 160, 231, 41))
        self.password.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.password.setText("")
        self.password.setObjectName("password")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 320, 231, 31))
        self.label_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 255);\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 240, 121, 41))
        self.pushButton.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        Sign_up.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Sign_up)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 628, 26))
        self.menubar.setObjectName("menubar")
        Sign_up.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Sign_up)
        self.statusbar.setObjectName("statusbar")
        Sign_up.setStatusBar(self.statusbar)

        self.retranslateUi(Sign_up)
        QtCore.QMetaObject.connectSlotsByName(Sign_up)

        self.pushButton.clicked.connect(self.register)

    def retranslateUi(self, Sign_up):
        _translate = QtCore.QCoreApplication.translate
        Sign_up.setWindowTitle(_translate("Sign_up", "MainWindow"))
        self.label.setText(_translate("Sign_up", "Enter Username"))
        self.label_2.setText(_translate("Sign_up", "Enter Password"))
        self.pushButton.setText(_translate("Sign_up", "Sign up"))

    def register(self):
        userid = self.User_name.text()
        pssw = self.password.text()

        if(userid=="" or pssw==""):
            self.label_3.setText("Wrong Input")
        if userid in listdir("Users"):
            self.label_3.setText("Username already exists!")
        else:
            os.chdir('C:\\Users\\pa1ka\\Desktop\\Mini Project\\Users')
            os.mkdir(userid)
            file = open(f"C:\\Users\\pa1ka\\Desktop\\Mini Project\\Users\\{userid}\\"+"credentials","w")
            file.write(userid+"\n"+pssw)
            file.close()

            self.label_3.setText("Registration Success")
            print("Registration Successful")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sign_up = QtWidgets.QMainWindow()
    ui = Ui_Sign_up()
    ui.setupUi(Sign_up)
    Sign_up.show()
    sys.exit(app.exec_())
