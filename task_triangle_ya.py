x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
d1 = (x2-x1)**2 + (y2-y1)**2
d2 = (x3-x2)**2 + (y3-y2)**2
d3 = (x3-x1)**2 + (y3-y1)**2
if d1 > d2 and d1 > d3:
    c = (d2 + d3 == d1)
elif d2 > d1 and d2 > d3:
    c = (d1 + d3 == d2)
else:
    c = (d1 + d2 == d3)
if c:
    print('yes')
else:
    print('no')
