# Take an array and remove every second element from the array. Always keep the first element and start removing with
# the next element

def remove_every_other(my_list):
    return [my_list[i] for i in range(len(my_list)) if i % 2 == 0]


my_list = ["Keep", "Remove", "Keep", "Remove", "Keep",]
print(remove_every_other(my_list))