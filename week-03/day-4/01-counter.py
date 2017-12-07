# Write a recursive function that takes one parameter: n and counts down from n.

number = int(input('Enter a number: '))

def re_countdown(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return str(number) + ' , ' + str(re_countdown(number-1))
    
print (re_countdown(number))