#cria banco/tabela
#Tipo quando você precisar guardar fichas de pessoas numa gaveta, você precisa criar a gaveta e definir o modelo da ficha, os campos que ela vai ter. É isso que esse arquivo faz, espero ter ajudado...

import sqlite3 #Importa a ferramenta para falar com o banco de dados
conn = sqlite3.connect('banco.db') #cria/abre o arquivo com esse nome entre aspas no seu pc
cursor = conn.cursor() #cursor é a caneta que você usa pra escrever no banco

cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               nome TEXT NOT NULL, 
               email TEXT NOT NULL UNIQUE, 
               senha TEXT NOT NULL, 
               data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP)''')
#id integer primary key autoincrement = gera automaticamente o numero unico de cada pessoa
#nome text not null = nome obrigatorio
#email not null unique = email obrigatorio e nao pode repetir
#senha text not null = é pq a senha é obrigatoria ta?
#data_criação = a data é preenchida automaticamente quando você cria alguma "ficha", de quando ela foi guardada

conn.commit()#"salva" as alterações no banco
conn.close() #fecha a conexão, tipo fecha o arquivo

print("Banco de dados e Tabla criados!")