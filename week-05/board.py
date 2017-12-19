from tkinter import *

class Board(object):
    #wall == 1, floor == 0
    def __init__(self):
        self.floor = PhotoImage(file='elements/floor.png')
        self.wall = PhotoImage(file='elements/wall.png')
        self.tile = 70
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

        def draw_map(self, canvas):
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[i])):
                if self.tiles[row][col] == 0:
                    image = self.floor
                else:
                    image = self.wall
                canvas.create_image(col * self.tile, row * self.tile, anchor=NW, image=image)
        
        
        
#    def is_wall(self, x, y):
#        self.tiles[y][x] == 1
#    
    def is_floor(self, x, y):
        self.tiles[y][x] == 0
#    
#feature: generáljon 10db 0/1 random számot a listába 10szer és úgy rajzolja a térképet