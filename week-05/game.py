from tkinter import *
import random
from board import Board, Hud
from character import Hero, Monster, Boss


class Game(object):
    
    def __init__(self):
        root = Tk()
        canvas = Canvas(root, width=700, height=700, bd=0)
        self.board = Board()
        self.board.draw_board(canvas)
        self.hero = Hero(canvas)
        self.hero.draw_hero(0,0)
        self.hero.update_image(self.hero.hero_down)
        self.boss = Boss(canvas)
        self.monster = Monster(canvas)
        self.monster_num = 3
        self.coordinates = self.board.get_random_coordinates(self.monster_num + 1)
        self.monster.draw_skeleton(self.coordinates[:-1])
        self.boss.draw_boss(self.coordinates[-1])
        self.hud = Hud()
        self.hud.draw_hud(canvas, 0, 660)
        root.bind("<KeyPress>", self.on_key_press)
        canvas.pack()
        #canvas.focus_set()
        root.mainloop()


    def on_key_press(self, e):

        if (e.keysym == "Up"):
            self.hero.update_image(self.hero.hero_up)
            if self.board.is_wall(self.hero.x, self.hero.y - self.board.tile_size) == False:
                self.hero.move(0,- self.board.tile_size)
        elif (e.keysym == "Down"):
            self.hero.update_image(self.hero.hero_down)
            if self.board.is_wall(self.hero.x, self.hero.y + self.board.tile_size) == False:
                self.hero.move(0,+ self.board.tile_size)
        elif (e.keysym == "Left"):
            self.hero.update_image(self.hero.hero_left)
            if self.board.is_wall(self.hero.x - self.board.tile_size, self.hero.y ) == False:
                self.hero.move(- self.board.tile_size, 0)
        elif (e.keysym == "Right"):
            self.hero.update_image(self.hero.hero_right)
            if self.board.is_wall(self.hero.x + self.board.tile_size, self.hero.y ) == False:
                self.hero.move(+ self.board.tile_size, 0)
            
game = Game()