tarelki = int(input())
sredstvo = int(input())
if (tarelki / 2) > sredstvo:
    a = sredstvo * 2
else:
    a = tarelki 
for i in range(a):
    sredstvo -= 0.5
    tarelki -= 1
if sredstvo <= 0 and tarelki <= 0:
    print('Все тарелки вымыты, моющее средство закончилось')
elif tarelki <= 0:
    print('Все тарелки вымыты. Осталось', sredstvo, 'ед. моющего средства')
else:
    print('Моющее средство закончилось. Осталось', tarelki, 'тарелок')
