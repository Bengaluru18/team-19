from flask import *
import pymysql
app = Flask(__name__)
app.secret_key = "any "


def dbconnection():
    connection = pymysql.connect(host="localhost"
                                 , user="root"
                                 , password="251408"
                                 , db="jpmc")
    return connection
@app.route("/")
def index():
    return render_template("home.html")
@app.route("/signin")
def signin():
    return render_template('signin.html')

@app.route('/admonecode',methods = ['POST', 'GET'])
def admin():

    if request.method == 'POST':
        if 'admin' in session:

           sql="select name,location,address,date,phone_no,no_student,status from projects where status = 'newproject';"
           con =dbconnection()
           cur=con.cursor()
           cur.execute(sql)
           newresults = cur.fetchall()
           sql = "select name,location,address,date,phone_no,no_student,status from projects where status <> 'newproject';"
           cur.execute(sql)
           exresults=cur.fetchall()
           con.close()
        return render_template("admone.html",newresults= newresults,exresults=exresults)

    return render_template("signin.html")

''''@app.route('/validation',methods = ['POST', 'GET'])
def validation():
    message = "login please"
    if request.form['username'] == "admin":
            if request.form['password']=='admin':
                return render_template('admin.html')
            else:
                return render_template('signin.html')
    if request.form['username']=="feildworker":
        if request.form['password']=="feild":
            return render_template('worker.html')
    return render_template('home.html')'''

@app.route('/validation',methods=['POST','GET'])
def validation():
    if request.method=='POST':
        username =request.form['username']
        password =request.form['password']
        sql="select * from users where username = \'"+ username +"\' and password = \'"+ password+"\';"
        print(sql)
        con = dbconnection()
        cur = con.cursor()
        cur.execute(sql)
        result=cur.fetchall()
        if result is not None:
            for row in result:
                print(row[3])
                if row[3]  == 'admin':
                    Session['admin'] = row[3]
                    return  render_template('admin.html')
                if row[3] =='feildworker':
                    Session['feildworker']=row[3]
                    return render_template('worker.html')
        return render_template('signin.html')










@app.route('/addwkr', methods=['POST', 'GET'])
def addworker():
    message="login please"
    if request.method == 'POST':
        if 'admin' in session:
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
