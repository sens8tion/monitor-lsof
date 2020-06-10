import os
import pwd
import time
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


usersList = ["all", "root", "homeassistant"]


class NumLSOF(Resource):
    def get(self):
        def num_lsof_user(user):
            if user == "all":
                stream = os.popen("lsof | wc -l")
                output = stream.read()
                return int(output) - 1
            else:
                try:
                    pwd.getpwnam(user)
                except KeyError:
                    # print('User: ' + user + ' does not exist')
                    return -1
                stream = os.popen("lsof -u " + user + " | wc -l")
                output = stream.read()
                return int(output) - 1

        row = {"time": time.asctime()}
        for user in usersList:
            print("getting user:" + user)
            row[user] = num_lsof_user(user)
        return {"lsof": row}, 200


class UsersList(Resource):
    def get(self):
        return {"users": [user for user in usersList]}, 200


class UserById(Resource):
    def get(self, id):
        return {"username": usersList[id]}


class UserByName(Resource):
    def post(self, name):
        usersList.append(name)

        return {"message": "New user added"}


api.add_resource(UsersList, "/users")
api.add_resource(UserById, "/user/<int:id>")
api.add_resource(UserByName, "/user/<string:name>")
api.add_resource(NumLSOF, "/NumLSOF")

app.run()
