# Find part of an integer
#
# -  Create a function that takes two strings as a parameter
# -  Returns the starting index where the second one is starting in the first one
# -  Returns `-1` if the second string is not in the first one
#
# ## Example
# -  input: `"this is what I'm searching in"`, `"searching"`
# -  output: `17`

inputs = "this is what I'm searching in"
char = "searching"

def find_str(inputs, char):
    i = 0

    if char in inputs:
        c = char[0]
        for ch in inputs:
            if ch == c:
                if inputs[i:i+len(char)] == char:
                    return i

            i += 1

    return -1

print(find_str(inputs, char))