import flask
import flask_sqlalchemy
from flask_socketio import SocketIO

app = flask.Flask(__name__)
app.config.from_pyfile('settings.py')
db = flask_sqlalchemy.SQLAlchemy(app)
socket_io = SocketIO(app)


