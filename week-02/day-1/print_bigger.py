# Write a program that asks for two numbers and prints the bigger one

num1 = int(input('Choose a number: '))
num2 = int(input('Choose another number: '))

if int(num1) > int(num2):
    print(num1)
elif int(num1) < int(num2):
    print(num2)
elif int(num1) == int(num2):
    print('The numbers are equal!')
    