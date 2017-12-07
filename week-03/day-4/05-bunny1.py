# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

number = int(input('How many bunnies are we have? '))

def total_number_of_ears(number):
    if number == 0:
        return 0
    else:
        return 2 + total_number_of_ears(number-1)
    
print(number, 'bunny have', total_number_of_ears(number), 'ears')