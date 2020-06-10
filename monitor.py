import os
import pwd

def num_lsof_user(user):
    if user == 'all':
        stream = os.popen('lsof | wc -l')
        output = stream.read()
        return int(output)-1
    else:
        try:
            pwd.getpwnam(user)
        except KeyError:
            print('User: ' + user + ' does not exist')
            return -1
        stream = os.popen('lsof -u '+ user +' | wc -l')
        output = stream.read()
        return int(output)-1

users = ['root', 'homeassistant', 'all']
for user in users:
    print(user + ": " + str(num_lsof_user(user)))