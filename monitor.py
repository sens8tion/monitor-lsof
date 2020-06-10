import os

def num_lsof_user(user):
    stream = os.popen('lsof -u '+ user +' | wc -l')
    output = stream.read()
    return int(output)-1

users = ['root', 'johnedwards']
for user in users:
    print(f"{user}: {num_lsof_user(user)}")