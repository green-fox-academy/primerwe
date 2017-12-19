from tkinter import *
from board import Area
import random

size = 700

root = Tk()
root.configure(background ='black')
canvas = Canvas(root, width=size, height=size, bd=0)
canvas.pack()

    
    
    
def on_key_press(e):
    
    if (e.keysym == "Up"):
        hero.draw_character(hero.x, hero.y - 1, hero.hero_up)
    elif (e.keysym == "Down"):
        hero.draw_character(hero.x, hero.y + 1, hero.hero_down)
    elif (e.keysym == "Left"):
        hero.draw_character(hero.x - 1, hero.y, hero.hero_left)
    elif (e.keysym == "Right"):
        hero.draw_character(hero.x + 1, hero.y, hero.hero_right)


board = Board(canvas)
hero = Hero(canvas)
characters = Characters(canvas)
enemy1 = Monster(canvas)
enemy2 = Monster(canvas)
enemy3 = Monster(canvas)
boss = Boss(canvas)


root.bind("<KeyPress>", on_key_press)
canvas.pack()

canvas.focus_set()

root.mainloop()