from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def display_user_signup():
    return render_template("main-form.html")

# function to make sure something is input:
def something_input(string):
    try:
        good_length == len(string) > 0
        return good_length
    except: 
        return False

# len() - length of a string between 3 and 20:
def good_length(string):
    try:
        good_string == (len(string) > 3 and len(string) < 20)
        return good_string
    except:
        return False

#function to check no spaces:
def no_spaces(string):
    try:
        no_spaces == (" " not in string)
        return no_spaces
    except: 
        return False

#check for one @ symbol
def one_at(email):
    ats = []

    for char in email:
        if char is "@":
            ats += char

    try: 
        good_ats == (len(ats) is 1)
        return good_ats
    except:
        return False        

#check for one .
def one_dot(email):
    dots = []

    for char in email:
        if char is ".":
            dots += char

    try:
        good_dots == (len(dots) is 1)
        return good_dots
    except:
        return False

def is_username(username):
    try:
        good_username == something_input(username) and good_length(username) and no_spaces(username)
        return good_username
    except:
        return False
    
def is_password(password):
    try:
        good_password == something_input(password) and good_length(password) and no_spaces(password)
        return good_password
    except:
        return False

def is_matching_password(verify_password, password):
    try:
        verified_pw == (verify_password == password)
        return verified_pw
    except:
        return False

def is_email(email):
    if not something_input(email):
        return True
    else:
        try:
            good_email == (no_spaces(email) and good_length(email) and one_dot(email) and one_at(email))
            return good_email
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
    verify_password_error = ""
    email_error = ""

    if not is_username(username):
        username_error = "That's not a valid username."
        username = ""

    if not is_password(password):
        password_error = "That's not a valid password."
        password = ""

    if not is_matching_password(verify_password, password):
        verify_password_error = "Passwords don't match."
        verify_password = ""

    if not is_email(email):
        email_error = "That's not a valid email."
        email = ""

    if not username_error and not password_error and not matching_password_error and not email_error:
        name = username
        return redirect("/welcome?name={0}".format(name))
    else:
        return render_template("main-form.html", username_error=username_error,
        password_error=password_error,
        verify_password_error=verify_password_error,
        email_error=email_error)

@app.route("/welcome")
def welcome():
    name = request.args.get("name")
    return "<h1>Welcome, {0}!</h1>".format(name)

app.run()