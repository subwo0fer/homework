def average(lst):
    d = 0
    for i in range(len(lst)):
        d += float(lst[i])
    d = d/len(lst)
    d = round(d, 3)
    return d
