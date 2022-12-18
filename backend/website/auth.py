import json

from app import create_app
from flask import Blueprint, request
from flask_login import current_user, login_required, login_user, logout_user
from website import errors
from werkzeug.security import check_password_hash, generate_password_hash
import werkzeug
import pandas as pd
import os

from .models import User, permissions

auth = Blueprint("auth", __name__)

remember_logins = False     # consider changing this to true

# Defining functionality for "/data" endpoint
@auth.route('/data', methods=["GET"], strict_slashes=False)
def get_data():
    return {
		"X":"dataaa"
		}


@auth.route("/login", methods=["POST"], strict_slashes=False)
def login():

    email = request.json["email"]
    password = request.json["password"]
    
    user = User(email = email)

    if user:
        if check_password_hash(user.password, password):
            print("Logged in!")
            login_user(user,remember = remember_logins)
            perm = permissions(user)
            user_json = json.dumps(user.__dict__)
            permissions_json = json.dumps(perm.__dict__)
            print(user_json)
            print(permissions_json)
            # return redirect(url_for('views.home'))
        else:
            print("Password incorrect!")
            return errors.incorrect_password(werkzeug.exceptions.BadRequest)
    else:
        print("Email does not exist")
        return errors.email_doesnt_exist(werkzeug.exceptions.BadRequest)
    # TODO what to return here
    return {"email" : email,"password" : password}

@auth.route("/userentry", methods=["POST"], strict_slashes=False)
def register():
    name = request.json["firstName"]+" "+request.json["lastName"]
    email = request.json["email"]
    password = "password123"
    vjudge = request.json["vjudgeHandle"]
    role = request.json["platformRole"]

    if User.exists(email):
        print("user already registered")
    else:
        User.addUser(vjudge_handle = vjudge,name = name,
                    email = email, level = 1,role = role,
                    active = True, points = 0,
                    password = generate_password_hash(password, method='sha256'))
        print("User added successfully")
    # TODO what to return here?
    return {"email" : email,"password" : password}

@auth.route("/userentryfile", methods=["POST"], strict_slashes=False)
def registerfile():
   
    file = request.files.get("excel-file")
    df = pd.DataFrame(pd.read_excel(file))
    for i, row in df.iterrows():
        vjudge = row["vjudge"]
        email  = row["email"]
        password = "password123"
        name = row["name"]
        role = "Trainee"
        # print(name,email,password)
        if User.exists(email):
            print(email)
            print("user already registered")
        else:
            User.addUser(vjudge_handle = vjudge,name = name,
                    email = email, level = 1,role = role,
                    active = True, points = 0,
                    password = generate_password_hash(password, method='sha256'))
            print("User added successfully")
        
    # f = file.read()
    # print(f)
    # workbook = pd.DataFrame(f)
    # workbook.head()

    
    # TODO what to return here?
    return " " #{"email" : email,"password" : password} 
