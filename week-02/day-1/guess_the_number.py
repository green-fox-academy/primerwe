# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stored number is lower
# You found the number: 8

storedNumber = 13

guessedNumber = int(input('Choose a number: '))

if int(storedNumber) > int(guessedNumber):
    print('The stored number is higher')
elif int(storedNumber) < int(guessedNumber):
    print('The stored number is lower')
else:
    print('You found the number: 13')
