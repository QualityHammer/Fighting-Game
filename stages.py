from settings import *


# Background sprite class
class Background(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(path.join(BACK, 'Back.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (166, 0)
