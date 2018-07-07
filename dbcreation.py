from flask import *
from flask_sqlalchemy import *
from datetime import *

from sqlalchemy import Column, Integer, DateTime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = ""

db = SQLAlchemy(app)
class projects(db.Model):
   pid = db.Column('projectid', db.Integer, primary_key = True)
   name = db.Column(db.String(100),unique=True)
   locality = db.Column(db.String(50))
   address = db.Column(db.String(200))
   date= Column(DateTime)
   phone_no= db.Column(db.String(50))
   no_student=db.Column(db.Integer)
   status=db.Column(db.String(100))

   def __repr__(self):
       return f"projects('{self.name}','{self.locality}','{self.address}','{self.date}','{self.phone_no}','{self.no_student}','{self.status}')"


class versions(db.Model):
    version = db.Column(db.Integer, primary_key= True)
    pid =db.column(db.Integer,db.ForeignKey('projects.pid'))
    date= Column(DateTime)

    def __repr__(self):
        return f"versions('{self.date}')"

class templates(db.Model):
    qid =db.Column(db.Integer, primary_key=True)
    questions=db.Column(db.String(250))
    qtype=db.Column(db.String(250))

    def __repr__(self):
        return f"templates('{self.question}','{self.qtype}')"

class assessment(db.Model):
    aid=db.Column(db.Integer,primary_key=True)
    pid=db.column(db.Integer,db.ForeignKey('projects.pid'))
    qid=db.column(db.Integer,db.ForeignKey('templates.qid'))
    questions=db.Column(db.String(250))

    def __repr__(self):
        return f"assessments('{self.questions}')"









if __name__ == '__main__':
    app.run(debug=True)
    



