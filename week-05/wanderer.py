from tkinter import *
from board import Area

size = 700

root = Tk()
root.configure(background ='black')
canvas = Canvas(root, width=size, height=size, bd=0)
canvas.pack()

class Board(object):
    
    def __init__(self):
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
        self.pos_x = 0
        self.pos_y = 0
        self.character_del = 0
        self.tile = 70
    
    def draw_character(self, pos_x, pos_y, character_img):
        self.canvas.delete(self.character_del)
        self.character_del = canvas.create_image(pos_x*self.tile, pos_y*self.tile, anchor=NW, image=character_img)
        

class Hero(Characters):
    
    def __init__(self, canvas):
        super().__init__(canvas)
        self.hero_up_img = PhotoImage(file='elements/hero-up.png')
        self.hero_down_img = PhotoImage(file='elements/hero-down.png')
        self.hero_left_img = PhotoImage(file='elements/hero-left.png')
        self.hero_right_img = PhotoImage(file='elements/hero-right.png')

        self.draw_character(self.pos_x, self.pos_y, self.hero_down_img)

        
def on_key_press(e):
    if e.keysym == "Up":
        hero.draw_character(hero.pos_x, hero.pos_y - 1, hero.hero_up_img)
    elif e.keysym == "Down":
        hero.draw_character(hero.pos_x, hero.pos_y + 1, hero.hero_down_img)
    elif e.keysym == "Left":
        hero.draw_character(hero.pos_x - 1, hero.pos_y, hero.hero_left_img)
    elif e.keysym == "Right":
        hero.draw_character(hero.pos_x + 1, hero.pos_y, hero.hero_right_img)


        

board = Board()
hero = Hero(canvas)
board.draw_map
hero.draw_character

root.bind("<KeyPress>", on_key_press)
canvas.pack()
root.mainloop()