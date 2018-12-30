from settings import *


# Ground object
class Ground(pg.sprite.Sprite):

    ID = 'GND'

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((WIDTH, 100))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0, HEIGHT)


# Wall object
class Wall(pg.sprite.Sprite):

    ID = 'WLL'

    def __init__(self, direction):
        pg.sprite.Sprite.__init__(self)
        self.direction = direction
        self.image = pg.Surface((100, HEIGHT - 100))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        if direction == 'left':
            self.rect.topleft = (0, 0)
        elif direction == 'right':
            self.rect.topright = (WIDTH, 0)
        else:
            print('ERROR: {} has a false direction')
