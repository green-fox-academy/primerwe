# divide the canvas into 4 equal parts
# and repeat this pattern in each quarter:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]
from tkinter import *
import random

x = 0
y = 0

def half_lines():
    hline = canvas.create_line(0, 150, 300, 150, fill="black", width=1)
    vline = canvas.create_line(150, 0, 150, 300, fill="black", width=1)
def line_play_quarter(x,y):
    for i in range(1,8):
        rand_color = ('#%06X' % random.randint(0,256**3-1))
        lines = canvas.create_line(0, y+(i*20), x+(i*20), 150, fill=rand_color, width=1)
    for i in range(1,8):
        rand_color = ('#%06X' % random.randint(0,256**3-1))
        lines = canvas.create_line(x+(i*20), 0, 150, y+(i*20), fill=rand_color, width=1)
        
    for i in range(1,8):
        rand_color = ('#%06X' % random.randint(0,256**3-1))
        lines = canvas.create_line(150, y+(i*20), 150+x+(i*20), 150, fill=rand_color, width=1)
    for i in range(1,8):
        rand_color = ('#%06X' % random.randint(0,256**3-1))
        lines = canvas.create_line(150+x+(i*20), 0, 300, y+(i*20), fill=rand_color, width=1)
        
    for i in range(1,8):
        rand_color = ('#%06X' % random.randint(0,256**3-1))
        lines = canvas.create_line(0, 150+y+(i*20), x+(i*20), 300, fill=rand_color, width=1)
    for i in range(1,8):
        rand_color = ('#%06X' % random.randint(0,256**3-1))
        lines = canvas.create_line(x+(i*20), 150, 150, 150+y+(i*20), fill=rand_color, width=1)
        
    for i in range(1,8):
        rand_color = ('#%06X' % random.randint(0,256**3-1))
        lines = canvas.create_line(150, 150+y+(i*20), 150+x+(i*20), 300, fill=rand_color, width=1)
    for i in range(1,8):
        rand_color = ('#%06X' % random.randint(0,256**3-1))
        lines = canvas.create_line(150+x+(i*20), 150, 300, 150+y+(i*20), fill=rand_color, width=1)
    
root = Tk()

canvas = Canvas(root, width='300', height='300', bg='#a0a0a0')
canvas.pack()

half_lines()
line_play_quarter(x,y)

root.mainloop()