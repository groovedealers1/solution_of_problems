# Driving School Series #1   7 kyu

def foo(s):
    if len([num for num in s if num <= 18]) == 0:
        return 'No pass scores registered.'
    else:
        return round(sum([num for num in s if num <= 18]) / len([num for num in s if num <= 18]))


s = [10, 10, 10, 18, 20, 20]
print(foo(s))