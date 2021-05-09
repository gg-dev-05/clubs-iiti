from flask import Blueprint, render_template, request, session, redirect
from config.mysql import mysql
from utilities.send_mail import send_mail
from utilities.images import img
from utilities.verifyIITIStudent import checkIfMailIsValid
clubs = Blueprint('clubs', __name__, url_prefix='/clubs')


@clubs.route('/<clubName>')
def club(clubName):

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
    # print('-----------------')
    # print(imageUrl)
    # -----------------------------------------

    # verifying the current email id ---------------
    try:
        cur.execute("SELECT Club_Title FROM clubheads WHERE Club_Head_Mail_Id = '{}'".format(
            session["email"]))
        club = cur.fetchall()
        # print(club)

        for i in club:
            # print(i[0])
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
        # print(club)

        for i in club:
            # print(i[0])
            if i[0] == title:
                notexist = False

        if notexist:
            cur.execute("SELECT Club_Name FROM approvals WHERE Mail_Id = '{}'".format(
                session["email"]))
            clb = cur.fetchall()
            for i in clb:
                # print(i[0])
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
    # print(club)

    cur.execute(
        "SELECT Full_Name, Mail_Id, CurrentStatus FROM approvals INNER JOIN students USING(Mail_Id) WHERE Club_Name = '{}'".format(club[0]))
    newRecruits = cur.fetchall()
    print("newRecruits: ", newRecruits)
    cur.execute(
        "SELECT FUll_Name, Mail_Id FROM students WHERE Mail_id IN (SELECT Mail_id FROM clubmembers WHERE Club_Name='{}');".format(club[0]))
    currentMembers = cur.fetchall()
    print("currentMembers: ", currentMembers)
    # print(clubName)
    print("verified:", verified)
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
    cur = mysql.connection.cursor()
    user = dict(session).get("email", None)
    if(user == None):
        return render_template("signIn.html")
    verified = False
    print("Running query: ", "SELECT Club_Title FROM clubheads WHERE Club_Head_Mail_Id = '{}'".format(
        session["email"]))
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
            print("Executing Query: " +
                  "DELETE FROM clubMembers WHERE Mail_Id='{}' AND Club_Name='{}';".format(email, club[0]))
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
