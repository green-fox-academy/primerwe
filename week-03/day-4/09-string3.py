# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

string = input('Enter a string: ')

def separate_chars(string):
    if string == '':
        return ''
    else:
        return string[0] + '*' + separate_chars(string[1:])
    
print(separate_chars(string))