# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

divisor = int(input("Enter a number: "))

def divide():
    try:
        result = 10 / divisor
        return(result)
    except ZeroDivisionError:
        return("Fail")
            
print(divide())