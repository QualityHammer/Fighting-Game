from settings import *


# Ground object
class Ground(pg.sprite.Sprite):

    ID = 'GND'

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(path.join(OBJECTS, 'Floor.png')).convert()
        self.image = pg.transform.scale(self.image, (1500, 166))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0, HEIGHT)


# Wall object
class Wall(pg.sprite.Sprite):

    ID = 'WLL'

    # direction; 'r' - right side, 'l' - left side
    def __init__(self, direction):
        pg.sprite.Sprite.__init__(self)
        self.direction = direction
        self.image = pg.image.load(path.join(OBJECTS, 'Wall.png')).convert()
        self.rect = self.image.get_rect()
        if direction == 'l':
            self.image = self.image
            self.rect.topleft = (0, 0)
        elif direction == 'r':
            self.image = pg.transform.flip(self.image, True, False)
            self.rect.topright = (WIDTH, 0)
        else:
            # If wall has no direction
            print('ERROR: {} has a false direction').format(self)
