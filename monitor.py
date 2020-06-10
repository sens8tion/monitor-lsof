import os
import pwd
import time
from datetime import datetime
import json


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


users = ["all", "root", "homeassistant"]
time_between_readings = 60
output = "/tmp/lsof.log"
while True:
    row = {"time": time.asctime()}
    sleeptime = time_between_readings - datetime.utcnow().second
    time.sleep(sleeptime)
    for user in users:
        row[user] = num_lsof_user(user)
    with open(output, "a") as file_object:
        file_object.write(json.dumps(row) + "\n")
