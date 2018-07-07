from flask import *
import sqlite3
app = Flask(__name__)
app.secret_key = "any "

def dbconnection():
    conn = sqlite3.connect('database.db')
    return conn
@app.route("/")
@app.route("/home.html")
def index():
    return render_template("home.html")
@app.route("/signin")
def signin():
    return render_template('signin.html')

@app.route('/admonecode',methods = ['POST', 'GET'])
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
           exresults=cur.fetchall()
           con.close()
           return render_template("admone.html",newresults= newresults,exresults=exresults,message=message)

    return render_template("signin.html")

@app.route('/validation',methods = ['POST', 'GET'])
def validation():
    message = "login please"
    if request.method == 'POST':
        username=str(request.form['username'])
        password=str(request.form['password'])
        sql="select role from users where username= \'"+username+"\' and password = \'"+password+"\';"
        con = dbconnection()
        cur = con.cursor()
        cur.execute(sql)
        role = cur.fetchone()
        val=role[0]
        if val == "admin":
            return render_template('admin.html')
        elif role == "feildworker":
            return render_template('worker.html')




@app.route('/addwkr', methods=['POST', 'GET'])
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
