def square(number):
    return number ** 2

print("The square of 7 is :", square(7))

print("The square of 2.5 is : ", square( 2.5))


"""Return the maximum of the three values."""

def maximum(value1, value2, value3):
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
            max_value = value3
    return max_value

print(maximum(12, 34, 56))

print(maximum(12.3, 45.6, 9.7))

print(maximum('Yellow', 'Red', 'Orange'))

print(maximum(13.5, -3, 7))
