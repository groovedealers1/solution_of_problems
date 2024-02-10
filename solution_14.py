# 7 kyu
import math

def cooking_time(eggs):
    if eggs <= 8:
        return 5
    else:
        return 5 * math.ceil(eggs / 8)


eggs = 20
print(cooking_time(eggs))