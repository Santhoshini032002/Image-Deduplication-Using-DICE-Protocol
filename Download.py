from DBConnection import DBConnection
from PyQt5 import QtCore, QtGui, QtWidgets
from Decrypt import decrypt
import PIL.Image
class Ui_Download(object):

    def __init__(self,unm):
        self.unm=unm

    def getFilelist(self):
        try:
            database = DBConnection.getConnection()
            cursor = database.cursor()
            cursor.execute("select imgid,imgnm from files where unm='" + self.unm + "'")
            records = cursor.fetchall()
            for row in records:
                self.comboBox.addItem(str(row[0]) + "  -->  " + str(row[1]))

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
    def download(self):

        file=self.comboBox.currentText()
        fd=file.split("  -->  ")
        imgid=fd[0]
        imgnm=fd[1]
        print("imgd=",imgid)
        print("imgnm=",imgnm)
        decrypt(imgid,imgnm)
        self.showMessageBox("Download", "Image Decrypt and Download Successfully")
        img = PIL.Image.open("output.jpg")
        img.show()


    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(503, 366)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(170, 80, 181, 41))
        self.comboBox.setStyleSheet("color: rgb(85, 170, 127);\n"
"font: 75 12pt \"Verdana\";")
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 42, 151, 31))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Verdana\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 170, 211, 41))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 85, 0);\n"
"font: 75 11pt \"Verdana\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.download)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Download"))
        self.label.setText(_translate("Dialog", "Select File"))
        self.pushButton.setText(_translate("Dialog", "Decrypt and Download"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Download("a")
    ui.setupUi(Dialog)
    ui.getFilelist()
    Dialog.show()
    sys.exit(app.exec_())
