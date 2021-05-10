from flask import Blueprint, render_template, session, request, redirect
from config.mysql import mysql

student = Blueprint('student', __name__)


@student.route("/student", methods=['GET', 'POST'])
def studentHome():
    user = dict(session).get("email", None)
    if(user == None):
        return render_template("signIn.html")

    if request.method == 'POST':
        # Get DATA from the form
        student = request.form
        try:
            Mail_Id = student['mail_id']
            Full_Name = student['full_name']
            LinkedIn = student['linkedin']
            Branch = student['branch']
            Roll_No = int(student['roll_no'])
            Phone_No = int(student['phone_no'])
            Current_Year = int(student['year'])
            Bio = student['Bio']
            # send_mail(Mail_Id, "Thanks for trusting clubsIITI here are your submitted details: \nYour Mail Id : {}\n Full Name: {}\n LinkedIn: {}\n Branch: {}\n Roll No.: {}\n Phone No.: {}\n Current Year: {}\n Bio: {}\n".format(Mail_Id, Full_Name, LinkedIn, Branch, Roll_No, Phone_No, Current_Year,Bio))

            if(Mail_Id == user):
                cur = mysql.connection.cursor()
                cur.execute(
                    "INSERT INTO students VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Mail_Id=%s, Full_Name=%s, LinkedIn=%s, Branch=%s, Roll_No=%s, Phone_No=%s, Current_Year=%s, Bio=%s",
                    (Mail_Id, Full_Name, LinkedIn, Branch, Roll_No, Phone_No,
                     Current_Year, Bio, Mail_Id, Full_Name, LinkedIn, Branch, Roll_No, Phone_No,
                     Current_Year, Bio))

                mysql.connection.commit()
                cur.close()

                return redirect("/")

            else:
                return render_template("notAuthorized.html")

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            return str(e)

    else:
        # print("Redirect")
        return redirect("/login")


@student.route("/remove", methods=['POST'])
def bye():
    user = dict(session).get("email", None)
    if(user == None):
        return render_template("signIn.html")

    if request.method == 'POST':
        cur = mysql.connection.cursor()

        print("Executing Query: " +
              "DELETE FROM students WHERE Mail_Id='{}';".format(user))
        cur.execute("DELETE FROM students WHERE Mail_Id='{}';".format(user))
        mysql.connection.commit()
        cur.close()
        return render_template("goodbye.html")

    else:
        return render_template("error.html")
