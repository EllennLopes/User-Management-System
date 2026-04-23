# UMS - Sistema de Usuários

Meu primeiro projeto com banco de dados! Um sistema de cadastro 
de usuários usando Python, Flask e SQLite, dá pra criar, listar, 
editar e deletar usuários. Feito do zero enquanto aprendia SQL e 
como APIs funcionam.

## O que cada arquivo faz

- **db.py** — cria o banco de dados e a tabela de usuários
- **insert.py** — insere um usuário manualmente (usado pra testar)
- **update.py** — atualiza o nome de um usuário pelo id
- **delete.py** — deleta um usuário pelo id
- **usuarios_db.py** — lista todos os usuários no terminal
- **app.py** — a API em si, fica rodando e responde as requisições

## Observação

Cada arquivo tem comentários explicando o que cada parte do 
código faz, escrevi do meu jeito pra fixar melhor o que aprendi.

## Tecnologias usadas

- Python
- Flask
- SQLite

## Próximos passos

- [x] Adicionar hash de senha com werkzeug
- [x] Criar endpoint de login
- [ ] Integrar com o frontend que estou desenvolvendo no Figma
