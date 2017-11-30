# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4

test_nr = int(input("Enter a number between 1-15: "))
result = 0

for i in range(test_nr):
    summa = int(input("Enter a number: "))
    result += test_nr
    
print('Sum: ', result)
print('Average: ', result / test_nr)