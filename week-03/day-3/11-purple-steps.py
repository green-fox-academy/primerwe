# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]
from tkinter import *

x = 10
y = 10

def draw_steps():
    for i in range(19):
        steps = canvas.create_rectangle(x*(i+1), y*(i+1), x*(i+2), y*(i+2), fill='#b145f4')

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

draw_steps()

root.mainloop()