import mysql.connector
class Conexao:
    def __init__(self):
        self.codigo_geral = 0
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='OuvidoriaSQL',

        )
        self.cursor = self.connection.cursor()

    def registrar_ocorrencia(self):
        self.cursor = self.connection.cursor()
        sql = 'INSERT INTO OcorrenciaSQL(tipo, titulo, descricao ) VALUES( %s, %s, %s)'
        data = ('tipo', input(), input())
        self.codigo_geral += 1
        self.cursor.execute(sql, data)
        self.connection.commit()
        userid = self.cursor.lastrowid

        print(userid,'Ocorrência cadastrada com sucesso! Código:', self.codigo_geral)


    def deletar_ocorrencia(self,id):
        sql = 'DELETE from ocorrencias where id=%s'
        data = (id,)

        self.cursor.execute(sql, data)
        self.connection.commit()

        recordAffect = self.cursor.rowcount

        return recordAffect

    def close_conexao(self):
            self.cursor.close()
            self.connection.close()




