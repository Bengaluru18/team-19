from flask import *
import sqlite3
app = Flask(__name__)
app.secret_key = "any "

def dbconnection():
    conn = sqlite3.connect('database.db')
    return conn
@app.route("/")
def index():
    return redirect(url_for('admin'))

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
@app.route('/home/signin/admonecode',methods = ['POST', 'GET'])
def admin():
    message="login please"
    if request.method == 'POST':
        if 'adminname' in session:

           sql="select name,location,address,date,phone_no,no_student,status from projects where status = 'newproject';"
           con =dbconnection()
           cur=con.cursor()
           cur.execute(sql)
           newresults = cur.fetchall();
           sql = "select name,location,address,date,phone_no,no_student,status from projects where status <> 'newproject';"
           cur.execute(sql)
           exresults=cur.fetchall();
           con.close()
           return render_template("admone.html",newresults= newresults,exresults=exresults,message=message)

    return render_template("signin.html")


@app.route('/home/signin/addwkr', methods=['POST', 'GET'])
def addworker():
    message="login please"
    if request.method == 'POST':
        if 'adminname' in session:
            username = request.form['username']
            password = request.form['password']
            role="feildworker"
            con = dbconnection()
            cur = con.cursor()
            try:
                cur.execute('INSERT INTO users (username,password,role) VALUES (?, ?, ?)', (username, password, role))
                con.commit()
                con.close()
                message="successful registration of worker"
            except:
                con.rollback()
                message="error occured try again"
                con.close()
            return render_template("admone.html", message=message)
        return render_template("admone.html",message=message)
    return render_template("admone.html",message=message)


@app.route('/fwone', methods=['POST', 'GET'])
def fwone():
    return render_template('fwone.html')




if __name__ == '__main__':
   app.run(debug = True)
