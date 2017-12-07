# We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
# (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
# have 3 ears, because they each have a raised foot. Recursively return the
# number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

number = int(input('How many bunnies are we have? '))

def total_number_of_ears(number):
    if number == 0:
        return 0
    if number % 2 == 0:
        return 3 + total_number_of_ears(number-1)
    else:
        return 2 + total_number_of_ears(number-1)
    
print(number, 'bunny have', total_number_of_ears(number), 'ears')