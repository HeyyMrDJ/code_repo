'''
Challenge to return ratio of
pos, neg, zero numbers to number of elements in a list
'''

arr = [1, 1, 0, -1, -1]


def int_ratio(my_list: list):
    'Test'
    pos_num = 0
    neg_num = 0
    zero_num = 0
    for num in my_list:
        if num == 0:
            zero_num += 1
        if num > 0:
            pos_num += 1
        if num < 0:
            neg_num += 1

    return pos_num/len(my_list), neg_num/len(my_list), zero_num/len(my_list)


a, b, c = int_ratio(arr)

print(f"{a:06f}\n{b:06f}\n{c:06f}")
