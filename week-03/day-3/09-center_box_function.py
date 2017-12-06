# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.
from tkinter import *
import random

canvas_width = 300
canvas_height = 300
x = canvas_width / 2
y = canvas_height / 2
size = 0

def draw_squares(size):
    for i in range(3):
        size = random.randrange(1,151)
        rand_color = ('#%06X' % random.randint(0,256**3-1))
        squares = canvas.create_rectangle((x-size/2), (y-size/2), (x+size/2), (y+size/2), fill=rand_color)

root = Tk()

canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

draw_squares(size)

root.mainloop()