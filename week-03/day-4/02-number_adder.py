# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.

number = int(input('Enter a number: '))
def number_add(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return number + number_add(number-1)
    
print('Sum =', number_add(number))