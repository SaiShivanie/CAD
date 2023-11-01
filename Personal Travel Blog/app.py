import flask
from flask import *
import os
os.add_dll_directory("C:\Program Files\IBM\SQLLIB\BIN")
import ibm_db
from flask_db2 import DB2

dsn_hostname = "2d46b6b4-cbf6-40eb-bbce-6251e6ba0300.bs2io90l08kqb1od8lcg.databases.appdomain.cloud" 
dsn_uid = "jpm30609"     
dsn_pwd = "G6aftPPNLi5N5XCl"     

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "bludb"           
dsn_port = "32328"                
dsn_protocol = "TCPIP"            
dsn_security = "SSL"

dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security)

#print the connection string to check correct values are specified

try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )

app = Flask(__name__)

@app.route("/")
def display():
    return render_template("home.html")

@app.route("/travel")
def travel():
    return render_template("travel.html")

@app.route("/taj")
def taj():
    query = "SELECT * FROM dest"
    stmt = ibm_db.exec_immediate(conn, query)
    data= []
    res = ibm_db.fetch_assoc(stmt)
    while res:
        data.append(res)
        res = ibm_db.fetch_assoc(stmt)
    return render_template("taj.html",data=data)

@app.route("/guide")
def guide():
    return render_template("guide.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/india")
def india():
    query = "SELECT * FROM keyfacts"
    stmt = ibm_db.exec_immediate(conn, query)
    key_facts_data = []
    result = ibm_db.fetch_assoc(stmt)
    while result:
        key_facts_data.append(result)
        result = ibm_db.fetch_assoc(stmt)
    
    return render_template("india.html", key_facts_data=key_facts_data)
    #return render_template("index.html")

@app.route('/submit-comment', methods=['POST'])
def submit_comment():
    comment = request.form.get('comment')
    if conn:
        # Insert the comment into the database
        stmt = ibm_db.prepare(conn, "INSERT INTO comments (comment) VALUES (?)")
        if ibm_db.execute(stmt, (comment,)):
            return redirect(request.referrer)
        else:
            return "Database error"
    else:
        return "Database connection error"
if __name__=="__main__":
    app.run(debug=True)