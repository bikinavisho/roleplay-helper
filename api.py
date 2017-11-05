# API handles JS and socket requests
# key word: REQUESTS

import flask
from flask_socketio import join_room, send, emit, leave_room

from init import app, db, socket_io
import databaseFormat


@socket_io.on('stat_update')
def stat_update():
	print('hi')


