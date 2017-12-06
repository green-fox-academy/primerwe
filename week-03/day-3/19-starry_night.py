# draw the night sky:
# - The background should be black
# - The stars should be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

from tkinter import *
import random

x=0
y=0
def draw_the_night_sky(x,y):
    for i in range(1,101):
        x = random.randrange(0,251)
        y = random.randrange(0,251)
        rand_grey = ('grey' + str(random.randrange(50,100)))
        stars = canvas.create_rectangle(x, y, x+10, y+10, fill=rand_grey)

root = Tk()

canvas = Canvas(root, width='300', height='300', bg='black')
canvas.pack()

draw_the_night_sky(x,y)

root.mainloop()