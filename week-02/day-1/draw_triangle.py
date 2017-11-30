# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

number = int(input("Choose a number: "))
char = "*"

for i in range(number):
    print(char)
    char += "*"
    