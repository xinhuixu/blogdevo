from flask import Flask, redirect, request, render_template, session, url_for, flash
import os
from utils import db_builder
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = '\xf35{\x12\x1c\xc7;\xf0\xd1x\x8d8\xe7f\xa3'

@app.route("/")
def index():
    for user in session:
        return redirect(url_for("home"))
    return redirect(url_for("login"))

@app.route("/login/")
def login():
    for user in session:
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/home/")
def home():
    return render_template("home.html") #stuff = "username"

@app.route("/auth/", methods=["POST"])
def auth():
    ## register
    print request.form
    if "register" in request.form:
        if (request.form["username"] == "" or request.form["password"] == ""):
            flash("please fill in all forms of info")
            return redirect(url_for("login"))
        elif (db_builder.check(request.form["username"])):
            flash("username taken, please choose a new one")
            return redirect(url_for("login"))
        else:
            user0 = request.form["username"]
            pass0 = request.form["password"]
            db_builder.add_user(user0,pass0)
            flash("new account created")
            return redirect(url_for("login"))
    ## login
    else:
        if (not (db_builder.check(request.form['username']))):
            flash("username does not exist") 
            return redirect(url_for("login"))
        elif (db_builder.getHash(user1) == request.form['password']):
            user1 = request.form['username']
            session["user"] = user1
            return redirect(url_for("home"))
        else:
            flash("incorrect username and password combination")
            return redirect(url_for("login"))

@app.route("/logout/")
def logout():
    session.pop("user")
    return redirect(url_for("index"))

def hashp(password):
    return hashlib.sha512(password).hexdigest()

def add_content():
    return True

@app.route("/story/")
def story(id):
    # title = db_builder.getTitle(id)
    # content = db_builder.getLatestContent(id)
    # return render_template("story.html", title = title, content = content, author = session['username'])
    return True

if __name__ == "__main__":
    app.debug = True
    app.run()
