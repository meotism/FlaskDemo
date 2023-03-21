# from config import *
from server import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type  = db.Column(db.String(50))
    name    = db.Column(db.String(50))
