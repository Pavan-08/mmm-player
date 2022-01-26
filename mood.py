from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets

import mmm


class Ui_mood(object):
    def __init__(self,guest,user_id):
        self.guest = guest
        self.user_id = user_id
    def setupUi(self, mood):

        mood.setObjectName("mood")
        mood.resize(622, 522)
        self.centralwidget = QtWidgets.QWidget(mood)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 90, 241, 71))
        self.label.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(210, 210, 141, 41))
        self.comboBox.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(220, 330, 131, 51))
        self.submitButton.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.submitButton.setObjectName("submitButton")
        mood.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mood)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 26))
        self.menubar.setObjectName("menubar")
        mood.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mood)
        self.statusbar.setObjectName("statusbar")
        mood.setStatusBar(self.statusbar)

        self.retranslateUi(mood)
        QtCore.QMetaObject.connectSlotsByName(mood)

        self.submitButton.clicked.connect(self.pressed)
    def pressed(self):
        #mood.hide()
        mmm.main(self.comboBox.currentText(), self.guest, self.user_id)



    def retranslateUi(self, mood):
        _translate = QtCore.QCoreApplication.translate
        mood.setWindowTitle(_translate("mood", "MainWindow"))
        self.label.setText(_translate("mood", " How\'s your Mood?"))
        self.comboBox.setItemText(0, _translate("mood", "Happy"))
        self.comboBox.setItemText(1, _translate("mood", "Sad"))
        self.comboBox.setItemText(2, _translate("mood", "Party"))
        self.submitButton.setText(_translate("mood", "SUBMIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mood = QtWidgets.QMainWindow()
    ui = Ui_mood()
    ui.setupUi(mood)
    mood.show()
    sys.exit(app.exec_())
