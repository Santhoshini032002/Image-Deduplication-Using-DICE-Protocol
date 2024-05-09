# Image-Deduplication-Using-DICE-Protocol
#HOME PAGE
from PyQt5 import QtCore, QtGui, QtWidgets
from User import Ui_User
from CSP import Ui_CSP
class Ui_Dialog(object):

    def userlogin(self, event):
        try:
            self.usr = QtWidgets.QDialog()
            self.ui = Ui_User(self.usr)
            self.ui.setupUi(self.usr)
            self.usr.show()
            event.accept()

        except Exception as e:
            print("Error", e.args[0])
            tb = sys.exc_info()[2]
            print("line no", tb.tb_lineno)

    def csplogin(self, event):
        try:
            self.csp = QtWidgets.QDialog()
            self.ui = Ui_CSP(self.csp)
            self.ui.setupUi(self.csp)
            self.csp.show()
            event.accept()

        except Exception as e:
            print("Error", e.args[0])
            tb = sys.exc_info()[2]
            print("line no", tb.tb_lineno)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(739, 563)
        Dialog.setStyleSheet("background-color: rgb(200, 135, 70);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 0, 651, 141))
        self.label.setStyleSheet("color: rgb(85, 0, 127);\n"
"font: 75 16pt \"Verdana\";")
        self.label.setObjectName("label")
        self.users = QtWidgets.QLabel(Dialog)
        self.users.setGeometry(QtCore.QRect(140, 120, 411, 131))
        self.users.setStyleSheet("image: url(../DICE/images/user.png);")
        self.users.setText("")
        self.users.setObjectName("users")
        self.users.mousePressEvent = self.userlogin
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(310, 250, 111, 51))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Verdana\";")
        self.label_3.setObjectName("label_3")
        self.csp = QtWidgets.QLabel(Dialog)
        self.csp.setGeometry(QtCore.QRect(220, 320, 271, 121))
        self.csp.setStyleSheet("image: url(../DICE/images/csp.png);")
        self.csp.setText("")
        self.csp.setObjectName("csp")
        self.csp.mousePressEvent = self.csplogin
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(230, 450, 241, 21))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Verdana\";")
        self.label_5.setObjectName("label_5")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Home"))
        self.label.setText(_translate("Dialog", "Client Side Secure Image Deduplication Using DICE Protocol"))
        self.label_3.setText(_translate("Dialog", "Users"))
        self.label_5.setText(_translate("Dialog", "Cloud Service Provider"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
