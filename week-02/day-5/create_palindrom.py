#1. ask for a string
#2. reverse the string
#3. put together the original string with the reversed one

str1 = str(input("Enter a word: ")) 

def create_palindrom(str1):
    str2 = str1[::-1]
    return "".join((str1, str2))
    
print(create_palindrom(str1))