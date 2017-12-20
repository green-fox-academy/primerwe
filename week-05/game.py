from tkinter import *
from random import randint
from board import Board, Hud
from character import Hero, Skeleton, Boss
#main


class Game(object):
    
    def __init__(self):
        root = Tk()
        self.hud_x = 0
        self.hud_y = 650
        self.canvas = Canvas(root, width=700, height=700, bd=0)
        
        self.board = Board()
        self.board.draw_board(self.canvas)
        
        self.hero = Hero(self.canvas)
        self.hero.draw_hero(0,0)
        self.hero.update_image(self.hero.hero_down)
        self.hero_has_key = False
        self.hero_can_move = True
        
        self.skeleton = Skeleton(self.canvas)
        self.skeleton_num = 3
        self.coordinates = self.board.get_random_coordinates(self.skeleton_num + 1)
        self.skeletons = []
        self.create_skeletons()
        self.add_skeleton_coordinates()
        self.add_key_to_skeleton()
        self.skeleton.draw_skeleton(self.coordinates[:-1])
        
        self.boss = Boss(self.canvas)
        self.boss.draw_boss(self.coordinates[-1])
        self.boss.x = self.coordinates[-1][0]
        self.boss.y = self.coordinates[-1][1]
        self.boss_is_dead = False
        
        self.enemies = []
        self.enlist_enemies()
        self.deleted_enemies = []
        
        self.hud = Hud()
        self.hud.draw_hud(self.canvas, self.hud_x, self.hud_y, self.hero.level, self.hero.hp, self.hero.dp, self.hero.sp)
        self.enemy_stat_onscreen = False
        
        root.bind("<KeyPress>", self.on_key_press)
        self.canvas.pack()
        #canvas.focus_set()
        root.mainloop()

    def on_key_press(self, e):
        if self.hero_can_move == True:
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
        self.check_after_arrows()
        if (e.keysym == "Space") and [self.hero.x, self.hero.y] in self.coordinates:
            self.fight(self.hero, self.enemies[self.coordinates.index([self.hero.x, self.hero.y])])
    
    def check_after_arrows(self):
        if [self.hero.x, self.hero.y] in self.coordinates and [self.hero.x, self.hero.y] not in self.deleted_enemies and self.enemy_stat_onscreen == False:
            self.hud.draw_enemy_stat(self.canvas, self.hud_x, self.hud_y, self.enemies[self.coordinates.index([self.hero.x, self.hero.y])])
            self.enemy_stat_onscreen = True
            #self.hero_can_move = False
        if [self.hero.x, self.hero.y] not in self.coordinates and self.enemy_stat_onscreen == True:
            self.hud.clear_enemy_stat(self.canvas)
            self.enemy_stat_onscreen = False
    
    def create_skeletons(self):
        for i in range(self.skeleton_num):
            self.skeletons.append(Skeleton(self.canvas))
            
    def add_skeleton_coordinates(self):
        for i, skeleton in zip(self.coordinates, self.skeletons):
            skeleton.x = i[0]
            skeleton.y = i[1]
    
    def add_key_to_skeleton(self):
        self.skeletons[randint(0, self.skeleton_num - 1)].key = True
    
    
    def enlist_enemies(self):
        for skeleton in self.skeletons:
            self.enemies.append(skeleton)
        self.enemies.append(self.boss)
        
    def is_strike(self, attacker, defender):
        var = attacker.sp + 2 * attacker.dice() #> defender.hp
        print(var)
        return var
    
    def strike(self, attacker, defender):
        print("Before first strike attacker.hp: ", attacker.hp, "defender.hp: ", defender.hp)
        if self.is_strike(attacker, defender) > defender.hp:
            print("def hp", defender.hp)
            dice = attacker.dice()
            print("dice", dice)
            print("att sp: ", attacker.sp)
            print("def dp", defender.dp)
            defender.hp -= ((attacker.sp + 2 * dice) - defender.dp)
            print("after strike attacker.hp: ", attacker.hp, "defender.hp: ", defender.hp)
            
    def fight(self, fighter_one, fighter_two):
        while fighter_one.hp > 0 and fighter_two.hp > 0:
            self.strike(fighter_one, fighter_two)
            if fighter_one.hp > 0 and fighter_two.hp > 0:
                fighter_one, fighter_two = fighter_two, fighter_one
        self.hud.update_hud()
        self.hud.update_enemy_stat()
        if self.hero.hp > 0:
            self.level_up()
            self.deleted_enemies.append([self.hero.x, self.hero.y])
            self.hero_can_move = True
            if self.boss.hp <= 0:
                self.boss.delete()
                self.boss_is_dead = True
                self.enter_next_area()
            for i in self.skeletons:
                if fighter_two == i:
                    if i.key == True:
                        self.hero_has_key = True
                        self.hud.draw_inventory(self.canvas, self.hud_x, self.hud_y)
                    i.delete(self.coordinates.index([self.hero.x, self.hero.y]))
                    self.enter_next_area()
        else:
            self.hud.update_hud()
            self.hud.update_enemy_stat()
            print("Game Over")
    
    def level_up(self):
        self.hero.max_hp += self.hero.dice()
        self.hero.dp += self.hero.dice()
        self.hero.sp += self.hero.dice()
        self.hero.level += 1
        self.canvas.delete(self.hud.hud1)
        self.canvas.delete(self.hud.hud2)
        self.canvas.delete(self.hud.hud3)
        self.canvas.delete(self.hud.hud4)
        self.hud.draw_hud(self.canvas, 0, 670, self.hero.level, self.hero.hp, self.hero.dp, self.hero.sp)
    
    def enter_next_area(self):
        if self.hero_has_key == True and self.boss_is_dead == True:
            self.hud.next_level(self.canvas, 150, 150)
            self.hero_can_move = False
            
    

            
game = Game()