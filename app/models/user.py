import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    organization = db.Column(db.Text)
    email = db.Column(db.text)
    roles = db.Column(db.Text)
    date_created = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True, server_default='true')
    cases = db.relationship('Case', backref='user', lazy=True)

    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.id

    def is_valid(self):
        return self.is_active
