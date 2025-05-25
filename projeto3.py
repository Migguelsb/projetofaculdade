from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(591, 621)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cabecalho = QtWidgets.QLabel(self.centralwidget)
        self.cabecalho.setGeometry(QtCore.QRect(-60, -10, 711, 131))
        self.cabecalho.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.cabecalho.setObjectName("cabecalho")
        self.label_valor = QtWidgets.QLabel(self.centralwidget)
        self.label_valor.setGeometry(QtCore.QRect(40, 240, 81, 20))
        self.label_valor.setObjectName("label_valor")
        self.label_desc = QtWidgets.QLabel(self.centralwidget)
        self.label_desc.setGeometry(QtCore.QRect(150, 240, 111, 21))
        self.label_desc.setObjectName("label_desc")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(410, 240, 131, 71))
        self.btn_add.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.btn_add.setObjectName("btn_add")
        self.escrever_valor = QtWidgets.QLineEdit(self.centralwidget)
        self.escrever_valor.setGeometry(QtCore.QRect(10, 270, 113, 20))
        self.escrever_valor.setObjectName("escrever_valor")
        self.escrever_desc = QtWidgets.QLineEdit(self.centralwidget)
        self.escrever_desc.setGeometry(QtCore.QRect(140, 270, 113, 20))
        self.escrever_desc.setObjectName("escrever_desc")
        self.check_entrada = QtWidgets.QCheckBox(self.centralwidget)
        self.check_entrada.setGeometry(QtCore.QRect(420, 220, 70, 17))
        self.check_entrada.setStyleSheet("color: rgb(0, 255, 127);\n"
"color: rgb(0, 170, 0);")
        self.check_entrada.setObjectName("check_entrada")
        self.check_saida = QtWidgets.QCheckBox(self.centralwidget)
        self.check_saida.setGeometry(QtCore.QRect(490, 220, 70, 17))
        self.check_saida.setStyleSheet("color: rgb(255, 0, 0);")
        self.check_saida.setObjectName("check_saida")
        self.tbl_entradas = QtWidgets.QTextBrowser(self.centralwidget)
        self.tbl_entradas.setGeometry(QtCore.QRect(10, 100, 161, 91))
        self.tbl_entradas.setObjectName("tbl_entradas")
        self.tbl_saida = QtWidgets.QTextBrowser(self.centralwidget)
        self.tbl_saida.setGeometry(QtCore.QRect(210, 100, 161, 91))
        self.tbl_saida.setObjectName("tbl_saida")
        self.tbl_total = QtWidgets.QTextBrowser(self.centralwidget)
        self.tbl_total.setGeometry(QtCore.QRect(400, 100, 161, 91))
        self.tbl_total.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.tbl_total.setObjectName("tbl_total")
        self.tbl_financas = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl_financas.setGeometry(QtCore.QRect(50, 370, 501, 231))
        self.tbl_financas.setObjectName("tbl_financas")
        self.tbl_financas.setColumnCount(5)
        self.tbl_financas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_financas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_financas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_financas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_financas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_financas.setHorizontalHeaderItem(4, item)
        self.label_data = QtWidgets.QLabel(self.centralwidget)
        self.label_data.setGeometry(QtCore.QRect(300, 240, 71, 21))
        self.label_data.setObjectName("label_data")
        self.editar_data = QtWidgets.QDateEdit(self.centralwidget)
        self.editar_data.setGeometry(QtCore.QRect(270, 270, 110, 22))
        self.editar_data.setObjectName("editar_data")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cabecalho.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">TO NO AZUL</span></p></body></html>"))
        self.label_valor.setText(_translate("MainWindow", "VALOR"))
        self.label_desc.setText(_translate("MainWindow", "DESCRIÇÃO"))
        self.btn_add.setText(_translate("MainWindow", "ADICIONAR"))
        self.escrever_valor.setPlaceholderText(_translate("MainWindow", "Digite o valor:"))
        self.escrever_desc.setPlaceholderText(_translate("MainWindow", "Digite a descrição:"))
        self.check_entrada.setText(_translate("MainWindow", "Entrada"))
        self.check_saida.setText(_translate("MainWindow", "Saída"))
        self.tbl_entradas.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600;\"> Entradas</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#00ff00;\">       </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#00ff00;\">            00.00</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:600; color:#00ff00;\"><br /></p></body></html>"))
        self.tbl_saida.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600;\">   Saídas</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#00ff00;\">       </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#00ff00;\">            </span><span style=\" font-size:9pt; font-weight:600; color:#ff0000;\">00.00</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:600; color:#00ff00;\"><br /></p></body></html>"))
        self.tbl_total.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600;\">    Total</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#00ff00;\">      </span><span style=\" font-size:9pt; font-weight:600; color:#000000;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#000000;\">             00.00</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:600; color:#00ff00;\"><br /></p></body></html>"))
        item = self.tbl_financas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tbl_financas.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Valor"))
        item = self.tbl_financas.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Descrição"))
        item = self.tbl_financas.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Data"))
        item = self.tbl_financas.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Fluxo"))
        self.label_data.setText(_translate("MainWindow", "DATA"))

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
