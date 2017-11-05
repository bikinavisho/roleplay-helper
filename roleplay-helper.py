import flask
import os

from init import app, db, socket_io
import databaseFormat


def init_stat(character_name, stat_name):
	stat = databaseFormat.Stat()
	stat.name = stat_name
	stat.value = 0
	stat.xp = 0
	stat.xp_left = 0
	stat.character_id = databaseFormat.Character.query.filter_by(name=character_name).first().id

	db.session.add(stat)
	db.session.commit()


def init_character(name):
	character = databaseFormat.Character()
	character.name = name
	character.level = 1

	db.session.add(character)
	db.session.commit()

	init_stat(name, 'Strength')
	init_stat(name, 'Agility')
	init_stat(name, 'Constitution')
	init_stat(name, 'Acuity')
	init_stat(name, 'Intellect')


@app.route('/')
def render_index():
	return flask.render_template('index.html')


@app.route('/', methods=['POST'])
def post_character():
	# TODO: make more complex forms and options
	name = flask.request.form['name']
	character = databaseFormat.Character.query.filter_by(name=name).first()
	if character is None:
		init_character(name)

	return flask.redirect(flask.url_for('render_character', name=name), 303)


@app.route('/characters/<string:name>')
def render_character(name):
	character = databaseFormat.Character.query.filter_by(name=name).first()
	return flask.render_template('character.html', name=character.name, level=character.level, stats=character.stats)


@app.route('/character')
def render_generic_character():
	character_name = 'Bianca'
	character_level = 1
	stats = []
	for stat in ['Power', 'Agility', 'Constitution', 'Acuity', 'Intellect']:
		stats.append(make_stat(stat))

	return flask.render_template('character.html', name=character_name, level=character_level, stats=stats)


def make_stat(name):
	return {'name': name, 'value': 0, 'xp': 0, 'xp_left': 0}


# Run Application
if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	socket_io.run(app, host='0.0.0.0', port=port)

