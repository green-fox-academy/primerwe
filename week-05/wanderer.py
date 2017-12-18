from tkinter import *
from board import Area

size = 700

root = Tk()
root.configure(background ='black')
canvas = Canvas(root, width=size, height=size, bd=0)
canvas.pack()


class Board(object):
    
    def __init__(self, canvas):
        self.canvas = canvas 
        self.floor_img = PhotoImage(file='elements/floor.png')
        self.wall_img = PhotoImage(file='elements/wall.png')
        self.area = Area()
        self.draw_map(self.area.tiles)
        
    def draw_map(self, area):
        for i in range(len(area)):
            for j in range(len(area[i])):
                if area[i][j] == 0:
                    image = self.floor_img
                else:
                    image = self.wall_img
                canvas.create_image(j * 70, i * 70, anchor=NW, image=image)


class Characters(object):
    
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 0
        self.y = 0
        self.tile = 70
        self.character_delete = 0
    
    def draw_character(self, x, y, character_img):
        self.canvas.delete(self.character_delete)
        self.character_delete = canvas.create_image(x*self.tile, y*self.tile, anchor=NW, image=character_img)
    
    
class Hero(Characters):
    
    def __init__(self, canvas):
        super().__init__(canvas)
        self.hero_up = PhotoImage(file='elements/hero-up.png')
        self.hero_down = PhotoImage(file='elements/hero-down.png')
        self.hero_left = PhotoImage(file='elements/hero-left.png')
        self.hero_right = PhotoImage(file='elements/hero-right.png')
        
        self.draw_character(self.x, self.y, self.hero_down)
        
    def draw_character(self, x, y, character_img):
        if 0 <= x <= 9 and 0 <= y <= 9:
            if board.area.tiles[y][x] == 0:
                self.x = x
                self.y = y
                self.canvas.delete(self.character_delete)
                self.character_delete = canvas.create_image(x*self.tile, y*self.tile, anchor=NW, image=character_img)

def on_key_press(e):
    #pass
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
board.draw_map
hero.draw_character


root.bind("<KeyPress>", on_key_press)
canvas.pack()

canvas.focus_set()

root.mainloop()