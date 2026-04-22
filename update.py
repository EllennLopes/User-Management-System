#Vai corrigir uma ficha(atualizar usuário)
#Essas três linhas... já sabe (CONECTOR DO BANCO DE DADOS, ABRIR O BANCO, E ESCREVER NELE)
import sqlite3
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

cursor.execute(''' UPDATE usuarios SET nome = ? WHERE id = ?''', ("Novo Nome Atualizado", 1))
# SET nome = ? (vai mudar o nome né?)
#WHERE id = ? (o registro que vai ser alterado, uma fichazinha por favorrrr, se n tiver o WHERE vai mudar tudo migs)

conn.commit()#salvar
conn.close()#fechar conexão

print("Usuário Atualizado!")
