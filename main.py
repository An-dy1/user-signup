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


#functions needed to verify:
# function to make sure something is input
# len() - length of a string
# function to check no special characters or spaces
# email criteria: single @, single . , contains no spaces, between 3 and 20 characters

@app.route("/" methods=["POST"])
def index():

    username = request.form.get["username"]
    password = request.form.get["password"]
    verify_password = request.form.get["verify_password"]
    email = request.form.get["email"]

    if not is_username(username):
        username_error = "That's not a valid username. Make sure it's between 3 and 20 characters and contains no special characters"
        username = ""
    else: 
        username = username # is this right??

    if not is_password(password):
        password_error = "That's not a valid password."
        password = ""
    else:
        password = password #is this right?

    if not is_matching_password(verify_password, password):
        matching_password_error = "Passwords don't match"
        verify_password = ""
    else:
        verify_password = verify_password #is this right?

    if not is_email(email):
        email_error = "That's not a valid email"
        email = ""
    else:
        email = email #is this right?

    if not username_error and not password_error and not matching_password_error and not email_error:
        name = username
        return redirect("/welcome?name={0}".format(name)) #look carefully here
    else:
        template = jinja_env.get_template("main-form.html")
        return template.render(username_error=username_error,
        password_error=password_error,
        matching_password_error=matching_password_error,
        email_error=email_error)


@app.route("/welcome" methods=["POST"])
def welcome():
    return render_template("welcome.html")