from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask('__main__')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = ""

db = SQLAlchemy(app)
class projects(db.Model):
   pid = db.Column('projectid', db.Integer, primary_key = True)
   name = db.Column(db.String(100), nullable=False,unique=True)
   locality = db.Column(db.String(50))
   address = db.Column(db.String(200))
   date=db.Column(db.Date)
   phone_no= db.Column(db.String(50))
   no_student=db.Column(db.Integer)
   status=db.Column(db.String(100))

   def __init__(self, name, locality, address, date,phone_no,no_student,status):
       self.name = name
       self.locality = locality
       self.address = address
       self.date = date
       self.phone_no=phone_no
       self.no_student=no_student
       self.status=status





if __name__ == '__main__':
    app.run(debug=True)
    db.create_all()
