def sum_collection(new_set: set):
    total = 0
    for index in range(0, len(new_set)):
        total += index
    return total

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
print(sum_collection(my_set))


x = "python is fun"
print(x[10:])