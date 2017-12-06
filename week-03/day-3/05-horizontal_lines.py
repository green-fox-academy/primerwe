# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

from tkinter import *
import random

x = 0
y = 0
def draw_horizontal(x, y):
    for i in range(3):
        x = random.randrange(0,251)
        y = random.randrange(0,301)
        lines = canvas.create_line(x, y, x+50, y, fill='#b4dc47', width=3)

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

draw_horizontal(x, y)

root.mainloop()