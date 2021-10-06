import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Text)
    name = db.Column(db.Text)
    geo = db.Column(db.Text)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    url_meeting_schedule = db.Column(db.Text)
    url_result = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)

    files = db.relationship('File', backref='case', lazy=True)
    steps = db.relationship('Steps', backref='case', lazy=True)
