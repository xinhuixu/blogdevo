from flask import Flask, redirect, request, render_template, session, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(15)

@app.route("/")
def index():

@app.route("/login/")
def login():
    
