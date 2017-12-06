# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/envelope-star/r2.png]
from tkinter import *

x=0
y=0
def half_lines():
    hline = canvas.create_line(0, 150, 300, 150, fill="#a0a0a0", width=1)
    vline = canvas.create_line(150, 0, 150, 300, fill="#a0a0a0", width=1)
def draw_envelope_star(x,y):
    for i in range(1,15):
        lines = canvas.create_line(x+(i*10), 150, 150, 150-(y+(i*10)), fill='#b4dc47', width=1)
    for i in range(1,15):
        lines = canvas.create_line(x+(i*10), 150, 150, 150+(y+(i*10)), fill='#b145f4', width=1)
    for i in range(1,15):
        lines = canvas.create_line(150, y+(i*10), 150+(x+(i*10)), 150, fill='red', width=1)
    for i in range(1,15):
        lines = canvas.create_line(150, 150+(y+(i*10)), 300-(x+(i*10)), 150, fill='blue', width=1)

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

half_lines()
draw_envelope_star(x,y)

root.mainloop()