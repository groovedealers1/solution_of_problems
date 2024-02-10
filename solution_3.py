def mean(lst):
    a = [0, '']

    for i in lst:
        try:
            a[0] += int(i)
        except ValueError:
            a[1] += i
    a[0] = a[0] / 10
    return a


lst = ['u', '6', 'd', '1', 'i', 'w', '6', 's', 't', '4', 'a', '6', 'g', '1', '2', 'w', '8', 'o', '2', '0']
print(mean(lst))
