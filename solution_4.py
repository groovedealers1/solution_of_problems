# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
def double_char(s):
    new_str = ''
    for i in s:
        new_str += i * 2

    return new_str


s = 'Hello World'
print(double_char(s))