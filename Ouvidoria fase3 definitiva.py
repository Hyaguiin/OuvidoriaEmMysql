class Conexao:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='OuvidoriaSQL',
        )
        self.cursor = self.connection.cursor()