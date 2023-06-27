import mysql.connector

class Conexao:
        def __init__(self):
            self.connection = mysql.connector.connect(
                host='localhost',
                user='Ouvidoria',
                password='ouvidoria',
                database='ouvidoria',
            )
            self.cursor = self.connection.cursor()

        def listar_usuarios(self):
            sql='SELECT * FROM usuarios'

            self.cursor.execute(sql)
            lista_usuario= self.cursor.fetchall()

            return lista_usuario

        def cadastrar_usuario(self, nome, usuario, senha):
                sql='INSERT INTO usuarios(nome, usuario, senha) VALUES (%s,%s,%s)'
                data=(nome, usuario, senha)

                self.cursor.execute(sql, data)
                self.connection.commit()

                userId = self.cursor.lastrowid
                return userId

        def deletar_usuario(self, id):
            sql='DELETE from usuarios where id=%s'
            data=(id,)

            self.cursor.execute(sql,data)
            self.connection.commit()

            recordAffect = self.cursor.rowcount

            return recordAffect

        def atualizar_usuario(self, nome, usuario, id):
            sql = 'UPDATE usuarios set nome=%s, usuario=%s where id=%s'
            data = (nome, usuario, id)

            self.cursor.execute(sql, data)
            self.connection.commit()

            lista_afetada = self.cursor.rowcount

            return lista_afetada

        def close_conexao(self):
            self.cursor.close()
            self.connection.close()


conexao = Conexao()

lista_usuarios = conexao.listar_usuarios()
for usuario in lista_usuarios:
        print(usuario)
        print(usuario[0], usuario[1])

conexao.close_conexao()