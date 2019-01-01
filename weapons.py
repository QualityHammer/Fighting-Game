from settings import *


# Test weapon
class TestWeapon(pg.sprite.Sprite):

    def __init__(self, fighter):
        pg.sprite.Sprite.__init__(self)
        self.fighter = fighter
        self.image = pg.Surface((40, 80))
        self.image.fill(LRED)
        self.rect = self.image.get_rect()
        self.image = pg.transform.rotate(self.image, 90)
        self.rect.topleft = self.fighter.rect.center

    def update(self):
        self.rect.topleft = self.fighter.rect.center
