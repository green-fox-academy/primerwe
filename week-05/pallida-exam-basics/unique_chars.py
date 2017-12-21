# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases
from collections import Counter

def unique_characters(inputs):
    output = []
    lower_chars = inputs.replace(" ", "").lower()
    char_counts = Counter(lower_chars)

    for char, count in char_counts.items():
        if count == 1:
            output.append(char)
    
    return output
    

print(unique_characters("anagram"))
# Should print out:
# ["n", "g", "r", "m"]