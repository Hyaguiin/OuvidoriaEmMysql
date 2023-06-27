import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'dbz123456789',
    database = 'OcorrenciaSQL'

)

cursor = conexao.cursor()

sql = 'INSERT INTO OcorrenciaSQL(tipo, titulo, descricao ) VALUES( %s, %s, %s)'
data = ('Reclamacao', 'ODEIO VOCES!', 'Vocês conseguiram EXPLODIR um banco de dados!')

cursor.execute(sql, data)
conexao.commit()
userid = cursor.lastrowid

print('ID da nova Ocorrência:', userid)
