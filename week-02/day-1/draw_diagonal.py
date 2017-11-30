# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%% 
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# %%%%%
# %   %
# %   %
# %   %
# %   %
# %%%%%
# The square should have as many lines as the number was

number = int(input('Choose a number: '))
n = 1

if number <= 3:
    print('Drawing a diagonal is not possible!')
else:
    print('%' * number)
    for i in range(number - 2):
        print ('%' + ' ' * (n - 1) + '%' + ' ' * (number - n - 2) + '%')
        n += 1
    print('%' * number)