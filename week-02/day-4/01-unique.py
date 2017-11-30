# Unique - remove the duplicates
#
#-  Create a function that takes a list of numbers as a parameter
#-  Returns a list of numbers where every number in the list occurs only once
#
## Example
#-  input: `[1, 11, 34, 11, 52, 61, 1, 34]`
#-  output: `[1, 11, 34, 52, 61]`

inputs = [1, 11, 34, 11, 52, 61, 1, 34]

def input_numbers(inputs):
    output = []
    for x in inputs:
        if x not in output:
            output.append(x)
    return(output)

print(input_numbers(inputs))