from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.
red_line = canvas.create_line(50, 50, 250, 50, fill="#f00", width=3)
green_line = canvas.create_line(250, 50, 250, 250, fill="#b4dc47", width=3)
blue_line = canvas.create_line(250, 250, 50, 250, fill="#00f", width=3)
yellow_line = canvas.create_line(50, 250, 50, 50, fill="#ff0", width=3)

root.mainloop()