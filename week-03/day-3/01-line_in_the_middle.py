from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a red horizontal line to the canvas' middle.
# draw a green vertical line to the canvas' middle.

red_hline = canvas.create_line(0, 150, 300, 150, fill="#ff0000", width=3)
green_vline = canvas.create_line(150, 0, 150, 300, fill="#00ff00", width=3)

root.mainloop()