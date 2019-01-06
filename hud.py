from settings import *


# Health bar object
class HealthBar(pg.sprite.Sprite):

    def __init__(self, screen, player):
        pg.sprite.Sprite.__init__(self)
        self.player = player
        self.screen = screen
        self.image = pg.image.load(path.join(OBJECTS, 'Health Bar.png')).convert()
        self.image = pg.transform.scale(self.image, (568, 35))
        self.rect = self.image.get_rect()
        self.set_rect()
        if self.player == 2:
            self.image = pg.transform.flip(self.image, True, False)
        self.image.set_colorkey(BLACK)

    # Crops the health bar to shorten it
    def damage(self, h, num):
        pct = num / h
        new_width = self.rect.width - self.rect.width * pct
        image = self.image
        self.image = pg.Surface((new_width, 35))
        if self.player == 1:
            self.image.blit(image, (0, 0), (self.rect.width - new_width, 0, new_width, 35))
        else:
            self.image.blit(image, (self.rect.width - new_width, 0), (0, 0, new_width, 35))
        self.rect = self.image.get_rect()
        self.set_rect()
        self.image.set_colorkey(BLACK)

    # Method to reset the rect back in place
    def set_rect(self):
        if self.player == 1:
            self.rect.topleft = (154, 852)
        else:
            self.rect.topright = (1347, 852)
