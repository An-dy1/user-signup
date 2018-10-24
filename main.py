from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def display_user_signup():
    return render_template("main-form.html")

#functions needed to verify:

# function to make sure something is input:
def something_input(string):
    try:
        len(string) > 0
        return True
    except:
        return False

# len() - length of a string between 3 and 20:
def good_length(string):
    try:
        len(string) > 3 and len(string) < 20
        return True
    except:
        return False

#function to check no spaces:
def no_spaces(string):
    try:
        " " not in string
        return True # or not in word
    except: 
        return False

#check for one @ symbol
def one_at(email):
    ats = []

    for char in email:
        if char is "@":
            ats += char

    try: 
        len(ats) == 1
        return True
    except:
        return False        

#check for one .
def one_dot(email):
    dots = []

    for char in email:
        if char is ".":
            dots += char

    try:
        len(dots) == 1
        return True
    except:
        return False

#passwords match:
def passwords_match(password, verify_password):
    try:
        password == verify_password
        return True #or something like this!
    except: 
        return False

def is_username(username):
    try:
        something_input(username) and good_length(username) and no_spaces(username)
        return True
    except:
        return False
    
def is_password(password):
    try:
        something_input(password) and good_length(password) and no_spaces(password)
        return True
    except:
        return False

def is_matching_password(verify_password, password):
    try:
        verify_password == password
        return True
    except:         #need to name some sort of error here?
        return False

def is_email(email):
    if not something_input(email):
        return True
    else:
        try:
            no_spaces(email) and good_length(email) and one_dot(email) and one_at(email)
            return True
        except:
            return False

@app.route("/", methods=["POST"])
def index():

    username = request.form.get("username")
    password = request.form.get("password")
    verify_password = request.form.get("verify_password")
    email = request.form.get("email")

    username_error = ""
    password_error = ""
    matching_password_error = ""
    email_error = ""

    if not is_username(username):
        username_error = "That's not a valid username. Make sure it's between 3 and 20 characters and contains no special characters"
        username = ""

    if not is_password(password):
        password_error = "That's not a valid password."
        password = ""

    if not is_matching_password(verify_password, password):
        matching_password_error = "Passwords don't match."
        verify_password = ""

    if not is_email(email):
        email_error = "That's not a valid email."
        email = ""

    if not username_error and not password_error and not matching_password_error and not email_error:
        name = username
        return redirect("/welcome?name={0}".format(name))
    else:
        return render_template(username_error=username_error,
        password_error=password_error,
        matching_password_error=matching_password_error,
        email_error=email_error)

@app.route("/welcome")
def welcome():
    name = request.args.get("name")
    return "<h1>Welcome, {0}!</h1>".format(name)

app.run()