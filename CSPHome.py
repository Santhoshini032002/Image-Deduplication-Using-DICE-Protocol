
from PyQt5 import QtCore, QtGui, QtWidgets
from StorageFiles import Ui_StorageFiles
from Graph import plotview
class Ui_CSPHome(object):

    def imagefiles(self):
        self.storage = QtWidgets.QDialog()
        self.ui = Ui_StorageFiles()
        self.ui.setupUi(self.storage)
        self.ui.clouddata()
        self.storage.show()
    def graphs(self):
        plotview()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(641, 403)
        Dialog.setStyleSheet("background-color: rgb(170, 170, 0);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 100, 251, 51))
        self.pushButton.setStyleSheet("font: 12pt \"Franklin Gothic Demi\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.imagefiles)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 220, 251, 51))
        self.pushButton_2.setStyleSheet("font: 12pt \"Franklin Gothic Demi\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.graphs)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CSP Home"))
        self.pushButton.setText(_translate("Dialog", "Storage Files"))
        self.pushButton_2.setText(_translate("Dialog", "Graph"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_CSPHome()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
