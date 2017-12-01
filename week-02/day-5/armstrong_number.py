#Write a simple program to check if a given number is an armstrong number. 
#The program should ask for a number. 
#Let's demonstrate this for a 4-digit number: 1634 is a 4-digit number, raise each digit to the fourth power, and add: 1^4 + 6^4 + 3^4 + 4^4 = 1634, so it is an Armstrong number.
#For a 3-digit number: 153 is a 3-digit number, raise each digit to the third power, and add: 1^3 + 5^3 + 3^3 = 153, so it is an Armstrong number.
#E.g. if we type 371, the program should print out: The 371 is an Armstrong number.

#helyiértékek alapján szétbontani a számot és a megfelelő kitevőre emelni a számjegyeket majd összeadni az így kapott összegeket

num = int(input("Enter a number: "))

def armstrong_number(num):
    output = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        output += digit ** len(str(num))
        temp //= 10
    
    if output == num:
        return('The ' + str(num) + ' is an Armstrong number.')
    else:
        return('The ' + str(num) + ' is not an Armstrong number.')

print(armstrong_number(num))