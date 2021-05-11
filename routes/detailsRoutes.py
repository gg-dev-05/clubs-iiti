from flask import Blueprint, session, render_template, redirect
from utilities.images import img
from config.mysql import mysql

details = Blueprint('details', __name__, url_prefix="/details")

@details.route("/")
def myDetails():
    '''
    This is to display the form that displays the student information as it exists in the db. 
    '''
    email = dict(session).get("email", None)
    if(email == None):
        return redirect("/")
    
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM students WHERE Mail_id='{}'".format(email))
        student = cur.fetchone()

        return render_template("editStudent.html", student=student)



