# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.
from tkinter import *
import random

x = 0
y = 0
def draw_square(x, y):
    for i in range(3):
        x = random.randrange(0,251)
        y = random.randrange(0,251)
        squares = canvas.create_rectangle(x, y, x+50, y+50, fill='#b4dc47')

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

draw_square(x, y)

root.mainloop()