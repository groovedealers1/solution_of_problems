def reverse_number(n):
    if str(n)[0] == '-':
        return str(n)[0] + str(n)[:0:-1]
    elif str(n)[::-1][0] == '0':
        return int(str(n)[::-1])
    else:
        return str(n)[::-1]


n = -123
print(reverse_number(n))

