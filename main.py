from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


def is_username(username): #username and password validations are the same, but how do I check several things in a try/except block?
    
def is_password(password):

def is_matching_password(verify_password, password):
    try:
        verify_password == password
        return True
    except:         #need to name some sort of error here?
        return False

def is_email(email):

@app.route("/" methods=["POST"])
def index():

    username = request.form.get["username"]
    password = 



@app.route("/welcome" methods=["POST"])
def welcome():
    return render_template("welcome.html")