from settings import *


# Ground object
class Ground(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((WIDTH, 100))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0, HEIGHT)
