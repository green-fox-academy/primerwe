from Sharpie import Sharpie
    
red = Sharpie("red", 1.25, 10)
green = Sharpie("#b4dc47", 0.7)
blue = Sharpie("#00f", 1.0, 65)
black = Sharpie("#000", 2.5, 0)
list_of_sharpies = [red, green, blue, black]
      
class SharpieSet(object):
    def count_usable(self):
        count = 0
        for i in range(len(list_of_sharpies)):
            if list_of_sharpies[i].ink_amount > 0:
                count += 1
        print(count)
    
    def remove_trash(self):
        no_trash_list = []
        for i in range(len(list_of_sharpies)):
            if list_of_sharpies[i].ink_amount > 0:
                no_trash_list.append(list_of_sharpies[i])
        return no_trash_list

red.use()
SharpieSet.count_usable(list_of_sharpies)
list_of_sharpies = SharpieSet.remove_trash(list_of_sharpies)

for i in range(len(list_of_sharpies)):
    list_of_sharpies[i].print_status()