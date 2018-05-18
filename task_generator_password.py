import random

def password_generator(length):
    password = ''
    for i in range(length):
        password += chr(random.randint(33, 126))
    return password
