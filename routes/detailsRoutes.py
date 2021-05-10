from flask import Blueprint, session, render_template, redirect
from utilities.images import img
from config.mysql import mysql

details = Blueprint('details', __name__, url_prefix="/details")

@details.route("/")
def myDetails():
    email = dict(session).get("email", None)
    if(email == None):
        return redirect("/")
    # Check if is admin 
    if(email == "garvitgalgat@gmail.com"):
        return render_template("error.html")
    
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM students WHERE Mail_id='{}'".format(email))
        student = cur.fetchone()
        # for i in range(len(student)):
        #     print(i, student[i])

        return render_template("editStudent.html", student=student)



