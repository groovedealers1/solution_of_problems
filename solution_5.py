# Is this a triangle?
def is_triangle(a, b, c):
    new_list = [a, b, c]

    if 0 in new_list or a < 0 or b < 0 or c < 0:
        return False

    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


a, b, c = 1, 2, 3
print(is_triangle(a, b, c))