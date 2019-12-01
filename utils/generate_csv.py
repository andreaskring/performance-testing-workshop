import string
import random


N = 50

def pwd(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

users = [
    'user{},{}\n'.format(i, pwd()) for i in range(N)
]

with open('../jmeter/users.csv', 'w') as f:
    f.writelines(users)

