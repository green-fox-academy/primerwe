from tkinter import *
import random
from board import Board

class Characters(object):
    
    def __init__(self, canvas):
        self.canvas = canvas
#        self.tile = 70
#        self.character_delete = 0
#    
#    def draw_character(self, x, y, character_img):
#        if 0 <= x <= 9 and 0 <= y <= 9:
#            if board.area.tiles[y][x] == 0:
#                self.x = x
#                self.y = y
#                self.canvas.delete(self.character_delete)
#                self.character_delete = canvas.create_image(x*self.tile, y*self.tile, anchor=NW, image=character_img)

    
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
            self.hero = canvas.create_image(x, y, anchor=NW, image=self.hero_down)

                   
class Monster(Characters):
    
    def __init__(self, canvas):
        super().__init__(canvas)
        self.x = random.randint(1,9)
        self.y = random.randint(1,9)
        self.skeleton = PhotoImage(file='elements/skeleton.png')
        
        self.draw_character(self.x, self.y, self.skeleton)
    

class Boss(Characters):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.x = random.randint(1,9)
        self.y = random.randint(1,9)
        self.boss = PhotoImage(file='elements/boss.png')
        
        self.draw_character(self.x, self.y, self.boss)        