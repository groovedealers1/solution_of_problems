def ones_complement(binary_number: str):
    # new_list = []
    # for i in binary_number:
    #     if i == '0':
    #         new_list.append('1')
    #     else:
    #         new_list.append('0')
    # return ''.join(new_list)

    return ''.join(['1' if i == '0' else '0' for i in binary_number])


number = '1001'
print(ones_complement(number))
