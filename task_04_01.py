with open('data.txt') as f:
    ish_dat = f.readline().split()

n = int(input())
p = int(input())

with open('out-1.txt', 'w') as f:
    for number in ish_dat:
        if int(number) % n == 0:
            del_bez_ost = str(number) + ' '
            f.write(del_bez_ost)

with open('out-2.txt', 'w') as f:
    for number in ish_dat:
        vozv_v_step = str(int(number) ** p) + ' '
        f.write(vozv_v_step)
