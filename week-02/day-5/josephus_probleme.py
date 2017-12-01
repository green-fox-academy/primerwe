#Write a function to solve Josephus Problem. 
#The program should ask for a number, this number represents how many people are in the "game". 
#The return value should be the number of the "winning" seat.

# n = (2 ** m) + l     n = people in the "game"
# w(n) = (2 * l) + 1  -> number of the a "winning" seat
# OR:
# convert n to binary
# move the first digit to the last (if 0 become the first, ignore it), 
# convert back to decimal == this will be the number of the "winning" seat

n = int(input('How many people are in the "game"?: '))

def josephus_problem(n):
    #convert the number to binary
        b = ''.join(str(1 & int(n) >> i) for i in range(n)[::-1])
        binary = b.lstrip("0")
    #convert int to str 
        binary_str = str(binary)
        digits = [int(x) for x in binary_str]
    #move the first digit to the last
        digits = digits[1:] + digits[:1]
        d = ''.join([str(x) for x in digits])
    #ignore zeros
        digits = d.lstrip("0")
    #convert back to decimal
        decimal = 0
        for digit in digits:
            decimal = decimal*2 + int(digit)
        return('The "winning seat" is: ' + str(decimal))

print(josephus_problem(n))