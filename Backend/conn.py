#!/usr/bin/env python3
""" socket connection """

from app import app
from flask import request
from flask_cors import CORS
from flask_socketio import SocketIO, emit

socketio = SocketIO(app, cors_allowed_origins="http://localhost:3000")
CORS(app)

global onlineUsers
onlineUsers = {}


def get_key(d, value):
    """ returns the key of a value in a dictionary """
    for k, v in d.items():
        if v == value:
            return k


@socketio.on('connect')
def connect():
    """ handles a user connecting to the socket """
    print('Client connected:', request.sid)


@socketio.on('disconnect')
def disconnect():
    """ handles a user disconnecting from the socket """
    user_id = get_key(onlineUsers, request.sid)
    if user_id:
        del onlineUsers[user_id]
        print('Client disconnected:', request.sid)


@socketio.on('sendMessage')
def sendMessage(data):
    """ handles a user sending a message """
    sender_id = data['sender_id']
    receiver_id = data['receiver_id']
    message = data['message']

    send_user_socket = onlineUsers.get(receiver_id)
    if send_user_socket:
        socketio.emit('receiveMessage', {
            'sender_id': sender_id,
            'receiver_id': receiver_id,
            'message': message
        }, room=send_user_socket)


@socketio.on('joinRoom')
def joinRoom(data):
    """ handles a user joining a room """
    user_id = data['user_id']
    room_id = data['room_id']
    onlineUsers[user_id] = request.sid
    socketio.emit('userJoinedRoom', {
        'user_id': user_id,
        'room_id': room_id
    }, room=request.sid)


@socketio.on('leaveRoom')
def leaveRoom(data):
    """ handles a user leaving a room """
    user_id = data['user_id']
    room_id = data['room_id']
    socketio.emit('userLeftRoom', {
        'user_id': user_id,
        'room_id': room_id
    }, room=request.sid)


@socketio.on('addUser')
def addUser(user_id):
    """ handles a user joining a room """
    onlineUsers[user_id] = request.sid
    emit('userAdded', user_id, broadcast=True)


@socketio.on('removeUser')
def removeUser(user_id):
    """ handles a user leaving a room """
    del onlineUsers[user_id]
    emit('userRemoved', user_id, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080, debug=True)
