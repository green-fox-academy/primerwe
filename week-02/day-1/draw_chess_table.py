# Crate a program that draws a chess table like this
#
# % % % % 
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % % 
#  % % % %
#

n = 8
for i in range(n):
    if i % 2 == 0:
        print('X X X X')
    else:
        print(' X X X X')