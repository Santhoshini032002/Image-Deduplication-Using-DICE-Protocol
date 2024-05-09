from PIL import Image
import image_slicer
import glob
import sys
from mysql.connector import MySQLConnection, Error
import mysql.connector
from DBConnection import DBConnection
from Hashlib import Hashlib
import os
from AES import AES
import numpy as np
import base64
from PyQt5 import QtCore, QtGui, QtWidgets

class Upload(object):

    def __init__(self,unm,Dialog):
        self.unm=unm
        self.dialog=Dialog

    def browse_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File")
        print(fileName)
        self.lineEdit.setText(fileName)

    def setblocks(self):
        try:
            print("unm=",self.unm)
            fileName=self.lineEdit.text()
            tiles = image_slicer.slice(fileName, 6 * 6, save=False)
            image_slicer.save_tiles(tiles, directory='./blocks')
            database = DBConnection.getConnection()
            cursor = database.cursor()
            self.showMessageBox("Information","Image split the blocks Successfully")
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def encrypt(self):
        try:


            database = DBConnection.getConnection()
            cursor = database.cursor()
            cursor.execute("select count(*) from files")
            imgid = cursor.fetchone()[0]
            print(imgid)
            id = 0
            if (imgid == 'None'):
                id = 1
            else:
                id = int(imgid) + 1

            if(id==1):
                img = []
                hash1 = []
                hash2 = []
                dict = {}
                all_files = glob.glob('./blocks/*.png')
                id1 = 0
                c=0
                hashlib = Hashlib()
                fileName = self.lineEdit.text()
                path, filename = os.path.split(fileName) # get filename only from fullpath
                imgdata = self.read_file(fileName)
                encodestring = base64.b64encode(imgdata)
                query="insert into files values(%s,%s,%s,%s)"
                values = (id, filename, encodestring,self.unm)
                cursor.execute(query,values)
                database.commit()
                for file in all_files:
                    print("file", file)
                    c = c + 1
                    if c < 6:
                        hashh = hashlib.sha256(file)
                        img.append(str(file))
                        hash1.append(str(hashh))
                    else:
                        hash = hashlib.sha256(file)
                        img.append(str(file))
                        hash1.append(str(hash))
                        id1 = id1 + 1;
                        id2 = str(id) + "." + str(id1)
                        print(id2)
                        aes = AES()  # Use AES Algorithm
                        aes.ENCRYPTT(str(id2), filename, img, hash1)  # Calling Encryption Method
                        c = 0
                        id2 = ""
                        hash1.clear()
                        img.clear()
                        self.lineEdit.setText("")
                self.showMessageBox("Message", "Image Encrypted and Uploaded Successfully")
                self.dialog.hide()
            else:
                fileName = self.lineEdit.text()
                path, filename = os.path.split(fileName)  # get filename only from fullpath
                imgdata=self.read_file(fileName)
                #imgdata=base64.b64encode(imgdata)
                #print("img=",imgdata)
                aes = AES()
                aes.ENCRYPT(id,filename,fileName,imgdata,self.unm)
                self.lineEdit.setText("")
                self.showMessageBox("Message","Image Encrypted and Uploaded Successfully")
                self.dialog.hide()




        except Exception as e:
            #print("Errr=",e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print("e=",e)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def read_file(self,filename):
        with open(filename, 'rb') as f:
            img = f.read()
        return img

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(558, 500)
        Dialog.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 80, 131, 20))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 150, 101, 20))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Verdana\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 170, 291, 31))
        self.lineEdit.setStyleSheet("font: 75 10pt \"Verdana\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(420, 170, 81, 31))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Verdana\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browse_file)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 230, 121, 31))
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Verdana\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.setblocks)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 230, 141, 31))
        self.pushButton_4.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.encrypt)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "File Upload"))
        self.label.setText(_translate("Dialog", "File Uploading"))
        self.label_2.setText(_translate("Dialog", "Select Image"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.pushButton_3.setText(_translate("Dialog", "Set Blocks"))
        self.pushButton_4.setText(_translate("Dialog", "Encrypt && Upload"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Upload(Dialog,"a")
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

