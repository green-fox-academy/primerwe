from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

x = 145
y = 145
# draw a green 10x10 square to the center of the canvas.
green_rect = canvas.create_rectangle(x, y, x+10, y+10, fill="#b4dc47")

root.mainloop()