import graphyte
import os
import pwd
import time


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


usersList = ["all", "root", "homeassistant"]
grafitehost = "edsoft.duckdns.org"

graphyte.init(grafitehost, prefix="stats.ha.lsof")

while True:
    time.sleep(4)
    for user in usersList:
        lsof = num_lsof_user(user)
        # print(f"{user} open files: {lsof}")
        graphyte.send(user, num_lsof_user(user))
