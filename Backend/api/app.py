#!/usr/bin/env python
""" Flask application """

import os
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('YOUR_FLASK_SECRET_KEY', 'default_secret_key')
socketio = SocketIO(app)

@app.route('/')
def index():
    """
    A function that serves as the route for the root URL path.
    
    Returns:
        The rendered HTML template for the 'chat.html' page.
    """
    return render_template('chat.html')

@socketio.on('message')
def handleMessage(msg):
    """
    Handle a message received from the client.

    Parameters:
        msg (str): The message received from the client.

    Returns:
        None
    """
    print('Message: ' + msg)
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
    app.run
