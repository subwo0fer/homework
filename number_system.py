def dec2bin(number):  #Из десятичной в двоичную
    buf2 = ''
    while number > 0:
        buf2 += str(number % 2)
        number //= 2
    buf2 = buf2[::-1]
    return buf2

def dec2oct(number): #Из десятичной в восьмиричную
    buf2 = ''
    while number > 0:
        buf2 += str(number % 8)
        number //= 8
    buf2 = buf2[::-1]
    return buf2


def dec2hex(number): #Из десятичной в шестнадцатиричную
    buf2 = ''
    while number > 0:
        if number % 16 > 9:
            buf2 += chr((number % 16) + 55)
        else:
             buf2 += str(number % 16)
        number //= 16
    buf2 = buf2[::-1]
    return buf2

def bin2dec(number): #Из двоичной в десятичную
    buf = len(str(number))
    num_str = str(number)
    buf2 = 0
    for i in range(buf):
        st = i + 1
        buf2 += int(num_str[i]) * 2 ** (buf - st)
    return buf2

def oct2dec(number): #Из восьмиричной в десятичную
    buf = len(str(number))
    num_str = str(number)
    buf2 = 0
    for i in range(buf):
        st = i + 1
        buf2 += int(num_str[i]) * 8 ** (buf - st)
    return buf2

def hex2dec(number): #Из восьмиричной в десятичную
    buf = len(str(number))
    buf2 = 0
    for i in range(buf):
        if 65 <= ord(number[i]) <= 70:
            buf3 = ord(number[i]) - 55
        elif 97 <= ord(number[i]) <= 102:
            buf3 = ord(number[i]) - 87
        else:
            buf3 = int(number[i])
        st = i + 1
        buf2 += buf3 * 16 ** (buf - st)
    return buf2
