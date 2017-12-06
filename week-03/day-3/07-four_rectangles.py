# draw four different size and color rectangles.
from tkinter import *
import random

x = 0
y = 0
dx = 0
dy = 0

def draw_rectangles(x, y, dx, dy):
    for i in range(4):
        x = random.randrange(0,301)
        y = random.randrange(0,301)
        dx = random.randrange(10,101)
        dy = random.randrange(10,101)
        rand_color = ('#%06X' % random.randint(0,256**3-1))
        rectangles = canvas.create_rectangle(x, y, x+dx, y+dy, fill=rand_color)
                             
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

draw_rectangles(x, y, dx, dy)

root.mainloop()