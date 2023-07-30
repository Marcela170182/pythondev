# front end -> "é o que vc vê"
#html, css, javascript

#Backend -> a lógica de funcionamento por trás do site
#python

#framework -> Flask -> criar site

#ambiente virtual -> local no seu computador com instalações específicas
# https://cdnjs.com/

from flask import Flask, render_template
from flask_socketio import SocketIO, send
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
#criar funcionalidade mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)
# criar a 1ª pagina = 1ªrota

@app.route("/")
def homepage():
    return render_template("index.html")

#roda o aplicativo
socketio.run(app, host="192.168.10.102")

#websocket -> tunel
#pip install python-socketio flask-socketio simple-websocket



