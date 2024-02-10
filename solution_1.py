# Plastic Balance 7 kyu

# [1,2,3,4,5] ==> 1+5 != 2+3+4 ==> [2,3,4] ==> 2+4 != 3 ==> [3] ==> 3+3 != 0 ==> []
# [0,104,3,101,0,111] ==> 0+111 != 104+3+101+0 ==> [104,3,101,0] ==> 104+0 = 3+101 ==> [104,3,101,0]
def plastic_balance(lst: list) -> list:
    for num in range(len(lst)):
        if lst == []:
            return []
        elif lst[0] + lst[-1] != sum(lst[1:-1]):
            lst = lst[1:-1]
        else:
            return lst


lst = [0, 104, 3, 101, 0, 111]
print(plastic_balance(lst))
