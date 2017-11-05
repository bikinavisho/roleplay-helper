from init import db, app


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(20))
	pw_hash = db.Column(db.String(64))


class Character(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(20))
	level = db.Column(db.Integer)
	stats = db.relationship('Stat', backref='character')


class Stat(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(20))
	value = db.Column(db.Integer)
	xp = db.Column(db.Integer)
	xp_left = db.Column(db.Integer)
	character_id = db.Column(db.Integer, db.ForeignKey('character.id'))


db.create_all(app=app)
