from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'random string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class Ationplan(db.Model):
    pid = db.relationship('Post', backref='projects', lazy=True)
    activities = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    datetime=datetime.now()
    progress= db.Column(db.String(60), nullable=False)
    version = db.Column(db.integer(60), nullable=False)

    def __repr__(self):
        return f"Ationplan('{self.activities}', '{self.description}', '{self.progress}','{self.version}')"
		
if __name__=='_main_':
   app.run(debug=True)