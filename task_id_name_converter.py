def camel_to_snake(name):
    resultat = ''
    resultat += name[0]
    for i in range(1, len(name)):
        if (ord(name[i]) >= 65) and (ord(name[i]) <= 90):
            resultat = resultat + chr(95)
        resultat += name[i]
    return resultat.lower()

def snake_to_camel(name):
    resultat = ''
    resultat += chr(ord(name[0]) - 32)
    for i in range(1, len(name)):    
        if ord(name[i]) >= 97 and ord(name[i]) <= 122:
            if ord(name[i-1]) != 95: 
                resultat += name[i]
        elif ord(name[i]) == 95:
            resultat += chr(ord(name[i+1]) - 32)
    return resultat
