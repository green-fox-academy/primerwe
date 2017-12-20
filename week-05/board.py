from tkinter import *
from random import randint
#view


class Board(object):
    #wall == 1, floor == 0
    def __init__(self):
        self.floor = PhotoImage(file="elements/floor.png")
        self.wall = PhotoImage(file="elements/wall.png")
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
        x = int(x/self.tile_size)
        y = int(y/self.tile_size)
        return self.tiles[y][x]
    
    def get_random_coordinates(self, skeleton_num):
        coordinates = []
        while len(coordinates) != skeleton_num:
            x = randint(0,len(self.tiles[0]) - 1)
            y = randint(0,len(self.tiles) - 1)
            if self.tiles[y][x] == 0 and [x * self.tile_size, y * self.tile_size] not in coordinates and [x, y] != [0, 0]:
                coordinates.append([x * self.tile_size, y * self.tile_size])
        return coordinates


class Hud(object):
    
    def __init__(self):
        self.x = 0
        self.y = 650
        self.key_img = PhotoImage(file = "elements/key.png")
        self.hud1 = None
        self.hud2 = None
        self.hud3 = None
        self.hud4 = None
        
    def draw_hud(self, canvas, x, y, level, hp, dp, sp):
        canvas.create_text(x + 2, y + 10, font=("Helvetica", 16, "bold"), anchor=NW, text="Hero")
        #canvas.create_line(x + 80, y, x + 80, y + 35, fill="#343D4A")
        self.hud1 = canvas.create_text(x + 90, y + 12, font=("Helvetica", 12, "italic"), anchor=NW, text=" Level "+str(level))
        self.hud2 = canvas.create_text(x + 180, y + 12, font=("Helvetica", 12, "italic"), anchor=NW, text=" HP: "+str(hp))
        self.hud3 = canvas.create_text(x + 270, y + 12, font=("Helvetica", 12, "italic"), anchor=NW, text=" DP: "+str(dp))
        self.hud4 = canvas.create_text(x + 360, y + 12, font=("Helvetica", 12, "italic"), anchor=NW, text=" SP: "+str(sp))
        
    def update_hud(self):
        pass


    def draw_inventory(self, canvas, x, y):
        self.inventory = canvas.create_text(x + 2, y + 40, font=("Helvetica", 14, "bold"), anchor=NW, text="Inventory")
        self.inventory_image = canvas.create_image(x, y + 40, anchor=NW, image=self.key_img)


    def draw_enemy_stat(self, canvas, x, y, enemy):
        self.enemy_stat1 = canvas.create_text(x + 2, y + 30, font=("Helvetica", 14, "bold"), anchor=NW, text=enemy.__class__.__name__)
        #self.enemy_statline= canvas.create_line(x, y + 275, x + 100, y + 275, fill="#343D4A")
        self.enemy_stat2 = canvas.create_text(x + 90, y + 32, font=("Helvetica", 12, "italic"), anchor=NW, text=" Level "+str(enemy.level))
        self.enemy_stat3 = canvas.create_text(x + 180, y + 32, font=("Helvetica", 12, "italic"), anchor=NW, text=" HP: "+str(enemy.hp))
        self.enemy_stat4 = canvas.create_text(x + 270, y + 32, font=("Helvetica", 12, "italic"), anchor=NW, text=" DP: "+str(enemy.dp))
        self.enemy_stat5 = canvas.create_text(x + 360, y + 32, font=("Helvetica", 12, "italic"), anchor=NW, text=" SP: "+str(enemy.dp))


    def update_enemy_stat(self):
        pass


    def clear_enemy_stat(self, canvas):
        canvas.delete(self.enemy_stat1)
        #canvas.delete(self.enemy_statline)
        canvas.delete(self.enemy_stat2)
        canvas.delete(self.enemy_stat3)
        canvas.delete(self.enemy_stat4)
        canvas.delete(self.enemy_stat5)


    def next_level(self, canvas, x, y):
        self.next_level_bckgr = canvas.create_rectangle(x, y, x + 450, y + 150, fill="#957740")
        self.next_level = canvas.create_text(x, y + 10, font=("Helvetica", 45, "italic bold"), anchor=NW, text="     Congrats!")
        self.next_level = canvas.create_text(x, y + 100, font=("Helvetica", 25, "italic"), anchor=NW, text="    Press space for next level.")