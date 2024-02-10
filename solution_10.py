
def make_string(s):
    return ''.join([i[0] for i in s.split(' ')])


s = "This Is A Test"
print(make_string(s))