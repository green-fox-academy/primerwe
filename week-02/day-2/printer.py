# - Create a function called `printer`
#   which prints the input parameters
#   (can have multiple number of arguments)

def printer_char(*args):
    char = ""
    for a in args:
        char += a
    print(char)
    
printer_char('Hello', 'Green', 'Fox')

def printer_sum(*args):
    total = 0
    for a in args:
        total += a
    print(total)
    
printer_sum(1, 2, 3, 5)

