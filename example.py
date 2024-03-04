def display_segment():
    list1 = [1,1,0,0,1,1,0,1]
    if list1[0] == 1:
        print(" # # # # #")
    if list1[5] and list1[1] == 1:
        for i in range(5):
            print("#          #")
    elif list1[5] == 0 and list1[1] == 1:
        for i in range(5):
            print("          #")
    elif list1[5] == 1 and list1[1] == 0:
        for i in range(5):
            print("#          ")
    if list1[6] == 1:
        print(" # # # # #")
    if list1[4] and list1[2] == 1:
        for i in range(5):
            print("#          #")
    elif list1[4] and list1[2] == 1:
        for i in range(5):
            print("          #")
    elif list1[4] == 1 and list1[2] == 0:
        for i in range(5):
            print("#          ")
    if list1[3] == 1:
        print(" # # # # #")


display_segment()