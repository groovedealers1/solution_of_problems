# Your task is to complete the function which takes a string,
# and returns an array with all possible rotations of the given string, in uppercase.

def scrolling_text(text):
    new_list = [text.upper()]

    for i in range(len(text) - 1):
        new_list.append(text[i + 1:].upper() + text[:i+1].upper())

    return new_list


text = "codewars"
print(scrolling_text(text))
