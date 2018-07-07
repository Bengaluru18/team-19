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
    answers=db.Column(db.String(250))

    def __repr__(self):
        return f"assessments('{self.questions}')"

class actionplan(db.Model):
    aid = db.Column(db.Integer,primary_key=True)
    pid = db.Column(db.Integer(10), db.ForeignKey('projects.pid'))
    activities = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    date=Column(DateTime)
    progress= db.Column(db.String(60), nullable=False)
    version = db.Column(db.Integer(60), db.ForeignKey('versions.version'))

    def __repr__(self):
        return f"actionplan('{self.activities}', '{self.description}','{self.date}', '{self.progress}')"

class users(db.Model):
    Qid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)
    role =  db.Column(db.String(30), nullable=False)
   # posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"user('{self.username}', '{self.role}')"


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/fwone", methods=['GET', 'POST'])
def fwone():
  return render_template('fwone.html', posts=posts)

@app.route("/admone", methods=['GET', 'POST'])
def admone():
  return render_template('admone.html', posts=posts)

@app.route("/fwsecond", methods=['GET', 'POST'])
def fwsecond():
  return render_template('fwsecond.html', posts=posts)

@app.route("/adfw1", methods=['GET', 'POST'])
def adfw1():
  return render_template('adfw1.html', posts=posts)

@app.route("/adfw2", methods=['GET', 'POST'])
def adfw2():
  return render_template('adfw2.html', posts=posts)



if __name__ == '__main__':
    app.run(debug=True)
    
