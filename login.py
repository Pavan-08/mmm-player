from os import listdir
from time import sleep
from sign_up import Ui_Sign_up
from PyQt5 import QtCore, QtGui, QtWidgets
from mood import Ui_mood
import mmm


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(568, 524)
        LoginWindow.setStyleSheet("background-color: rgb(255, 49, 218);\n"
                                  "font: 75 12pt \"MS Shell Dlg 2\";\n"
                                  "background-color: rgb(0, 255, 255);\n"
                                  "")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 50, 171, 16))
        self.label.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                 "font: 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 130, 151, 41))
        self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(210, 230, 101, 31))
        self.login_btn.setStyleSheet("background-color: rgb(170, 255, 255);\n"
                                     "font: 75 12pt \"MS Shell Dlg 2\";\n"
                                     "")
        self.login_btn.setObjectName("login_btn")
        self.Usernam_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Usernam_text.setGeometry(QtCore.QRect(240, 40, 221, 41))
        self.Usernam_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "font: 75 14pt \"MS Shell Dlg 2\";")
        self.Usernam_text.setText("")
        self.Usernam_text.setObjectName("Usernam_text")
        self.passwrd_text = QtWidgets.QLineEdit(self.centralwidget)
        self.passwrd_text.setGeometry(QtCore.QRect(240, 130, 221, 41))
        self.passwrd_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "font: 75 14pt \"MS Shell Dlg 2\";")

        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwrd_text.setFont(font)
        self.passwrd_text.setObjectName("passwrd_text")
        self.New_user_btn = QtWidgets.QPushButton(self.centralwidget)
        self.New_user_btn.setGeometry(QtCore.QRect(370, 270, 171, 41))
        self.New_user_btn.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(255, 255, 255);")
        self.New_user_btn.setObjectName("New_user_btn")
        self.guest_login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.guest_login_btn.setGeometry(QtCore.QRect(370, 330, 171, 41))
        self.guest_login_btn.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                           "background-color: rgb(255, 255, 255);")
        self.guest_login_btn.setObjectName("guest_login_btn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 390, 201, 41))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 568, 30))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        self.login_btn.clicked.connect(self.login)
        self.guest_login_btn.clicked.connect(self.guestLogin)
        self.New_user_btn.clicked.connect(self.newUser)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.label.setText(_translate("LoginWindow", "Enter User Name:"))
        self.label_2.setText(_translate("LoginWindow", "Enter Password:"))
        self.login_btn.setText(_translate("LoginWindow", "LOGIN"))
        self.New_user_btn.setText(_translate("LoginWindow", "->New User"))
        self.guest_login_btn.setText(_translate("LoginWindow", "->Guest Login"))

    def login(self):
        userid = self.Usernam_text.text()
        pssw = self.passwrd_text.text()

        if userid in listdir("Users"):

            file = open(f"Users\\{userid}\\credentials", "r")
            verify = file.read().splitlines()

            if pssw in verify:
                self.label_3.setText("Success")
                self.loginSuccess()

            else:
                self.label_3.setText("Wrong Password ")
                print("Wrong Password")


        else:
            self.label_3.setText("UnRegistered User")
            print("User Not registered")

    def loginSuccess(self):
        print("Login Successful")
        self.label_3.setText("Login Successful")
        sleep(1)
        LoginWindow.close()
        self.newWindow = QtWidgets.QMainWindow()
        self.guest = False
        self.ui = Ui_mood(self.guest,self.Usernam_text.text())
        self.ui.setupUi(self.newWindow)
        self.newWindow.show()

    def newUser(self):
        self.newWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Sign_up()
        self.ui.setupUi(self.newWindow)
        self.newWindow.show()

    def guestLogin(self):
        print("Guest Login")
        self.label_3.setText("Guest Login")
        LoginWindow.close()
        self.newWindow = QtWidgets.QMainWindow()
        self.guest = "False"
        self.ui = Ui_mood(self.guest,"")
        self.ui.setupUi(self.newWindow)
        self.newWindow.show()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
