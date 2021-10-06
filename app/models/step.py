import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Step(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    status = db.Column(db.Text)
    seq = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    closed_at = db.Column(db.DateTime)
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'),
        nullable=False)
