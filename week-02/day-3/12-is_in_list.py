# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]

def is_in_list(list_of_numbers):
    myItem1 = 4
    myItem2 = 8
    myItem3 = 12
    myItem4 = 16
    if myItem1 in list_of_numbers and myItem2 in list_of_numbers and myItem3 in list_of_numbers and myItem4 in list_of_numbers:
        print(True)
    else:
        print(False)

print(is_in_list(list_of_numbers))