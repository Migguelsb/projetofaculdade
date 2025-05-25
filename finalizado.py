import mysql.connector
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QMainWindow, QTableWidgetItem
from projeto3 import Ui_MainWindow
from login2 import Ui_Dialog
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
        # Conecta o botão à função
        self.ui.btn_add.clicked.connect(self.adicionar_transacao)

        # Carrega os dados iniciais na tabela e saldos
        self.carregar_dados_tabela()
        self.atualizar_saldos()

    def adicionar_transacao(self):
        valor = self.ui.escrever_valor.text()
        descricao = self.ui.escrever_desc.text()
        data = self.ui.editar_data.date().toString("yyyy-MM-dd")

        if self.ui.check_entrada.isChecked() and not self.ui.check_saida.isChecked():
            fluxo = 1
        elif self.ui.check_saida.isChecked() and not self.ui.check_entrada.isChecked():
            fluxo = 0
        else:
            QMessageBox.warning(self, "Aviso", "Selecione apenas um tipo de transação (Entrada ou Saída).")
            return

        try:
            conn = conectar_banco()
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO tbl_financeiro (valor_transacao, desc_transacao, dt_transacao, fluxo_transacao) VALUES (%s, %s, %s, %s)",
                (valor, descricao, data, fluxo)
            )
            conn.commit()
            QMessageBox.information(self, "Sucesso", "Item adicionado com sucesso!")

            self.carregar_dados_tabela()
            self.atualizar_saldos()

        except mysql.connector.Error as erro:
            QMessageBox.critical(self, "Erro de conexão", f"Erro ao conectar no banco:\n{erro}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def carregar_dados_tabela(self):
        try:
            conn = conectar_banco()
            cursor = conn.cursor()
            cursor.execute("SELECT id_transacao, valor_transacao, desc_transacao, dt_transacao, fluxo_transacao FROM tbl_financeiro")
            resultados = cursor.fetchall()

            self.ui.tbl_financas.setRowCount(0)

            for row_number, row_data in enumerate(resultados):
                self.ui.tbl_financas.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tbl_financas.setItem(row_number, column_number, QTableWidgetItem(str(data)))

            self.atualizar_saldos()

        except mysql.connector.Error as erro:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar dados:\n{erro}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def atualizar_saldos(self):
        try:
            conn = conectar_banco()
            cursor = conn.cursor()

            cursor.execute("SELECT SUM(valor_transacao) FROM tbl_financeiro WHERE fluxo_transacao = 1")
            total_entrada = cursor.fetchone()[0] or 0

            cursor.execute("SELECT SUM(valor_transacao) FROM tbl_financeiro WHERE fluxo_transacao = 0")
            total_saida = cursor.fetchone()[0] or 0

            total_geral = total_entrada - total_saida

            # Atualiza os valores e cores para entrada, saída e total
            self.ui.tbl_entradas.setText(f"Entrada:   R$ {total_entrada:.2f}")
            self.ui.tbl_entradas.setStyleSheet("color: green; font-size: 18px; font-weight: bold;")  
            self.ui.tbl_saida.setText(f"Saída:     R$ {total_saida:.2f}")
            self.ui.tbl_saida.setStyleSheet("color: red; font-size: 18px; font-weight: bold;")  

            self.ui.tbl_total.setText(f"Total:   R$ {total_geral:.2f}")
            self.ui.tbl_total.setStyleSheet("color: navy; font-size: 18px; font-weight: bold;")  
        except mysql.connector.Error as erro:
            QMessageBox.critical(self, "Erro", f"Erro ao atualizar saldos:\n{erro}")
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
                self.tela_principal = Telaprincipal()
                self.tela_principal.show()
                self.close()
            else:
                
                cursor.execute(
                    "INSERT INTO tbl_usuarios (nome_usuario, email_usuario, senha_usuario, cpf_usuario) VALUES (%s, %s, %s, %s)",
                    (nome, email, senha, cpf)
                )
                conn.commit()
                QMessageBox.information(self, "Cadastro feito", "Novo usuário criado com sucesso!")
                self.tela_principal = Telaprincipal()
                self.tela_principal.show()
                self.close()

        except mysql.connector.Error as erro:
            QMessageBox.critical(self, "Erro de conexão", f"Erro ao conectar no banco:\n{erro}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# inicio
app = QApplication(sys.argv)
window = Login()
window.show()
sys.exit(app.exec_())
