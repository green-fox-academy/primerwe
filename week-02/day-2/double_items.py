# - Create an array variable named `ag`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Double all the values in the array

ag = [3, 4, 5, 6, 7]
    
def double(ag):
    return [i*2 for i in ag]

print(double(ag))

def duplicate(ag):
    return [ag[i//2] for i in range(len(ag)*2)]

print(duplicate(ag))
