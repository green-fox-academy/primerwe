from tkinter import *
from random import randint
from board import Board
#entity


class Characters(object):
    
    def __init__(self, canvas):
        self.canvas = canvas
        self.level = 1
        #self.after_kill = PhotoImage(file="elements/floor.png")
        self.board = Board()
        
    def dice(self):
        return randint(1,6)
    
    def move_opts(self, coordinates):
        move_opts = []
        if self.board.is_wall(self.x + self.board.tile_size, self.y) == False and [self.x + self.board.tile_size, self.y] not in coordinates:
            move_opts.append([self.board.tile_size, 0])
        if self.board.is_wall(self.x - self.board.tile_size, self.y) == False and [self.x - self.board.tile_size, self.y] not in coordinates:
            move_opts.append([-self.board.tile_size, 0])
        if self.board.is_wall(self.x, self.y + self.board.tile_size) == False and [self.x, self.y + self.board.tile_size] not in coordinates:
            move_opts.append([0, self.board.tile_size])
        if self.board.is_wall(self.x, self.y - self.board.tile_size) == False and [self.x, self.y - self.board.tile_size] not in coordinates:
            move_opts.append([0, -self.board.tile_size])
        return move_opts
    
    
class Hero(Characters):
    
    def __init__(self, canvas):
        super(Hero, self).__init__(canvas)
        self.x = 0
        self.y = 0
        self.hero_up = PhotoImage(file="elements/hero-up.png")
        self.hero_down = PhotoImage(file="elements/hero-down.png")
        self.hero_left = PhotoImage(file="elements/hero-left.png")
        self.hero_right = PhotoImage(file="elements/hero-right.png")
        self.canvas = canvas
        self.max_hp = 20 + 3 * self.dice()
        self.hp = self.max_hp
        self.dp = 2 * self.dice()
        self.sp = 5 + self.dice()
        
    def draw_hero(self, x, y):
        self.hero = self.canvas.create_image(x, y, anchor=NW, image=self.hero_down)

    def move(self, dx, dy):
        self.canvas.move(self.hero, dx, dy)
        self.x += dx
        self.y += dy
    
    def update_image(self, img):
        self.img = img
        self.canvas.itemconfig(self.hero, image=self.img)


class Skeleton(Characters):
    
    def __init__(self, canvas):
        super(Skeleton, self).__init__(canvas)
        self.skeleton_img = PhotoImage(file="elements/skeleton.png")
        self.canvas = canvas
        self.hp = 2 * self.level * self.dice()
        self.dp = self.level / 2 * self.dice()
        self.sp = self.level * self.dice()
        self.skeleton_marker = ["skeleton_a", "skeleton_b", "skeleton_c", "skeleton_d", "skeleton_e", "skeleton_f"]
        self.key = False
        
    def draw_skeleton(self, coordinates):
        for i in range(len(coordinates)):
            self.skeleton = self.canvas.create_image(coordinates[i][0], coordinates[i][1], anchor=NW, image=self.skeleton_img, tags=self.skeleton_marker[i])
    
    def move(self, coordinates):
        move_coords = self.move_opts(coordinates)[randint(0, len(self.move_opts(coordinates)) - 1)]
        self.canvas.move(self.skeleton_img, move_coords[0], move_coords[1])
        self.x += move_coords[0]
        self.y += move_coords[1]
        return [self.x, self.y]
        
    def delete(self, skeleton_id):
        self.canvas.itemconfig(self.skeleton_marker[skeleton_id], image=None)

    
class Boss(Characters):
    
    def __init__(self, canvas):
        super(Boss, self).__init__(canvas)
        self.boss_img = PhotoImage(file="elements/boss.png")
        self.canvas = canvas
        self.hp = 2 * self.level * self.dice() + self.dice()
        self.dp = self.level / 2 * self.dice() + self.dice() / 2
        self.sp = self.level * self.dice() + self.level
        
    def draw_boss(self, coordinates):
        self.boss = self.canvas.create_image(coordinates[0], coordinates[1], anchor=NW, image=self.boss_img)
        
    def move(self, coordinates):
        move_coords = self.move_opts(coordinates)[randint(0, len(self.move_opts(coordinates)) - 1)]
        self.canvas.move(self.boss_img, move_coords[0], move_coords[1])
        self.x += move_coords[0]
        self.y += move_coords[1]
        return [self.x, self.y]
    
    def delete(self):
        self.canvas.itemconfig(self.boss, image=None)
