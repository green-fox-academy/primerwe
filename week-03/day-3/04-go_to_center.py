# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

from tkinter import *
import random

x = 0
y = 0
def draw_lines(x, y):
    for i in range(3):
        x = random.randrange(0,301)
        y = random.randrange(0,301)
        rand_color = ('#%06X' % random.randint(0,256**3-1))
        lines = canvas.create_line(x, y, 150, 150, fill=rand_color, width=3)

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

draw_lines(x, y)

root.mainloop()