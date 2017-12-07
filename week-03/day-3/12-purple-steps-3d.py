# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps-3d/r4.png]
from tkinter import *

x = 10
y = 10
size = 10

def draw_steps(x,y,size):
    for _ in range(6):
        steps = canvas.create_rectangle(x, y, x+size, y+size, fill='#b145f4')
        x += size
        y += size
        size += 10
        
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

draw_steps(x,y,size)

root.mainloop()