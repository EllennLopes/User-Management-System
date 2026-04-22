#Aqui seria tipo, o balcão de atendimento, esse aq fica rodando o tempo esperando alguém chamar, é a vossa API

from flask import Flask, request, jsonify
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

#As "?" vão ser substituídas na sequência em que você escreveu (nome, email,senha)
    cursor.execute('''INSERT INTO usuarios (nome, email, senha) VALUES (?, ? ,?)''', (dados['nome'], dados['email'], dados['senha']))
    
    conn.commit()
    conn.close()

    return{"mensagem": "Usuário Criado!"}
    
app.run(debug=True)