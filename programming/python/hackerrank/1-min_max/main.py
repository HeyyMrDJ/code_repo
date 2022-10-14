'Script to find largest and smallest sums in a list'

list2 = [1, 2, 3, 4, 5]


def min_max(list1: list) -> list and list:
    'Function to find minimum and maximum sums out of the list -1 number'

    list1.sort()
    large_list = list1[:]
    large_list.pop(0)
    small_list = list1[:]
    del small_list[-1]
    return small_list, large_list


my_list1, my_list2 = min_max(list2)
print(f"{sum(my_list1)} {sum(my_list2)}")
