import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text)
    size = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'),
        nullable=False)
