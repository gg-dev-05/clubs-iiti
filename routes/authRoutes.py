from flask import Blueprint, url_for, session, redirect
from config.OAuth import google, oauth

auth = Blueprint('auth', __name__)


@auth.route("/login")
def login():
    google = oauth.create_client("google")
    redirect_uri = url_for("auth.authorize", _external=True)
    return google.authorize_redirect(redirect_uri)


@auth.route("/authorize")
def authorize():
    google = oauth.create_client("google")
    token = google.authorize_access_token()
    resp = google.get("userinfo", token=token)
    user_info = resp.json()
    session["email"] = user_info["email"]
    email = session["email"]   
    session["name"] = user_info["name"]
    session["signedIn"] = True

    
    # Find admin mail in database (assuming garvitgalgat@gmail.com is admin)
    if(email == "garvitgalgat@gmail.com"):
        session["name"] = "ADMIN"
        return redirect("/admin")

    
    if email[:3] in ("cse") and email[-11:] == "@iiti.ac.in":
        session["roll_no"] = email[3:12]
        session["branch"] = email[:3].upper()
        return redirect("/")
    elif email[:2] in ("ee", "me", "ce") and email[-11:] == "@iiti.ac.in":
        session["roll_no"] = email[2:11]
        session["branch"] = email[:2].upper()
        return redirect("/")
    elif email[:4] in ("mems") and email[-11:] == "@iiti.ac.in":
        session["roll_no"] = email[4:13]
        session["branch"] = email[:4].upper()

        return redirect("/")
    else:
        logout()
        session["signedIn"] = False 
        return redirect("/")

@auth.route("/logout")
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect("/")
