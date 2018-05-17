from collections import namedtuple

def return_namedtuple(*args):
    bufer = args
    def decorator(func):
        def wrapper(*args, **kwargs):
            func_result = func(*args, **kwargs)
            if isinstance(func_result, tuple):
                stroka = (bufer)
                Na_tup = namedtuple('Na_tup', stroka)
                dict = {}
                for i in range(len(stroka)):
                    dict.update({stroka[i]:func_result[i]})
                d = Na_tup(**dict)
                return d
            else:
                print('Вы передали в декоратор не кортеж')
                return(func_result)
        return wrapper
    return decorator
