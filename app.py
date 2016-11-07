from flask import Flask, redirect, request, render_template, session, url_for, flash
import os
from utils import db_builder
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = '\xf35{\x12\x1c\xc7;\xf0\xd1x\x8d8\xe7f\xa3'


@app.route("/")
def index():
    if 'username' in session:
        username = session['username']
        print '!SESSION_STATUS: ' + username
        return redirect(url_for("home"))
    print '!SESSION_STATUS: session is empty'
    return redirect(url_for("login"))

@app.route("/login/")
def login():
    #for user in session:
        #return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/home/", methods=["POST"])
def home():
    print '!SESSION_STATUS: ' + session['username']
    l = db_builder.open_stories(session['username'])
    if "new_story" in request.form:
        new_story(db_builder.ctr())
        return redirect(url_for("home"))
    if "my_stories" in request.form:
        l = db_builder.get_mystory(session['username'])
    return render_template("home.html", stories = l) 

@app.route("/auth/", methods=["POST"])
def auth():
    ## register
    #print request.form
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
        elif (db_builder.get_hash(request.form['username']) == request.form['password']):
            user1 = request.form['username']
            session['username'] = user1
            print '!SESSION_STATUS: ' + session['username']
            return redirect(url_for("home"))
        else:
            flash("incorrect username and password combination")
            return redirect(url_for("login"))

@app.route("/logout/", methods=["GET"])
def logout():
    if "logout" in request.args:
        try:
            session.pop('username')
        except:
            return 'logout error'
    return redirect(url_for('index'))

def hashp(password):
    return hashlib.sha512(password).hexdigest()

def add_content(id1):
    db_builder.add_to_story(id1,session['username'],request.form["add_content"])

def new_story(id1):
    db_builder.new_story(id1, session['username'], request.form["add_content"])

@app.route("/story/<int:id1>")
def story(id1):
    title = db_builder.get_title(id1)
    author= db_builder.get_author(id1)
    can_add = db_builder.check_cont(id1, session['username'])
    content = db_builder.get_update(id1)
    if can_add:
        return render_template("story.html", title = title, content = content, user = session['username'], author = author, can_add = can_add)
    else:
        fstory = db_builder.get_contents(id1)
        return render_template("story.html", title = title, content = fstory, user = session['username'], author = author, can_add = can_add)

if __name__ == "__main__":
    app.debug = True
    app.run()
