

from __future__ import print_function
from flask import Flask, render_template
from flask_sockets import Sockets


app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/chat')
def chat_socket(ws):
    while not ws.closed:
        message = ws.receive()
        if message is None:  
            continue

        clients = ws.handler.server.clients.values()
        for client in clients:
            client.ws.send(message)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    print("""
This can not be run directly because the Flask development server does not
support web sockets. Instead, use gunicorn:

gunicorn -b 127.0.0.1:8080 -k flask_sockets.worker main:app

""")
