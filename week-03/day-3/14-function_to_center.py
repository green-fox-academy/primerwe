# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.
from tkinter import *

x = 0
y = 0
def go_to_center(x,y):
    for i in range(16):
        lines = canvas.create_line(150, 150, x+(i*20), 0, fill='#b4dc47', width=2)
    for i in range(16):
        lines = canvas.create_line(150, 150, 0, y+(i*20), fill='#b4dc47', width=2)
    for i in range(16):
        lines = canvas.create_line(150, 150, x+(i*20), 300, fill='#b00', width=2)
    for i in range(16):
        lines = canvas.create_line(150, 150, 300, y*(i+1)+(i*20), fill='#b00', width=2)
    
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

go_to_center(x,y)

root.mainloop()