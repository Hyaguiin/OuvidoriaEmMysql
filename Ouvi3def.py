import mysql.connector
from time import sleep

class Conexao:
    def __init__(self):
        self.codigo_geral = 0
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='dbz123456789',
            database='OcorrenciaSQL',
        )
        self.cursor = self.connection.cursor()

    @staticmethod
    def tempo():
        for c in range(3):
            print('*')
            sleep(0.2)


    def listar_ocorrencia(self):
        sql = 'SELECT * FROM OcorrenciaSQL'
        self.cursor.execute(sql)
        lista_ocorrencias = self.cursor.fetchall()
        
        return lista_ocorrencias

    def registrar_ocorrencia_elogio(self):
        self.cursor = self.connection.cursor()
        sql = 'INSERT INTO OcorrenciaSQL(tipo, titulo, descricao ) VALUES( %s, %s, %s)'
        self.titulo = input('Titulo: ')
        self.descicao = input('Descricao: ')
        data = ('Elogio', self.titulo, self.descicao)
        self.codigo_geral += 1
        self.cursor.execute(sql, data)
        self.connection.commit()
        userid = self.cursor.lastrowid

        print('Ocorrência cadastrada com sucesso! Código: ',userid)

    def registrar_ocorrencia_reclamacao(self):
        self.cursor = self.connection.cursor()
        sql = 'INSERT INTO OcorrenciaSQL(tipo, titulo, descricao ) VALUES( %s, %s, %s)'
        self.titulo = input('Titulo: ')
        self.descicao = input('Descricao: ')
        data = ('Reclamação', self.titulo, self.descicao)
        self.codigo_geral += 1
        self.cursor.execute(sql, data)
        self.connection.commit()
        userid = self.cursor.lastrowid

        print('Ocorrência cadastrada com sucesso! Código: ',userid)

    def registrar_ocorrencia_sugestao(self):
        self.cursor = self.connection.cursor()
        sql = 'INSERT INTO OcorrenciaSQL(tipo, titulo, descricao ) VALUES( %s, %s, %s)'
        self.titulo = input('Titulo: ')
        self.descicao = input('Descricao: ')
        data = ('Sugestão', self.titulo, self.descicao)
        self.codigo_geral += 1

        self.cursor.execute(sql, data)
        self.connection.commit()
        userid = self.cursor.lastrowid

        print('Ocorrência cadastrada com sucesso! Código: ',userid)

    def deletar_ocorrencia(self,id):
        sql = 'DELETE from OcorrenciaSQL where id=%s'
        data = (id,)

        self.cursor.execute(sql, data)
        self.connection.commit()

        recordAffect = self.cursor.rowcount

        return recordAffect
    
    def pesquisar_ocorrencia(self, id):
        sql = 'SELECT * from OcorrenciaSQL where id=%s'
        data= (id, )

        self.cursor.execute(sql,data)
        lista_ocorrencia = self.cursor.fetchall()
        for ele in lista_ocorrencia:
                print(ele[1])
                print(f'Titulo: {ele[2]}')
                print(f'Descrição: {ele[3]}')
        return lista_ocorrencia

    def close_conexao(self):
        self.cursor.close()
        self.connection.close()

