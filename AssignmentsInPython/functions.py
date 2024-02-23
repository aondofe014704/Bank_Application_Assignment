def list_of_numbers(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o):

    return a, b, c, d, e, f, g, h, i, j, k, l, m, n, o

#print(list_of_numbers(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))

def my_numbers_list():

    return 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15

    print(my_numbers_list())


def my_list():
    list_numbers = []
    for numz in range(15,31):
        list_numbers.append(numz)

    return list_numbers
print(my_list())


def reversed_list():
    value = list(range(1,10))

    return value[::-1]

print(reversed_list())