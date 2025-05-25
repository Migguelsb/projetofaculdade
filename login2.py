
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(299, 300)
        Dialog.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 110, 41, 41))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 8pt \"Sitka Subheading Semibold\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 160, 41, 21))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 8pt \"Sitka Subheading Semibold\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 220, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 280, 47, 13))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 120, 131, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 160, 131, 21))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 40, 131, 21))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 30, 41, 41))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 8pt \"Sitka Subheading Semibold\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 70, 41, 41))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 8pt \"Sitka Subheading Semibold\";")
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 80, 131, 21))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "E-mail"))
        self.label_2.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:22pt;\">SENHA</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Senha"))
        self.pushButton.setText(_translate("Dialog", "ENTRAR"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Digite seu E-mail:"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Digite sua senha:"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Digite seu nome:"))
        self.label_4.setText(_translate("Dialog", "Nome"))
        self.label_5.setText(_translate("Dialog", "CPF"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "Digite seu CPF:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
