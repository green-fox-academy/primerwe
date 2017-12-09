from tkinter import *
import math
import random

SIZE = 800
rand_color = ('#%06X' % random.randint(0,256**3-1))

def draw_sierpinsky_triangle(x, y, size, level):
    x = float(x)
    y = float(y)
    rand_color = ('#%06X' % random.randint(0,256**3-1))
    if level == 0:
        canvas.create_polygon(x, y,
                              x+size, y,
                              x+size/2, y+size*math.sqrt(3)/2,
                              fill=rand_color)
    else:
        draw_sierpinsky_triangle(x, y, size/2, level-1)
        draw_sierpinsky_triangle(x+size/2, y, size/2, level-1)
        draw_sierpinsky_triangle(x+size/4, y+size*math.sqrt(3)/4, size/2, level-1)

root = Tk()
canvas = Canvas(root, width=SIZE, height=SIZE, bg=rand_color)
canvas.pack()

draw_sierpinsky_triangle(2, 2, SIZE - 2, 7)

root.mainloop()