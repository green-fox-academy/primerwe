class Area(object):
    #wall == 1, floor == 0
    def __init__(self):
        self.tiles = [
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 0, 0, 1, 1],
            [0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 0, 1, 1, 0, 0, 0, 1]
        ]

    def is_wall(self, x, y):
        return self.tiles[x][y] == 1
    
    
#feature: generáljon 10db 0/1 random számot a listába 10szer és úgy rajzolja a térképet