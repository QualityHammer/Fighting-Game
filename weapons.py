from settings import *


# Test weapon
class TestWeapon(pg.sprite.Sprite):

    # Weapon base stats
    KNOCKBACK = 20

    def __init__(self, fighter):
        pg.sprite.Sprite.__init__(self)
        self.fighter = fighter
        self.image = pg.Surface((80, 40))
        self.image.fill(LRED)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.fighter.rect.center
        self.direction = 'r'

    # Weapon's basic attack
    def attack(self):
        # Sets hitbox
        center = self.rect.center
        self.image = pg.Surface((100, 70))
        self.image.fill(LRED)
        self.rect = self.image.get_rect()
        self.rect.center = center
        # Checks collision
        hits = pg.sprite.spritecollide(self, self.fighter.game.all_fighters, False)
        for hit in hits:
            if hit != self.fighter:
                if self.direction == 'r':
                    hit.vx = TestWeapon.KNOCKBACK
                    hit.vy = -TestWeapon.KNOCKBACK / 2
                else:
                    hit.vx = -TestWeapon.KNOCKBACK
                    hit.vy = -TestWeapon.KNOCKBACK / 2
        # Resets sprite
        self.image = pg.Surface((80, 40))
        self.image.fill(LRED)
        self.rect = self.image.get_rect()
        self.rect.center = center

    # Flips the sprite
    def flip(self):
        if self.direction == 'r':
            self.direction = 'l'
        else:
            self.direction = 'r'
        self.image = pg.transform.flip(self.image, True, False)

    # Flips sprite if fighter changes directions
    def update(self):
        if self.direction != self.fighter.direction:
            self.flip()
        if self.direction == 'r':
            self.rect.topleft = self.fighter.rect.center
        else:
            self.rect.topright = self.fighter.rect.center
