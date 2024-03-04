from AssignmentsInPython.Character_Format_Error import CharacterFormatError
from AssignmentsInPython.binary_format_error import BinaryFormatError
from AssignmentsInPython.invalid_length_error import InvalidLengthError


class SevenSegmentDisplay:
    def my_segment(self, binary_number: str):
        my_list = []
        if not binary_number.isnumeric():
            raise CharacterFormatError("Characters not valid inputs here, please Enter Number from 0 to 1")
        if len(binary_number) != 8:
            raise InvalidLengthError("invalid length")
        for i in binary_number:
            if i != '1' or 'i' != 0:
                raise BinaryFormatError("Invalid input, please Enter Number from 0 to 1")
        for i in range(0, len(binary_number)):
            my_list.append(binary_number[i])
        if my_list[0] == '1':
            print(" # # # # #")
        if my_list[5] and my_list[1] == '1':
            for i in range(5):
                print("#         #")
        elif my_list[5] == '0' and my_list[1] == '1':
            for i in range(5):
                print("          #")
        elif my_list[5] == '1' and my_list[1] == '0':
            for i in range(5):
                print("#        ")
        if my_list[6] == '1':
            print(" # # # # #")
        if my_list[4] == 0 and my_list[2] == 1:
            for i in range(5):
                print("#         #")
        elif my_list[4] and my_list[2] == '0':
            for i in range(5):
                print("          #")
        elif my_list[4] and my_list[2] == '0':
            for i in range(5):
                print("#          ")
        if my_list[3] == '1':
            print(" # # # # #")
