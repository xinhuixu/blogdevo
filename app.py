from flask import Flask, redirect, request, render_template, session, url_for
import os

app = Flask(__name__)
app.secret_key = '\xf35{\x12\x1c\xc7;\xf0\xd1x\x8d8\xe7f\xa3'

@app.route("/")
def index():
    for user in session:
        return redirect(url_for("login"))
    return redirect(url_for("home"))

@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/home/")
def home():
    return render_template("home.html") #stuff = username

@app.route("/auth/", methods=["POST"])
def auth():
     i = 0
    for arg in request.form:
        i += 1 
    if i == 0:
        return redirect(url_for("login"))
   return redirect(url_for("home"))

if __name__ == "__main__":
    app.debug = True
    app.run()
