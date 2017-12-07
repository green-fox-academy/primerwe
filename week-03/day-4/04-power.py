# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

number = int(input('Enter a non-negative int: '))
power = int(input('Enter a non-negative int: '))

def power_number(number, power):
    if number == 0:
        return 0
    if power == 0:
        return 1
    if number == 1 or power == 1:
        return number
    else:
        return number * power_number(number, power-1)

print('The ' + str(power) + 'nd/rd/nth power of ' + str(number) + ' is: ' + str(power_number(number, power)))