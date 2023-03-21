from flask import Flask, render_template
from datetime import datetime
from flask_cors import CORS
# load_dotenv
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')
import os
from flask_sqlalchemy import SQLAlchemy
# import models
# from models.user import *
# from models.job import *
# from models.user_job import *

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

CORS(app, resources={r"/api/*": {"origins": "*"}})
variable = os.getenv("VARIABLE")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@localhost/db-dev'

db = SQLAlchemy(app)

@app.before_first_request
def init():
    print("Ok")
    
# models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type  = db.Column(db.String(50))
    name    = db.Column(db.String(50))
    def __repr__(self):
        return "<User(id='%s', type='%s', name='%s')>" % (self.id, self.type, self.name)

class UserJob(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('job_id', db.Integer, db.ForeignKey('job.id'), primary_key=True)
    def __repr__(self):
        return "<UserJob(user_id='%s', job_id='%s')>" % (self.user_id, self.job_id)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type  = db.Column(db.String(50))
    name    = db.Column(db.String(50))
    def __repr__(self):
        return "<Job(id='%s', type='%s', name='%s')>" % (self.id, self.type, self.name)
with app.app_context():
    db.create_all()

@app.route('/api/users/add', methods=['GET'])
def addUser():
    users = [User(type='normal', name='test')
    ,User(type='admin', name='tuan')]
    db.session.add_all(users)
    db.session.commit()
    return 'User added', 200

@app.route('/api/users', methods=['GET'])
def getUsers():
    page = db.paginate(db.select(User))
    return render_template("./list_users.html", page=page)

@app.route('/api/users/<id>', methods=['GET'])
def getUserByID(id):
    user = db.session.execute(db.select(User).where(User.id == id)).scalar_one()
    return render_template("./user.html", user=user)

@app.route('/api/jobs/add', methods=['GET'])
def addJob():
    jobs = [Job(type='director', name='tuan'), Job(type='employee', name='test')]
    db.session.add_all(jobs)
    db.session.commit()
    return 'Job added', 200

@app.route('/api/jobs', methods=['GET'])
def getJobs():
    page = db.paginate(db.select(Job))
    return render_template("./list_jobs.html", page=page)

@app.route('/api/user_jobs/add', methods=['GET'])
def addUserJob():
    userJobs= [ UserJob(user_id=1, job_id=1),UserJob(user_id=2, job_id=2)]
    db.session.add_all(userJobs)
    db.session.commit()
    return 'UserJob added', 200

@app.route('/api/user_jobs', methods=['GET'])
def getUserJobs():
    page = db.paginate(db.select(UserJob))
    return render_template("./list_user_jobs.html", page=page)

@app.route('/')
def homepage():  
    the_time = datetime.now()
    return 'Hello World! Time on server is {}'.format(the_time) + ' and variable is {}'.format(variable) 

if __name__ == '__main__':
    app.run(debug='on')
