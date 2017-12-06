# fill the canvas with a checkerboard pattern.
from tkinter import *

can_width = 300
can_height = 300

def draw_board():
    cellwidth = can_width / 10
    cellheight = can_height / 10
    for row in range(10):
        for col in range(10):
            if (row+col) % 2 == 0:
                board = canvas.create_rectangle(col*cellwidth, row*cellheight, (col+1)*cellwidth, (row+1)*cellheight, fill="black")
            else:
                board = canvas.create_rectangle(col*cellwidth, row*cellheight, (col+1)*cellwidth, (row+1)*cellheight, fill="#b4dc47")
    
root = Tk()

canvas = Canvas(root, width=can_width, height=can_height)
canvas.grid(row=0,column=0)
canvas.pack()

draw_board()

root.mainloop()