# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4
a = int(input('1st number? '))
b = int(input('2nd number? '))
c = int(input('3rd number? '))
d = int(input('4th number? '))
e = int(input('5th number? '))

sum_all = a + b + c + d + e
average = int(sum_all) / 5

print(sum_all)
print(average)