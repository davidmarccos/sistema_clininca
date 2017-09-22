from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Views.DialogCadastrar import Ui_DialogCadastrar
from Views.DialogCadastrarConsulta import Ui_DialogCadastrarConsulta
from Model.Model import *


class ControllerView(object):
    def __init__(self):

        self.frm_cadastrar_cliente = QtWidgets.QMainWindow()
        self.frm_cadastrar_consulta = QtWidgets.QMainWindow()
        self.message_box = QMessageBox()
        self.model = Model()
        self.ui_cadastrar_cliente = Ui_DialogCadastrar()
        self.ui_cadastrar_consulta = Ui_DialogCadastrarConsulta()

    # Método é chamado na janela principal do Main.py
    def chamar_cadastro_cliente(self):
        self.ui_cadastrar_cliente.setupUi(self.frm_cadastrar_cliente)
        self.frm_cadastrar_cliente.show()

        # Eventos da Janela Cadastro Cliente
        self.ui_cadastrar_cliente.btn_cadastrar.clicked.connect(self.action_cadastrar_cliente)
        self.ui_cadastrar_cliente.btn_cancelar.clicked.connect(lambda: self.frm_cadastrar_cliente.close())

    # Método é chamado na janela principal do Main.py
    def chamar_cadastro_consulta(self):
        self.ui_cadastrar_consulta.setupUi(self.frm_cadastrar_consulta)
        self.frm_cadastrar_consulta.show()

        # Eventos da Janela Cadastro Consulta
        self.ui_cadastrar_consulta.btn_cancelar.clicked.connect(lambda: self.frm_cadastrar_consulta.close())
        self.ui_cadastrar_consulta.btn_buscar_cpf.clicked.connect(self.action_buscar_cpf_consulta)
        self.ui_cadastrar_consulta.btn_cadastrar.clicked.connect(self.action_cadastrar_consulta)

    #Metodo que conecta no DB e cadastra os clientes
    def action_cadastrar_cliente(self):

        try:

            if not (self.ui_cadastrar_cliente.txt_nome.text() == '' or self.ui_cadastrar_cliente.txt_telefone.text() == '()-' or self.ui_cadastrar_cliente.txt_cpf.text() == '..-' or (self.ui_cadastrar_cliente.txt_plano_saude.text() == '' or self.ui_cadastrar_cliente.txt_numero_plano.text()) == ''):

                self.model.cadastra_cliente(str(self.ui_cadastrar_cliente.txt_nome.text()),
                                            str(self.ui_cadastrar_cliente.txt_endereco.text()),
                                            str(self.ui_cadastrar_cliente.txt_telefone.text()),
                                            str(self.ui_cadastrar_cliente.txt_cpf.text()),
                                            str(self.ui_cadastrar_cliente.txt_plano_saude.text()),
                                            int(self.ui_cadastrar_cliente.txt_numero_plano.text()))

                self.message_box.about(self.frm_cadastrar_cliente, 'Sucesso',"Cliente cadastrado com sucesso!")

                self.ui_cadastrar_cliente.txt_nome.setText("")
                self.ui_cadastrar_cliente.txt_endereco.setText("")
                self.ui_cadastrar_cliente.txt_cpf.setText("")
                self.ui_cadastrar_cliente.txt_telefone.setText("")
                self.ui_cadastrar_cliente.txt_numero_plano.setText("")
                self.ui_cadastrar_cliente.txt_plano_saude.setText("")

            else:
                self.message_box.warning(self.frm_cadastrar_cliente, 'Error', "Campo não preenchido")
        except:
            print('Deu Erro!')
            self.message_box.warning(self.frm_cadastrar_cliente,'Error', "ERROR!")


    def action_buscar_cpf_consulta(self):

        self.model.busca_cpf_cadastrar_consulta(str(self.ui_cadastrar_consulta.txt_cpf.text()))
        data = self.ui_cadastrar_consulta.calendarConsulta.selectedDate().toPyDate()

        if(len(self.model.cursor.fetchall()) > 0):

            self.model.busca_cpf_cadastrar_consulta(str(self.ui_cadastrar_consulta.txt_cpf.text()))
            for linha in self.model.cursor.fetchall():
                self.ui_cadastrar_consulta.txt_nome.setText(linha[1])
                self.ui_cadastrar_consulta.txt_plano_saude.setText(linha[5])
                self.ui_cadastrar_consulta.txt_numero_plano.setText(str(linha[6]))
                self.id = linha[0]
                return self.id



        else:
            self.message_box.warning(self.frm_cadastrar_consulta, 'Error', 'CPF NÃO ENCONTRADO!')



    def action_cadastrar_consulta(self):
        self.model.cadastra_consulta(self.id,self.ui_cadastrar_consulta.calendarConsulta.selectedDate().toPyDate(),self.ui_cadastrar_consulta.txt_Dentista.text())