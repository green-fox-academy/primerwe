# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was

number = int(input("Choose a number: "))
char = "*"

for i in range(number):
    if number > 0:
        print((number - 1) * ' ' + char * (i * 2 + 1))
        i += 1
        number -= 1
    else:
        print("Choose a bigger number!")
