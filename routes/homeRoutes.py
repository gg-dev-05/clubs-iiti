from flask import Blueprint, render_template, session
from config.mysql import mysql
from utilities.images import img

home = Blueprint('home', __name__)

@home.route("/")
def index():
    signedIn = dict(session).get("signedIn", None)
    msg = ""
    msg_alert = "danger"
    print(signedIn)
    admin = False

    if signedIn:
        email = dict(session).get("email", None)
        msg = "Successfully signed in as : " + email
        msg_alert = "success"

        # Check if is admin 
        if(email == "garvitgalgat@gmail.com"):
            print("Admin is here!!")
            admin = True

        else:        
            # Check if student info is available
            cur = mysql.connection.cursor()
            cur.execute("select Full_Name from students where Mail_id='{}'".format(email))
            present = cur.fetchone()
            mysql.connection.commit()
            cur.close()
            if(present):
                print("Already Submitted")
            else:
                return render_template("newStudent.html", msg="Please verify your details", msg_alert="warning", name=session['name'])

    elif signedIn == None:
        msg = "Please signin into CLUBSIITI"
        msg_alert = "warning"

    else:
        print("clearing session info")
        for key in list(session.keys()):
            session.pop(key)
        msg = "Please use IITI email id"
		
    cur = mysql.connection.cursor()
    print("Running query: ", "select * from events ORDER BY dated DESC;")
    cur.execute(f"select * from events ORDER BY dated DESC;")
    events = cur.fetchall()
    
    # print(events)
    name = dict(session).get("name", None)
    print("current user:", name)
    # print(img)
    return render_template('home.html', name=name, msg=msg, msg_alert=msg_alert,img=img, events=events, admin=admin)