# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was

number = int(input("Choose a number: "))

for i in range(number-1):
    print((number - i) * ' ' + '*' * ((i * 2) + 1))
for i in range(number-1, -1, -1):
    print((number - i) * ' ' + '*' * ((i * 2) + 1))