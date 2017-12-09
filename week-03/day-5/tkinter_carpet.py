from tkinter import *
import random

SIZE = 729
rand_color = ('#%06X' % random.randint(0,256**3-1))

def draw_sierpinsky_carpet(x1, y1, x2, y2, level):
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    rand_color = ('#%06X' % random.randint(0,256**3-1))
    canvas.create_rectangle(
        (2 * x1 + x2) / 3,
        (2 * y1 + y2) / 3,
        (x1 + 2 * x2) / 3 - 1,
        (y1 + 2 * y2) / 3 - 1,
        fill=rand_color)
    if level < 5:
        draw_sierpinsky_carpet(
            x1, 
            y1, 
            (2 * x1 + x2) / 3.0, 
            (2 * y1 + y2) / 3.0,
            level + 1)
        draw_sierpinsky_carpet(
            (2 * x1 + x2) / 3.0, 
            y1, 
            (x1 + 2 * x2) / 3.0, 
            (2 * y1 + y2) / 3.0,
            level + 1)
        draw_sierpinsky_carpet(
            (x1 + 2 * x2) / 3.0, 
            y1,
            x2, 
            (2 * y1 + y2) / 3.0,
            level + 1)
        draw_sierpinsky_carpet(
            x1, 
            (2 * y1 + y2) / 3.0, 
            (2 * x1 + x2) / 3.0, 
            (y1 + 2 * y2) / 3.0, 
            level + 1)
        draw_sierpinsky_carpet(
            (x1 + 2 * x2) / 3.0, 
            (2 * y1 + y2) / 3.0, 
            x2, 
            (y1 + 2 * y2) / 3.0, 
            level + 1)
        draw_sierpinsky_carpet(
            x1, 
            (y1 + 2 * y2) / 3.0, 
            (2 * x1 + x2) / 3.0, 
            y2, 
            level + 1)
        draw_sierpinsky_carpet(
            (2 * x1 + x2) / 3.0, 
            (y1 + 2 * y2) / 3.0, 
            (x1 + 2 * x2) / 3.0, 
            y2, 
            level + 1)
        draw_sierpinsky_carpet(
            (x1 + 2 * x2) / 3.0, 
            (y1 + 2 * y2) / 3.0, 
            x2, 
            y2, 
            level + 1)

root = Tk()
canvas = Canvas(root, width=SIZE, height=SIZE)
canvas.pack()

canvas.create_rectangle(2,2, SIZE - 2, SIZE - 2, fill=rand_color)
draw_sierpinsky_carpet(2,2, SIZE - 2, SIZE - 2, 1)

root.mainloop()