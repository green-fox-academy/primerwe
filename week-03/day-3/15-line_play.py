# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]
from tkinter import *

x = 0
y = 0
def line_play(x,y):
    for i in range(1,15):
        lines = canvas.create_line(0, y+(i*20), x+(i*20), 300, fill='#b4dc47', width=1)
    for i in range(1,15):
        lines = canvas.create_line(x+(i*20), 0, 300, y+(i*20), fill='#b145f4', width=1)

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

line_play(x,y)

root.mainloop()