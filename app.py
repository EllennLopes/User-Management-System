#Aqui seria tipo, o balcão de atendimento, esse aq fica rodando o tempo esperando alguém chamar, é a vossa API

from flask import Flask, render_template, request, redirect, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
        #generate_password_hash = a fofoqueira que transforma "entupi o vaso" em "pizza de abacaxi com banana".... referências vc só vai entender se ler o arquivo https://github.com/EllennLopes/User-Management-System/blob/main/Informa%C3%A7%C3%B5es%20que%20aprendi%20sobre%20Hash.txt
        # check_password_hash = a parte do código que pergunta para a fofoqueira "ei, a pizza bate?" 

import sqlite3

app = Flask(__name__) #vai criar o servidor

def conectar():
    return sqlite3.connect('banco.db')

#O GET é tipo dizer "me mostra essas fichas(usuários) ae", e o POST é enviar, tipo "cria esse usuário aqui"
#Aqui vai listar os usuário, "mostrar as fichas"
@app.route('/usuarios', methods=['GET']) #quando alguém acessar os usuários 
def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios") #select são as colunas
    dados = cursor.fetchall() #fetchall pega todos os resultados de uma vez

    conn.close()
    return jsonify(dados) #jsonify transforma o resultado em JSON para mandar pro navegador

#criar usuario
@app.route('/usuarios', methods=['POST']) #quando alguém enviar dados com o POST
def criar_usuario():
    dados = request.json  #pega o JSON que veio no corpo da requisição

    conn = conectar()
    cursor = conn.cursor()

    senha_hash = generate_password_hash(dados['senha'])
    #entrega a senha para a fofoqueira ANTES DE GUARDAR NO BANCO PLMDS


    cursor.execute('''INSERT INTO usuarios (nome, email, senha) VALUES (?, ? ,?)''', (dados['nome'], dados['email'], senha_hash))
    #As "?" vão ser substituídas na sequência em que você escreveu (nome, email,senha)
    # Repara que passamos senha_hash aqui, e não dados['senha'] diretamente

    conn.commit()
    conn.close()
 
    return{"mensagem": "Usuário Criado!"}
    
#login via formulário HTML (porta da frente da casa)
@app.route('/login', methods=['GET', 'POST'])
def login_form():
    if request.method =='POST': #se a pessoa bate na porta com POST
        email = request.form['username'] #pega o email que a pessoa digitou no formulário
        senha = request.form['password'] #faz a mesma coisa, só que com a senha

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT senha FROM usuarios WHERE email = ?")
        resultado = cursor.fetchone() #o tio do banco procura se tem ficha com esse email
        conn.close()

        if resultado is None: #se não tem nenhuma ficha com esse email
            return {"mensagem": "Usuário não encontrado"}, 404
        senha_do_banco = resultado[0] #pega a senha guardada na ficha
        
        #a fofoqueira compara se a senha que você digitou vira a mesma pizza que tá guardada
        if check_password_hash(senha_do_banco, senha):
            return redirect("dashboard") #se sim, abre o portão e manda pra sala principal
        else:
            return {"mensagem": "Senha incorreta"}, 401
#se a pessoa veio só visistar (GET), mostra a pagina de login bonitinha
    return render_template("login.html")

#login via API JSON (porta dos fundos, usada por outros sistemas)
@app.route('/api/login', methods=['POST']) #quando alguém tentar entrar no sistema
def login_api():
    dados = request.json #pega o email e senha que vieram no corpo da requisição
    email = dados['email']
    senha = dados['senha']

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT senha FROM usuarios WHERE email = ?", (email,))
    resultado = cursor.fetchone() #fetchone pega só um resultado, até pq só tem um email igual né
    conn.close()

    if resultado is None: #se não achou o email no banco
        return{"mensagem": "Usuário não encontrado"}, 404
    #404 é o código HTTP de "não encontrado"

    senha_do_banco = resultado[0] #pega a pizza de abacaxi que tá guardada no banco

    if check_password_hash(senha_do_banco, dados['senha']):
        #pergunta pra fofoqueira se a senha que o usuário digitou vai virar a msm pizza de abacaxi e não uma diferente
        #se a pizza for a certa, o acesso é liberado
        return{"mensagem": "Login realizado!"}
    else:
        return {"mensagem": "Senha incorreta"}, 401
    #caso a fofoqueira disser "pizza portuguesa ou de frango", nega o acesso, NEGA!
    #401 é o código de HTTP de "não autorizado"

if __name__ == '__main__':
    app.run(debug=True)
#agora o app.run ta dentro do if __name__ -- '__main__'
#isso evita problemas quando o Flask é iniciado por um servidor externo


