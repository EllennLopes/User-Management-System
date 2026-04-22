#A gaveta já existe (arquivo db), agora é so colocar uma ficha dentro (inserir usuário) 
import sqlite3 #conector para o banco
conn = sqlite3.connect('banco.db') #vai abrir ou criar o arquivo com o nome entre aspas, já temos esse arquivo
cursor = conn.cursor() #caneta lembra?

cursor.execute(''' INSERT INTO usuarios (nome, email, senha) VALUES(?, ? ,?)''', ("Paula Rejane", "Parejane@email.com", "1234"))
# "?" são os espaços em branco na ficha
#você passa os valores que quiser (paula rejane etc etc, por exemplo), o slite pega os valores da tupla na ordem em que você escreveu incialmente(nome,email,senha) e troca pelo "?"

conn.close() #echar a conexão né amore?

print("Usuário inserido!")