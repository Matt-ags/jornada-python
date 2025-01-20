# Importante, quando nos estamos "criando uma aplicação", temos que pensar como ela vai ser, e escrever tipo as telas sabe? assim:

# Hashzap
# botao de iniciar chat
# popup para entrar no chat
# quando entrar no chat: (aparece para todo mundo)
    # a mensagem que você entrou no chat
    # o campo e o botão de enviar mensagem
# a cada mensagem que você envia (aparece para todo mundo)
    # Nome: Texto da Mensagem


from flask import Flask, render_template # estruturas para criar o site
from flask_socketio import SocketIO, send # estruturas para criar o chat

app = Flask(__name__) # cria o site
app.config["SECRET"] = "ajuiahfa78fh9f78shfs768fgs7f6" # chave de seguranca, pode ser qualquer coisa, mas escolha algo dificil
app.config["DEBUG"] = True # para testarmos o código, no final tiramos
socketio = SocketIO(app, cors_allowed_origins="*") # cria a conexão entre diferentes máquinas que estão no mesmo site

@socketio.on("message") # define que a função abaixo vai ser acionada quando o evento de "message" acontecer
def gerenciar_mensagens(mensagem):
    print(f"Mensagem: {mensagem}")
    send(mensagem, broadcast=True) # envia a mensagem para todo mundo conectado no site

@app.route("/") # cria a página do site
def home():
    return render_template("homepage.html") # essa página vai carregar esse arquivo html que está aqui

if __name__ == "__main__":
    socketio.run(app, host='localhost', port=5001) # define que o app vai rodar no seu servidor local, ou seja, na internet em que o seu computador tá conectado