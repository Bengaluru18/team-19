from flask import *
import pymysql
import _datetime
app = Flask(__name__)
app.secret_key = "any random string"


def dbconnection():
    connection = pymysql.connect(host="localhost"
                                 , user="root"
                                 , password="251408"
                                 , db="test3")
    return connection
@app.route("/")
def index():
    return render_template("home.html")
@app.route("/signin")
def signin():
    return render_template('signin.html')

@app.route('/admonecode',methods = ['POST', 'GET'])
def admin():


        if 'admin' in session:

           sql="select name,location,address,date,no_student,status from projects where status = 'newproject';"
           con =dbconnection()
           cur=con.cursor()
           print(sql)
           cur.execute(sql)
           newresults = cur.fetchall()
           sql = "select name,location,address,date,no_student,status from projects where status <> 'newproject';"
           print(sql)
           cur.execute(sql)
           exresults=cur.fetchall()
           con.close()
           return render_template("admone.html",newresults= newresults,exresults=exresults)
        else:
            return render_template("signin.html")

@app.route('/adfw2')
def lastdisp():
    return render_template("adfw2.html")


@app.route('/existingproject',methods=['POST','GET'])
@app.route('/5thpage.html',methods=['POST','GET'])
def existing():
    sql = "select name,locality,address,date,no_student,status from projects where status <> 'newproject';"
    con = dbconnection()
    cur = con.cursor()
    cur.execute(sql)
    exresults= cur.fetchall()


    con.close()
    return render_template("existingproj.html", exresults=exresults)

@app.route('/needsfill', methods=['POST','GET'])
def needsfill():
    name=request.form['name']
    locality=request.form['locality']
    address=request.form['address']
    no_student=request.form['no_student']
    status=request.form['status']
    sql="INSERT INTO projects(name,locality,address,date,phone_no,no_student,status) VALUES(\'"+name+"\',\'"+locality+"\',\'"+address+"\', NOW(),"+no_student+",\'"+status+"\');"
    return render_template('workersecond.html')





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
                if row[3]  == "admin":
                    sql = "select name,locality,address,date,no_student,status from projects where status = 'newproject';"
                    con = dbconnection()
                    cur = con.cursor()
                    print(sql)
                    cur.execute(sql)
                    newresults = cur.fetchall()
                    print(newresults)
                    sql = "select name,locality,address,date,no_student,status from projects where status <> 'newproject';"
                    cur.execute(sql)
                    print(sql)
                    exresults = cur.fetchall()
                    print(exresults)
                    con.close()
                    return render_template("admone.html", newresults=newresults, exresults=exresults)

                if row[3] =="feildworker":

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