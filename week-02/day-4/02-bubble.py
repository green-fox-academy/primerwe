# Sort that list
#
# -  Create a function that takes a list of numbers as parameter
# -  Returns a list where the elements are sorted in ascending numerical order
# -  Make a second boolean parameter, if it's `true` sort that list descending
#
# ## Example
# -  input `[34, 12, 24, 9, 5]`
# -  output `[5, 9, 12, 24, 34]`

inputs = [7, 99, 34, 12, 24, 9, 5]
reverse = str(input("Is it True or False?: "))

def input_sort(inputs, reverse):
    output = []
    if reverse != 'True' and reverse != 'False':
        return("Sorry, can't Do It")
    elif reverse == 'False':
        while inputs:
            minimum = inputs[0]
            for x in inputs:
                if x < minimum:
                    minimum = x
            output.append(minimum)
            inputs.remove(minimum)
        return(output)
    else:
        while inputs:
            maximum = inputs[0]
            for x in inputs:
                if x > maximum:
                    maximum = x
            output.append(maximum)
            inputs.remove(maximum)
        return(output)

print(input_sort(inputs, reverse))