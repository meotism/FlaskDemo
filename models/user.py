from server import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type  = db.Column(db.String(50))
    name    = db.Column(db.String(50))
