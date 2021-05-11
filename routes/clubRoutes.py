from flask import Blueprint, render_template, request, session, redirect
from config.mysql import mysql
from utilities.send_mail import send_mail
from utilities.images import img
from utilities.verifyIITIStudent import checkIfMailIsValid
clubs = Blueprint('clubs', __name__, url_prefix='/clubs')


@clubs.route('/<clubName>')
def club(clubName):
    '''
    This route goes to the clubpage
    '''
    cur = mysql.connection.cursor()
    cur.execute("select * from clubs WHERE Title=\'{}\'".format(clubName))
    club = cur.fetchone()

    # Check if club exists ----------------
    try:
        title = club[1]
        info = club[2]
        achievements = club[3]
        website = club[6]
        events = club[-1]

    except:
        return render_template("error.html")
    member = False
    verified = False
    notexist = True
    imageUrl = img[clubName]

    # verifying the current email id ---------------
    try:
        cur.execute("SELECT Club_Title FROM clubheads WHERE Club_Head_Mail_Id = '{}'".format(
            session["email"]))
        club = cur.fetchall()

        for i in club:
            if (i[0] == clubName):
                verified = True

    except:
        verified = False
    # ----------------------------------------------

    # verifying the current email id with current members ---------------
    try:
        cur.execute("SELECT Club_Name FROM clubmembers WHERE Mail_Id = '{}'".format(
            session["email"]))
        club = cur.fetchall()

        for i in club:
            if i[0] == title:
                notexist = False

        if notexist:
            cur.execute("SELECT Club_Name FROM approvals WHERE Mail_Id = '{}'".format(
                session["email"]))
            clb = cur.fetchall()
            for i in clb:
                if i[0] == title:
                    notexist = False

    except:
        notexist = True
    # ----------------------------------------------

    # verifying iiti student ---------------
    try:
        email = session["email"]
        if email[-11:] == "@iiti.ac.in":
            member = True
    except:
        member = False

    # ----------------------------------------------

    # Get new recruits from database
    cur.execute("select Club_Name FROM clubs WHERE Title='{}'".format(clubName))
    club = cur.fetchone()

    cur.execute(
        "SELECT Full_Name, Mail_Id, CurrentStatus FROM approvals INNER JOIN students USING(Mail_Id) WHERE Club_Name = '{}'".format(club[0]))
    newRecruits = cur.fetchall()
    cur.execute(
        "SELECT FUll_Name, Mail_Id FROM students WHERE Mail_id IN (SELECT Mail_id FROM clubmembers WHERE Club_Name='{}');".format(club[0]))
    currentMembers = cur.fetchall()
    return render_template("clubtemplate.html",
                           title=title,
                           info=info,
                           achievements=achievements,
                           website=website,
                           clubName=clubName,
                           imageUrl=imageUrl,
                           verified=verified, notexist=notexist, member=member,
                           currentMembers=currentMembers, newRecruits=newRecruits, events=events)


@clubs.route("/<clubName>/apply")
def apply(clubName):
    '''
    To apply in the club
    '''
    cur = mysql.connection.cursor()
    user = dict(session).get("email", None)

    if(user == None):
        return render_template("signIn.html")
    else:
        cur = mysql.connection.cursor()
        cur.execute(
            "select Club_Name FROM clubs WHERE Title='{}'".format(clubName))
        club = cur.fetchone()
        cur.execute(
            "INSERT INTO approvals VALUES('{}', '{}', 'U');".format(user, club[0]))
        mysql.connection.commit()
        cur.execute("select * from clubs WHERE Title=\'{}\'".format(clubName))
        club_title = cur.fetchone()
        cur.close()
        title = club_title[1]
        send_mail(user, "Subject: Thanks for applying\n\nThank you for applying to {}. \n You will soon recieve a mail regarding the interview from the club head".format(title))
        return render_template("applied.html", title=title)


@clubs.route("/<clubName>/<manage>/<email>")
def manage(clubName, manage, email):
    '''
    This function helps admin to accept reject or schedule meeting
    '''
    cur = mysql.connection.cursor()
    user = dict(session).get("email", None)
    if(user == None):
        return render_template("signIn.html")
    verified = False
    cur.execute(
        f"SELECT Club_Title FROM clubheads WHERE Club_Head_Mail_Id ='{user}'")
    club = cur.fetchall()

    for i in club:
        if (i[0] == clubName):
            verified = True

    if(verified):

        # Remove student from the club
        if(manage == "remove"):
            cur = mysql.connection.cursor()
            cur.execute(
                "select Club_Name FROM clubs WHERE Title='{}'".format(clubName))
            club = cur.fetchone()
            cur.execute("DELETE FROM clubMembers WHERE Mail_Id='{}' AND Club_Name='{}';".format(
                email, club[0]))
            mysql.connection.commit()
            cur.close()
            return redirect("/clubs/{}".format(clubName))

        elif(manage == "approve"):
            cur = mysql.connection.cursor()
            cur.execute(
                "select Club_Name FROM clubs WHERE Title='{}'".format(clubName))
            club = cur.fetchone()
            cur.execute(
                "INSERT INTO clubmembers VALUES ('{}','{}');".format(email, club[0]))
            cur.execute("DELETE FROM approvals WHERE Mail_Id='{}' AND Club_Name='{}';".format(
                email, club[0]))
            cur.execute(
                "DELETE FROM meetings WHERE student_mail_id = '{}' AND host_mail_id = '{}'".format(email, user))
            send_mail(
                email, "Subject:Welcome Welcome!!\n\nCongrats from {}\n You have been accepted into the club!!".format(club[0]))
            mysql.connection.commit()
            cur.close()
            return redirect("/clubs/{}".format(clubName))

        elif(manage == "reject"):
            cur = mysql.connection.cursor()
            cur.execute(
                "select Club_Name FROM clubs WHERE Title='{}'".format(clubName))
            club = cur.fetchone()
            cur.execute("DELETE FROM approvals WHERE Mail_Id='{}' AND Club_Name='{}';".format(
                email, club[0]))
            mysql.connection.commit()
            cur.close()
            return redirect("/clubs/{}".format(clubName))

        elif(manage == "schedule"):
            if(checkIfMailIsValid(email)):
                # msg = "Scheduling Interview with clubhead of " + clubName
                # send_mail(user, "Interview scheduled with student")
                return render_template("interview.html", host=user, student=email, clubName=clubName, meeting_details=["", "", ""])

            else:
                return render_template("error.html")

        else:
            return render_template("error.html")

    else:
        return render_template("error.html")


@clubs.route("/<clubName>/edit", methods=['GET', 'POST'])
def edit(clubName):
    '''
    This function helps edit the club details
    '''
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        email = dict(session).get("email", None)
        if(email == None):
            return render_template("signIn.html")

        verified = False
        cur.execute(
            f"SELECT Club_Title FROM clubheads WHERE Club_Head_Mail_Id ='{email}'")
        club = cur.fetchall()

        for i in club:
            if (i[0] == clubName):
                verified = True

        if(verified):
            cur.execute(
                "select Info, Achievements, Events FROM clubs WHERE Title='{}'".format(clubName))
            information = cur.fetchone()
            return render_template("editor.html", info=information[0], achievements=information[1], clubName=clubName, events=information[2])

        else:
            return render_template("error.html")

    else:
        data = request.form
        info = data['info']
        # replace ' with " so that these string does not interfere with our sql queries
        info = info.replace("'", '"')
        achievements = data['achievements']
        achievements = achievements.replace("'", '"')
        events = data['events']
        events = events.replace("'", '"')
        cur = mysql.connection.cursor()
        cur.execute("UPDATE clubs SET Info = '{}', Achievements = '{}', Events = '{}' WHERE Title = '{}'".format(
            info, achievements, events, clubName))
        cur.execute(
            "INSERT INTO events VALUES ('{}','{}', NOW());".format(clubName, events))

        mysql.connection.commit()
        cur.close()

        return redirect("/clubs/{}".format(clubName))


@clubs.route("/<clubName>/meeting/<student>", methods=["GET", "POST"])
def schedule(clubName, student):
    '''
    This function schedules the meeting with students
    '''
    user = dict(session).get("email", None)
    if(user == None):
        return render_template("signIn.html")

    details = request.form

    verified = False
    cur = mysql.connection.cursor()
    cur.execute(
        f"SELECT Club_Title FROM clubheads WHERE Club_Head_Mail_Id ='{user}'")
    club = cur.fetchall()

    for i in club:
        if (i[0] == clubName):
            verified = True

    if(verified):

        if request.method == "POST":

            details = request.form
            time = details['time']
            time = time[:-3]

            date = details['date']
            date = date.split("/")
            date = date[2]+"-"+date[0]+"-"+date[1]

            link = details['link']
            host = details['host']


            # Insert into db

            send_mail(user, "Subject: Meeting Details\n\nMeeting scheduled with {}\nDetails: \nTime: {}\n Date: {}\n Link: {}".format(
                student, time, date, link))
            send_mail(student, "Subject: Meeting Details\n\nHere are the scheduled meeting details:\nTime: {}\n Date: {}\n Link: {}".format(
                time, date, link))

            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO meetings VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE host_mail_id=%s, student_mail_id=%s, meeting_time=%s, meeting_date=%s, link=%s",
                        (host, student, time, date, link,
                         host, student, time, date, link))
            cur.execute(
                "UPDATE approvals SET CurrentStatus='A' WHERE Mail_Id='{}'".format(student))
            mysql.connection.commit()
            cur.close()
            # send mails
            return render_template("scheduled.html", student=student, link=link)

        else:
            if(checkIfMailIsValid(student)):
                cur = mysql.connection.cursor()
                cur.execute("SELECT meeting_time, meeting_date, link FROM meetings WHERE host_mail_id = '{}' AND student_mail_id = '{}'".format(
                    user, student))
                meeting_details = cur.fetchone()
                date = str(meeting_details[1])
                date = date.split("-")
                date = date[1]+'/'+date[2]+'/'+date[0]
                date = date
                send_mail(user, "Subject: Meeting Updated\n\nMeeting updated with {}\nDetails:\nTime: {}\n Date: {}\n Link: {}".format(
                    student, meeting_details[0], date, meeting_details[2]))
                return render_template("interview.html", host=user, student=student, clubName=clubName, meeting_details=meeting_details, date=date)
            else:
                return render_template("error.html")

    else:
        return render_template("error.html")
