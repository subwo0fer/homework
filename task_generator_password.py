import random

def password_generator(length):
    while True:
        password = ''
        for i in range(length):
            password += chr(random.randint(33, 126))
        yield password
