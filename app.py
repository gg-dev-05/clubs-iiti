from flask import Flask, render_template, redirect, request, session, url_for
from flask_mysqldb import MySQL
import smtplib
import ssl
import re
import MySQLdb
import yaml
from authlib.integrations.flask_client import OAuth
import os
from utilities.dbConfig import database_config
from config.mysql import mysql
from config.OAuth import oauth
from dotenv import find_dotenv, load_dotenv

from routes.homeRoutes import home
from routes.detailsRoutes import details
from routes.authRoutes import auth
from routes.clubRoutes import clubs
from routes.student import student
from routes.adminAccess import admin

'''
loading environment variables using dotenv
'''
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

DATABASE_URL = os.environ.get("CLEARDB_DATABASE_URL")
user, password, host, db = database_config(DATABASE_URL)

app.config['MYSQL_HOST'] = host
app.config['MYSQL_USER'] = user
app.config['MYSQL_PASSWORD'] = password
app.config['MYSQL_DB'] = db

''' MYSQL object initialization '''
mysql.init_app(app)


''' oauth object initialization '''
oauth.init_app(app)


app.secret_key = os.environ.get("secret_key")

app.register_blueprint(home)
app.register_blueprint(details)
app.register_blueprint(auth)
app.register_blueprint(clubs)
app.register_blueprint(student)
app.register_blueprint(admin)

@app.route("/mysql", methods=["POST"])
def run_queries():
    '''
    This Function runs mysql queries for testing routes
    '''
    data = request.form
    print(data)
    if(data['pwd'] == os.environ.get("secret_key")):
        cur = mysql.connection.cursor()
        cur.execute(data['q'])
        mysql.connection.commit()
        return "Done", 200
    return "Failed", 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html')


if __name__ == "__main__":
    if os.environ.get("env") == "dev":
        app.run(debug=True)
    else:
        app.run()
