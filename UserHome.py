from PyQt5 import QtCore, QtGui, QtWidgets
from Upload import Upload
from Downloading import Ui_Downloading
class Ui_UserHome(object):
    def __init__(self,unm):
        self.unm=unm


    def upload(self):
        self.uplad = QtWidgets.QDialog()
        self.ui = Upload(self.unm,self.uplad)
        self.ui.setupUi(self.uplad)
        self.uplad.show()

    def download(self):
        self.dwnlad = QtWidgets.QDialog()
        self.ui = Ui_Downloading(self.unm)
        self.ui.setupUi(self.dwnlad)
        self.ui.getFilelist()
        self.dwnlad.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(568, 484)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -10, 591, 501))
        self.label.setStyleSheet("background-image: url(../DICE/images/cloud.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 110, 241, 51))
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Times New Roman\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.upload)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 200, 241, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Times New Roman\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.download)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "UserHome"))
        self.pushButton.setText(_translate("Dialog", "Image Upload"))
        self.pushButton_2.setText(_translate("Dialog", "Image Download"))


'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_UserHome()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())'''

