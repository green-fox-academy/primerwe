# The program's aim is to collect your favourite animals and store them in a text file.
# There is a given text file called '''favourites.txt''', it will contain the animals
# If ran from the command line without arguments
# It should print out the usage:
# ```fav_animals [animal] [animal]```
# You can add as many command line arguments as many favourite you have.
# One animal should be stored only at once
# Each animal should be written in separate lines
# The program should only save animals, no need to print them
import sys

class Controller():
    def __init__(self):
        self.list_argv = []
        self.arg_reader()
        self.controller()
    
    def arg_reader(self):
        if len(sys.argv) <= 1:
            self.list_argv = []
        else:
            self.list_argv = sys.argv[1:]
    
    def controller(self):
        if self.list_argv[0] == '-a':
            if len(self.list_argv) <= 1:
                print('Unable to add')
            else:
                animals.add_fav_animals(self.list_argv[1])
                #animals.print_file()
        elif self.list_argv[0] == '-r':
            try:
                if len(self.list_argv) <= 1:
                    print('Unable to remove')
                elif int(self.list_argv[1]) > len(animals.txt):
                    print('Unable to remove: index is out of bound')
                else:
                    animals.remove_fav_animal(int(self.list_argv[1]))
                    #animals.print_file()
            except:
                print('Unable to remove: index is not a number')


class FavAnimals():
    
    def __init__(self):
        self.txt = ''
        self.open_read()
        
    def open_read(self):
        favs = open('favourites.txt', 'r')
        self.txt = favs.readlines()
        favs.close()

    def open_write(self):
        favs = open('favourites.txt', 'w')
        favs.writelines(self.txt)
        favs.close()
        
    def add_fav_animals(self, text):
        self.txt.append('[' + text + ']\n')
        self.open_write()
    
    def remove_fav_animal(self, item):
        del self.txt[item]
        self.open_write()
    
    def print_file(self):
        if len(self.txt) == 0:
            print("No favourite animals! :(")
            
        else:
            print("fav_animals:\n")
            for i in range(len(self.txt)):
                print(i+1, self.txt[i][:-1])
                
animals = FavAnimals()
control = Controller()