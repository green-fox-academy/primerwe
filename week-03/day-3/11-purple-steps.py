# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]
from tkinter import *

def draw_steps():
    x = 10
    y = 10
    size = 10
    for _ in range(19):
        steps = canvas.create_rectangle(x, y, x+size, y+size, fill='#b145f4')
        x += size
        y += size

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

draw_steps()

root.mainloop()