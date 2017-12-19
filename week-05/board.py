from tkinter import *
import random

class Board(object):
    #wall == 1, floor == 0
    def __init__(self):
        self.floor = PhotoImage(file='elements/floor.png')
        self.wall = PhotoImage(file='elements/wall.png')
        self.tile_size = 65
        self.x = 0
        self.y = 0
        self.tiles = [
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 0, 0, 1, 1],
            [0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 1, 1, 0, 0, 0, 1]
        ]

    def draw_board(self, canvas):
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                if self.tiles[row][col] == 0:
                    canvas.create_image(self.x, self.y, anchor=NW, image=self.floor)
                    self.x += self.tile_size
                else:
                    canvas.create_image(self.x, self.y, anchor=NW, image=self.wall)
                    self.x += self.tile_size
            self.x = 0
            self.y += self.tile_size


    def is_wall(self, x, y):
        cell_x = x//self.tile_size
        cell_y = y//self.tile_size
        if cell_x >= 0 and cell_x < len(self.tiles[0]) and cell_y >= 0 and cell_y < (len(self.tiles)):
            return self.tiles[cell_y][cell_x] == 1
        else:
            return True
        
    def get_cell(self, x, y):
        x = int(x/65)
        y = int(y/65)
        return self.tiles[y][x]
    
    def get_random_coordinates(self, monster_num):
        coordinates = []
        while len(coordinates) != monster_num:
            x = random.randint(0,len(self.tiles[0]) - 1)
            y = random.randint(0,len(self.tiles) - 1)
            if self.tiles[y][x] == 0 and [x, y] not in coordinates and [x, y] != [0, 0]:
                coordinates.append([x * self.tile_size, y * self.tile_size])
        return coordinates


class Hud(object):
    
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def draw_hud(self, canvas, x, y):
        canvas.create_text(x, y, font=(16), anchor=NW, text=" Hero " + " (Level 1) " + " HP: 8/10 " + " | " + " DP: 8 " + " | " + " SP: 6")