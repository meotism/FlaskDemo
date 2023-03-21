from server import db

class UserJob(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('job_id', db.Integer, db.ForeignKey('job.id'), primary_key=True)