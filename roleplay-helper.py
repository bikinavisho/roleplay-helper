import flask

app = flask.Flask(__name__)


@app.route('/')
def render_index():
	character_name = 'Bianca'
	character_level = 1
	stats = [make_stat('Strength'), make_stat('Agility'), make_stat('Constitution'), make_stat('Acuity'),
			 make_stat('Intellect')]

	return flask.render_template('index.html', name=character_name, level=character_level, stats=stats)


def make_stat(name):
	return {'name': name, 'value': 0, 'xp': 0, 'xp_left': 0}


if __name__ == '__main__':
	app.run()
