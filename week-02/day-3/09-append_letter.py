# Create a function called 'create_new_verbs()' which takes a list of verbs and a string as parameters
# The string should be a preverb
# The function appends every verb to the preverb and returns the list of the new verbs

def create_new_verbs():
    verbs = ["megy", "ver", "kapcsol", "rak", "néz"]
    preverb = "be"
    new_verbs = []
    new_verbs = [preverb + x for x in verbs]
    print(new_verbs)
    
print(create_new_verbs())