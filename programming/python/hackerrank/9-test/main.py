import statistics
list1 = [0, 1, 2, 4, 6, 5, 3]
n = 7
def my_func(x, list1):
    y = statistics.median(list1)
    # return int(y / x)
    return y

print(my_func(n, list1))
