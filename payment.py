from flask import Flask
from flask import render_template,request
import pyodbc 
app = Flask(__name__)
# home page
@app.route("/*")
def home():
    print('Loading Home page')
    return render_template("/web.html")
# form page
@app.route("/buy", methods=["GET","POST"])
def form():
    q=('Driver={SQL Server};' 'Server=.;' 'Database=master;' 'Trusted_connection=yes;')
    con=pyodbc.connect(q)
    cursor=con.cursor()
    print("Creating a New Table")
    print('Loading Registration page')
    if request.method == "POST":
        Name=request.form["name"]
        Email = request.form["email"]
        Address = request.form["address"]
        City = request.form["city"]
        State = request.form["state"]
        ZipCode = request.form["zip"]
        NameonCard = request.form["cname"]
        credictcardnumber = request.form["cnum"]
        ExpMonth = request.form["exmon"]
        ExpYear = request.form["exyear"]
        CVV = request.form["cvv"]
       
        cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'payment'")
        if cursor.fetchone():
            cursor.execute("insert into payment values(?,?,?,?,?,?,?,?,?,?,?)",(Name,Email,Address,City,State,ZipCode,NameonCard,credictcardnumber,ExpMonth,ExpYear,CVV))
            con.commit()
            con.close()
        else:
            cursor.execute("create table payment(Name varchar(20),Email varchar(30),Address varchar(30),City varchar(30),State varchar(30),Zip_Code varchar(30),Name_on_Card varchar(30),credict_card_number varchar(30),Exp_Month varchar(30),Exp_Year varchar(30),CVV varchar(30))")
            con.commit()
            cursor.execute("insert into payment values(?,?,?,?,?,?,?,?,?,?,?)",(Name,Email,Address,City,State,ZipCode,NameonCard,credictcardnumber,ExpMonth,ExpYear,CVV))
            con.commit()
            con.close()
            
        return render_template('paymentsuccess.html',name=Name,email=Email,address=Address)
    else:
        Name=request.args.get("name")        
        Email = request.args.get("email")
        Address = request.args.get("address")
        City = request.args.get("city")
        State = request.args.get("state")
        ZipCode = request.args.get("zip")
        NameonCard = request.args.get("cname")
        credictcardnumber = request.args.get("cnum")
        ExpMonth = request.args.get("exmon")
        ExpYear = request.args.get("exyear")
        CVV = request.args.get("cvv")
        return render_template('paymentsuccess.html',name=Name,email=Email,address=Address)
if __name__ == "__main__":
    app.run(debug=True)
    print('web service started')
else:
    print('web service Stopped')
     
