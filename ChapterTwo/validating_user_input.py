
number_of_passes = 0
number_of_failures = 0

for number in range(10):
    result = int(input("Enter result : (1 = pass, 2 = fail): "))
    if result != 1 and result != 2:
        print("please Enter the correct scores")
    if result == 1:
        number_of_passes += 1
    if result == 2:
        number_of_failures += 1

if number_of_passes > 8:
    print("Kudos to the instructor")
