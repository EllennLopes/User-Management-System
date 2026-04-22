# deleta usuarios ou JOGAR A FICHA FORA HAHAHAHAHA - to coringando po, perdão

import sqlite3
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

#WHERE id = 1 (dai vai só apagar o usuário com id 1, se n botar o WHERE vai apagar tudo)
cursor.execute(''' DELETE FROM usuarios WHERE id = ? ''', (1,))


conn.commit()
conn.close()