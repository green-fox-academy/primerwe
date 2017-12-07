# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

string = str(input('Enter a string: '))

def x_change_to_y(string, old, new):
    if string == '':
        return ''
    if string[0] == 'x':
        return new + x_change_to_y(string[1:], 'x', 'y')
    return string[0] + x_change_to_y(string[1:], 'x', 'y')

print(x_change_to_y(string, 'x', 'y'))
