# Find the part of int
#
# -  Create a function that takes a number and a list of numbers as a parameter
# -  Returns the indeces of the numbers in the list where the first number is part of
# -  Returns an empty list if the number is not part any of the numbers in the list
#
# ## Example
# -  input: `[1, 11, 34, 52, 61]`, `1`
# -  output: `[0, 1, 4]`

inputs = [1, 11, 19, 34, 52, 61, 101]
in_number = 1

def subint(inputs, in_number):
    output = []
    for i in range(len(inputs)):
        if str(in_number) in str(inputs[i]):
            output.append(i)
    return(output)

print(subint(inputs, in_number))
