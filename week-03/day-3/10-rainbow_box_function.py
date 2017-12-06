# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.
from tkinter import *
import random

x = 150
y = 150
size = 0

def draw_squares(size):
    for i in range(random.randrange(1,300)):
        size = random.randrange(1,300)
        d = size / 2
        square_color = ('#%06X' % random.randint(0,256**3-1))
        squares = canvas.create_rectangle(x-d, y-d, x+d, y+d, fill=square_color)

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

draw_squares(size)

root.mainloop()