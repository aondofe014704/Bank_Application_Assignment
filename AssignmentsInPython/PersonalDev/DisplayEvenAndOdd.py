user_number = int(input("please Enter a number : "))
sum_odd = 0
sum_even = 0
for index in range(1, user_number):
    if user_number % 2 == 0:
        sum_even+=user_number
        print(sum_even)
for number in range(1, user_number):
    if user_number % 2 != 0:
        sum_odd+=user_number
        print(sum_odd)






