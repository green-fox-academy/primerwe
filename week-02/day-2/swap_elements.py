# - Create a variable named `abc`
#   with the following content: `["first", "second", "third"]`
# - Swap the first and the third element of `abc`

abc = ["first", "second", "third"]

for i in range (len(abc)//2):
    abc[i], abc[len(abc) - i - 1] = abc[len(abc) - i - 1], abc[i]
print(abc)