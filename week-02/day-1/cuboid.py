# Write a program that stores 3 sides of a cuboid as variables (doubles)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000

a = 2
b = 3
c = 4

surface = 2 * (a * b + a * c + b * c)
volume = a * b * c

print('Surface Area: ' + str(surface))
print('Volume: ' + str(volume))
