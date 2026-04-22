#aqui seria tipo "LER TODAS AS FICHAS DA GAVETAAAA"
#essas três linhas abaixo já foram explicadas nos dois arquivod anteriores - db e insert
import sqlite3
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM usuarios") #SELECT * é tipo dizer "Me traz todas as colunas"
usuarios = cursor.fetchall() #fetchall pega todos os resultados de uma vez

for user in usuarios: #para cada usuario econtrado
    print(user)

conn.close()#fecha a conexão ner
