# Create a function called 'reverse_string' which takes a string as a parameter
# The function reverses it and returns with the reversed string


strg = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"

def reverse(strg):
    i = len(strg) - 1
    strgNew = ''
    while  i >= 0:
        strgNew = strgNew + str(strg[i])
        i = i -1
    return strgNew

print(reverse(strg))
    