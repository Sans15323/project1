from flask import Flask
from flask import render_template,request
import pyodbc 
app = Flask(__name__)
# home page
@app.route("/@")
def home():
    print('Loading Home page')
    return render_template("/web.html")
# form page
@app.route("/signup", methods=["GET","POST"])
def form():
    q=('Driver={SQL Server};' 'Server=.;' 'Database=master;' 'Trusted_connection=yes;')
    con=pyodbc.connect(q)
    cursor=con.cursor()
    print("Creating a New Table")
    print('Loading Registration page')
    if request.method == "POST":
        Name=request.form["name"]
        Email = request.form["email"]
        Password = request.form["password"]
       
        cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'userdata'")
        if cursor.fetchone():
            cursor.execute("insert into userdata values(?,?,?)",(Name,Email,Password))
            con.commit()
            con.close()
        else:
            cursor.execute("create table userdata(Name varchar(20),Email varchar(30),Password varchar(10))")
            con.commit()
            
        return render_template('loginsuccess.html',name=Name,email=Email)
    else:
        Name=request.args.get("name")        
        Email = request.args.get("email")
        Password = request.args.get("password")
        return render_template('loginsuccess.html',name=Name,email=Email)
if __name__ == "__main__":
    app.run(debug=True)
    print('web service started')
else:
    print('web service Stopped')
     
