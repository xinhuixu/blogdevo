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
    # if ("register" in request.form):
        # if (request.form["username"] == "" or request.form["password"] == ""):
            # flash("please fill in all forms of info")
            # return redirect(url_for("login"))
        # else if (db_builder.check(request.form["user"])):
            # flash("username taken, please choose a new one")
            # return redirect(url_for("login"))
        # else:
            # user0 = request.form["username"]
            # pass = hash(request.form["password"])
            # db_builder.add_user(user0,pass)
            # flash("new account created")
            # return redirect(url_for("login"))
    ## login
    # else if ("login" in request.form)
        # if (! db_builder.check(request.form['username'])):
            # flash("username does not exist") 
            # return redirect(url_for("login"))
        # user1 = request.form['username']
        # else if (! db_builder.getHash(user1) == (request.form['password'])):
            # flash("incorrect username and password combination")
            # return redirect(url_for("login"))
            # remember to rehash pass
        # else:
            # session["user"] = user1
    return redirect(url_for("home")) #remember to indent correctly

@app.route("/logout/")
def logout():
    session.pop() #check which username actually logged out, or if its only one user at a time...
    return redirect(url_for("index"))

def hash(password):
    return hashlib.sha512(request.form['pass']).hexdigest()

def add_content():
    return True

if __name__ == "__main__":
    app.debug = True
    app.run()
