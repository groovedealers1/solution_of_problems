# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

def alphabet_position(text):
    new_list = []
    new_str = ' '
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for symbol in text:
        if symbol in alphabet or symbol in alphabet.upper():
            for i in range(len(alphabet)):
                if symbol == alphabet[i] or symbol == alphabet.upper()[i]:
                    new_list.append(str(i + 1))

    return new_str.join(new_list)


text = "The sunset sets at twelve o' clock."
print(alphabet_position(text))
