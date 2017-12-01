#Write a simple program to check if a given number is an armstrong number. 
#The program should ask for a number. 
#Let's demonstrate this for a 4-digit number: 1634 is a 4-digit number, raise each digit to the fourth power, and add: 1^4 + 6^4 + 3^4 + 4^4 = 1634, so it is an Armstrong number.
#For a 3-digit number: 153 is a 3-digit number, raise each digit to the third power, and add: 1^3 + 5^3 + 3^3 = 153, so it is an Armstrong number.
#E.g. if we type 371, the program should print out: The 371 is an Armstrong number.

num = (input("Enter a number: "))

def armstrong_number(num):
    #raise each digit to the nth power
    power_l = [ int(x) ** (len(num)) for x in num ]
    
    #add them up
    output = 0
    for p in power_l:
        output += p
    
    # check if the output is equal with the number
    if int(output) == int(num):
        return('The ' + str(num) + ' is an Armstrong number.')
    else:
        return('The ' + str(num) + ' is not an Armstrong number.')

print(armstrong_number(num))
    