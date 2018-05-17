import hashlib

cache = ''

def make_token(username, password):
    s = username + password
    return hashlib.md5(s.encode()).hexdigest()

def login_required(func):
    def wrapper(*args, **kwargs):
        global cache
        with open('token.txt') as f:
            req_log_pass = f.readline()
        n = 3
        if cache != req_log_pass:
            while n:
                login = input()
                password = input()
                user_token = make_token(login, password)
                if user_token == req_log_pass:
                    cache = req_log_pass
                    break
                n -= 1
        if cache == req_log_pass:
            return func(*args, **kwargs)
        else:
            return None
    return wrapper


@login_required
def f1(a, b):
    return a, b

@login_required
def f2(a, b):
    return a, b


print(f1(10, 20))
print(f2(30, 40))
