# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]
from tkinter import *

box_list = [[10, 10], [290,  10], [290, 290], [10, 290]]
other_list = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]

bx = [box_list[i][0] for i in range(0, len(box_list))]
by = [box_list[i][1] for i in range(0, len(box_list))]
ox = [other_list[i][0] for i in range(0, len(other_list))]
oy = [other_list[i][1] for i in range(0, len(other_list))]

def draw_green_lines():
    for i in range(0, len(box_list)):
        box = canvas.create_line(bx[i], by[i], bx[i-1], by[i-1], fill="#b4dc47")
    for i in range(0, len(other_list)):
        line = canvas.create_line(ox[i], oy[i], ox[i-1], oy[i-1], fill="#b4dc47")
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

draw_green_lines()

root.mainloop()