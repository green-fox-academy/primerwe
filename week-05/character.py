from tkinter import *
import random
from board import Board


class Characters(object):
    
    def __init__(self, canvas):
        self.canvas = canvas

    
class Hero(Characters):
    
    def __init__(self, canvas):
        self.x = 0
        self.y = 0
        self.hero_up = PhotoImage(file='elements/hero-up.png')
        self.hero_down = PhotoImage(file='elements/hero-down.png')
        self.hero_left = PhotoImage(file='elements/hero-left.png')
        self.hero_right = PhotoImage(file='elements/hero-right.png')
        self.canvas = canvas
        
    def draw_hero(self, x, y):
        self.hero = self.canvas.create_image(x, y, anchor=NW, image=self.hero_down)

    def move(self, dx, dy):
        self.canvas.move(self.hero, dx, dy)
        self.x += dx
        self.y += dy
    
    def update_image(self, img):
        self.img = img
        self.canvas.itemconfig(self.hero, image=self.img)


class Monster(Characters):
    
    def __init__(self, canvas):
#        self.x = random.randint(1,9)
#        self.y = random.randint(1,9)
        self.skeleton_img = PhotoImage(file='elements/skeleton.png')
        self.canvas = canvas
        
    def draw_skeleton(self, coordinates):
        for i in range(len(coordinates)):
            self.skeleton = self.canvas.create_image(coordinates[i][0], coordinates[i][1], anchor=NW, image=self.skeleton_img)
    

class Boss(Characters):
    
    def __init__(self, canvas):
#        self.x = random.randint(1,9)
#        self.y = random.randint(1,9)
        self.boss_img = PhotoImage(file='elements/boss.png')
        self.canvas = canvas
        
    def draw_boss(self, coordinates):
        self.boss = self.canvas.create_image(coordinates[0], coordinates[1], anchor=NW, image=self.boss_img)