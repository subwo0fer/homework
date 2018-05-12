n = int(input())
p = int(input())

with open('data.txt') as f:
    ish_dat = f.readline().split()

with open('out-1.txt', 'w') as f:
    for number in ish_dat:
        if int(number) % n == 0:
            f.write(str(number) + ' ')

with open('out-2.txt', 'w') as f:
    for number in ish_dat:
        f.write(str(int(number) ** p) + ' ')
