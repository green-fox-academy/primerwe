# Given a string, compute recursively a new string where all the 'x' chars have been removed.

string = input('Enter a string: ')

def remove_x(string, old, new):
    if string == '':
        return ''
    if string[0] == 'x':
        return new + remove_x(string[1:], 'x', ' ')
    else:
        return string[0] + remove_x(string[1:], 'x', ' ')

print(remove_x(string, 'x', ' '))