import sqlite3

class Model():

    def conecta_banco(self):
        try:
            self.conn = sqlite3.connect('Model/minha_conexao.db')
            return self.conn
        except:
            print('Conexão Caiu')

    def cadastra_cliente(self, nome, endereco, telefone, cpf, plano_saude, numero_plano):
        self.conecta_banco()
        self.cursor = self.conn.cursor()
        self.cursor.execute(""" INSERT INTO cliente (nome, endereco, telefone,cpf,plano_saude,numero_plano) VALUES ((?),(?),(?),(?),(?),(?));""", (nome, endereco, telefone, cpf, plano_saude, numero_plano))
        self.conn.commit()



    def busca_cpf_cadastrar_consulta(self, cpf):
        query = 'select * from cliente where cpf = "'+cpf+'";'
        self.conecta_banco()
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        return self.cursor

    def cadastra_consulta(self, id_cliente, data_consulta, dentista):
        query = 'INSERT INTO consulta (fk_cliente, data_consulta, dentista) VALUES ('+str(id_cliente)+',"'+str(data_consulta)+'","'+dentista+'");'
        self.conecta_banco()
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        self.conn.commit()
