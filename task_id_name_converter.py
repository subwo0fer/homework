c = 'CamelCase'
c = list(c)
print(c)
d = len(c)
for i in range(1,d):
    s = str(c[i])
    print(s.isupper())
    if s.isupper():
        c.insert(i, '_')
        print('asda')
print(c)

