def foo(func: list, arr: list):
    new_list = []
    for i in range(len(func)):
        if 'lambda' in str(func[i]):
            s = func[i]
            for u in arr:
                if s(u):
                    new_list.append(u)

    return new_list


my_list = [lambda a: a % 2 == 0, 9, 3, 1, 0]
my_array = [1, 2, 3, 4]
print(foo(my_list, my_array))

