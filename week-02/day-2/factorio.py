# - Create a function called `factorio`
#   that returns it's input's factorial

def factorio(n):
    if n == 1:
        return n
    else:
        return n * factorio(n-1)

num = int(input("Enter a number: "))

if num < 0:
    print("Sorry, no factorial for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of",num,"is",factorio(num))