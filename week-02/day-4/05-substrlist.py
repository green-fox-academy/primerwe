# Find the substring in the list
#
# -  Create a function that takes a string and a list of string as a parameter
# -  Returns the index of the string in the list where the first string is part of
# -  Returns `-1` if the string is not part any of the strings in the list
#
# ## Example
# -  input: `"ching"`, `["this", "is", "what", "I'm", "searching", "in"]`
# -  output: `4`

inputs = ["this", "is", "what", "I'm", "searching", "in"]
in_str = "ching"

def substr_list(inputs, in_str):
    output = 0
    for i in inputs:
        if 'ching' in i:
            output = inputs.index(i)
            return(output)

print(substr_list(inputs, in_str))
