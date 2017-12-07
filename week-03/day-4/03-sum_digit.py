# Given a non-negative int n, return the sum of its digits recursively (no loops). 
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while 
# divide (/) by 10 removes the rightmost digit (126 // 10 is 12).

number = int(input('Enter a non-negative int: '))

def sum_digit(number):
    if number < 0:
        return 'Enter a non-negative int!'
    elif number <= 10:
        return number
    else:
        return sum_digit(number // 10) + number % 10
    
print('Sum =', sum_digit(number))