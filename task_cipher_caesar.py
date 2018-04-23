def encode(user_t, user_s):
    resultat = ''
    for i in range(len(user_t)):                                   		#Основной цикл проходит от 1 до последнего символа
        if ord(user_t[i]) >= (97) and ord(user_t[i]) <= (122):     		#Проверка что символ маленький
            
            if ord(user_t[i]) + user_s > 122:                      		#Если символ маленький то проверяем что его номер со смещением не превышает 122
                resultat = resultat + chr(ord(user_t[i]) + user_s - 26)  	#Если он все-таки больше то смещаем его на 26 назад и записываем в результат
            else:
                 c = ord(user_t[i]) + user_s                       		#А если он не превышает 122 то просто записываем его в результат без смещения
                 resultat = resultat + (chr(c)) 
            

        elif ord(user_t[i]) >= (65) and ord(user_t[i]) <= (90):    		#Если символ оказался не маленький то проверяем что он большой 
            
            if ord(user_t[i]) + user_s > 90:                       		#Если символ большой то проверяем что его номер со смещением не превышает 90
                resultat = resultat + (chr(ord(user_t[i]) + user_s - 26)) 	#Если он все-таки больше 90 то смещаем его на 26 назад и записываем в результат
            else:
                 c = ord(user_t[i]) + user_s                         		#А если он не превышает 90 то просто записываем его в результат без смещения
                 resultat = resultat + (chr(c)) 

        else:
            resultat = resultat + (user_t[i])                       		#если символ не большой и не маленький то не меняя его записываем в результат
    return resultat

def decode(user_t, user_s):
    resultat = ''
    for i in range(len(user_t)):                                   		#Основной цикл проходит от 1 до последнего символа
        if ord(user_t[i]) >= (97) and ord(user_t[i]) <= (122):     		#Проверка что символ маленький
            
            if ord(user_t[i]) - user_s < 97:                      		#Если символ маленький то проверяем что его номер со смещением не меньше 97
                resultat = resultat + chr(ord(user_t[i]) - user_s + 26)  	#Если он все-таки меньше то смещаем его на 26 вперед и записываем в результат
            else:
                 c = ord(user_t[i]) - user_s                       		#А если он не меньше 97 то просто записываем его в результат без смещения
                 resultat = resultat + (chr(c)) 
            

        elif ord(user_t[i]) >= (65) and ord(user_t[i]) <= (90):    		#Если символ оказался не маленький то проверяем что он большой 
            
            if ord(user_t[i]) - user_s < 65:                       		#Если символ большой то проверяем что его номер со смещением не меньше 65
                resultat = resultat + (chr(ord(user_t[i]) - user_s + 26)) 	#Если он все-таки меньше 65 то смещаем его на 26 вперед и записываем в результат
            else:
                 c = ord(user_t[i]) - user_s                         		#А если он не меньше 65 то просто записываем его в результат без смещения
                 resultat = resultat + (chr(c)) 

        else:
            resultat = resultat + (user_t[i])                       		#если символ не большой и не маленький то не меняя его записываем в результат

    return resultat
