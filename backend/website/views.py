from flask import Blueprint
from flask import request
from Vjudge_api import get_vjudge_data
from .models import ProgressPerContest
from website import errors
import werkzeug
from . import db
from .__init__ import urls
from .models import User
import json

views = Blueprint("views", __name__)

@views.route(urls['PROGRESS_PER_CONTEST'], methods=["POST"], strict_slashes=False)
def get_progress_per_contest():
    print("here")
    contest_id = request.json["contestID"]
    print(contest_id)
    problemCount = ProgressPerContest.getProblemCount(contest_id=contest_id)
    print('#Problems:',problemCount)
    trainees = User.getVjudge_Handles()
    for trainee in trainees:
        id = trainee["user_id"]
        vjudge = trainee["vjudge_handle"]
        print(id, vjudge)
        res = get_vjudge_data(contest_id = contest_id,username=vjudge,result=1)
        filtered_res = {}
        for x in res:
            filtered_res[(x['problemId'],x['userName'])] = x
            #print(x)
        numSolved = len(filtered_res)
        print("Solved:",numSolved)
        zone = ProgressPerContest.getZone(problemCount=problemCount,solved=numSolved)
        print(zone)
        ProgressPerContest.addProgressPerContest(id,contest_id,numSolved,zone)
    return " "

@views.route(urls['PROFILE'], methods = ["GET"], strict_slashes=False)
def displayProfile():
    email = request.args.get("email")
    # if(User.exists(email)==False):
    #     return errors.email_doesnt_exist(werkzeug.exceptions.BadRequest)
    print (email)
    user = User(email = email)

#     #return user as json object
#    return user.json.dumps(user._dict_)
    ret = json.dumps(user.__dict__)
    # console.log ("heeellooooo")
    print (ret)
    return json.dumps(user.__dict__)


@views.route(urls['PROFILE'], methods = ["POST"], strict_slashes=False)
def editProfile():

    email = request.json["email"]
    name = request.json["name"]
    vjudge_handle = request.json["vjudgeHandle"]
    password = request.json["password"]
    User.updatePassword(email, password)
    mycursor = db.cursor()
    query = "UPDATE user SET vjudge_handle=%s, name=%s, password=%s WHERE email=%s;"
    mycursor.execute(query, (vjudge_handle, name, password, email,))
    db.commit()
    #how to redirect to profile after update?
    #redirect ('/profile')
    return {"hereeee": "here"}

@views.route(urls['USERS'], methods = ["GET"], strict_slashes=False)
def getUsers():
    print('in method')
    role = request.args.get("role")
    print(role)
    return {"hellow": "heloo"}