import mysql.connector
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QMainWindow, QTableWidgetItem
from projeto3 import Ui_MainWindow  # Sua tela principal
from login2 import Ui_Dialog  # Sua tela de login
import sys

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="controle_financeiro"
    )

class Telaprincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Tela principal")
        
        # Conecta os botões (MANTIDO SEU CÓDIGO ORIGINAL)
        self.ui.btn_add.clicked.connect(self.adicionar_transacao)
        self.carregar_dados_tabela()

    def adicionar_transacao(self):
        valor = self.ui.escrever_valor.text()
        descricao = self.ui.escrever_desc.text()
        data = self.ui.editar_data.date().toString("yyyy-MM-dd")

        if self.ui.check_entrada.isChecked() and not self.ui.check_saida.isChecked():
            fluxo = 1
        elif self.ui.check_saida.isChecked() and not self.ui.check_entrada.isChecked():
            fluxo = 0
        else:
            QMessageBox.warning(self, "Aviso", "Selecione apenas um tipo de transação!")
            return

        try:
            conn = conectar_banco()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tbl_financeiro (valor_transacao, desc_transacao, dt_transacao, fluxo_transacao) VALUES (%s, %s, %s, %s)",
                (valor, descricao, data, fluxo)
            )
            conn.commit()
            QMessageBox.information(self, "Sucesso", "Transação adicionada!")
            self.carregar_dados_tabela()

        except mysql.connector.Error as erro:
            QMessageBox.critical(self, "Erro", f"Erro no banco:\n{erro}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def carregar_dados_tabela(self):
        try:
            conn = conectar_banco()
            cursor = conn.cursor()
            cursor.execute("SELECT id_transacao, valor_transacao, desc_transacao, dt_transacao, fluxo_transacao FROM tbl_financeiro")
            
            self.ui.tbl_financas.setRowCount(0)
            
            for row_num, row_data in enumerate(cursor.fetchall()):
                self.ui.tbl_financas.insertRow(row_num)
                for col_num, data in enumerate(row_data):
                    self.ui.tbl_financas.setItem(row_num, col_num, QTableWidgetItem(str(data)))
                    
        except mysql.connector.Error as erro:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar dados:\n{erro}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

class Login(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login)
        self.setWindowTitle("Tela de Login")

    def login(self):
        # MANTIDO SEU CÓDIGO ORIGINAL DE LOGIN/CADASTRO
        nome = self.ui.lineEdit_3.text()
        email = self.ui.lineEdit.text()
        senha = self.ui.lineEdit_2.text()
        cpf = self.ui.lineEdit_4.text()

        try:
            conn = conectar_banco()
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM tbl_usuarios WHERE email_usuario = %s AND senha_usuario = %s", (email, senha))
            resultado = cursor.fetchone()

            if resultado:
                QMessageBox.information(self, "Login realizado", "Usuário autenticado com sucesso!")
                self.abrir_principal()
            else:
                cursor.execute(
                    "INSERT INTO tbl_usuarios (nome_usuario, email_usuario, senha_usuario, cpf_usuario) VALUES (%s, %s, %s, %s)",
                    (nome, email, senha, cpf)
                )
                conn.commit()
                QMessageBox.information(self, "Cadastro feito", "Novo usuário criado com sucesso!")
                self.abrir_principal()

        except mysql.connector.Error as erro:
            QMessageBox.critical(self, "Erro de conexão", f"Erro ao conectar no banco:\n{erro}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def abrir_principal(self):
        self.tela_principal = Telaprincipal()
        self.tela_principal.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # GARANTE QUE SÓ O LOGIN APARECE PRIMEIRO
    login = Login()
    login.show()
    
    sys.exit(app.exec_())