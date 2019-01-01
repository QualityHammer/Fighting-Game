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
        self.direction = 'r'

    def flip(self):
        # Flips the sprite
        if self.direction == 'r':
            self.direction = 'l'
        else:
            self.direction = 'r'
        self.image = pg.transform.flip(self.image, True, False)

    def update(self):
        # Flips sprite if fighter changes directions
        if self.direction != self.fighter.direction:
            self.flip()
        if self.direction == 'r':
            self.rect.topleft = self.fighter.rect.center
        else:
            self.rect.topright = self.fighter.rect.midleft
