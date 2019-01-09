from settings import *


# Test weapon
class TestWeapon(pg.sprite.Sprite):

    # Weapon base stats
    DAMAGE = 10
    KNOCKBACK = 20

    # fighter; fighter object holding this weapon
    def __init__(self, fighter):
        pg.sprite.Sprite.__init__(self)
        self.fighter = fighter
        self.image = pg.image.load(path.join(WEAPONS, 'TestWeapon.png')).convert()
        self.image = pg.transform.rotate(self.image, 290)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.fighter.get_hand_loc()
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
                else:
                    hit.vx = -TestWeapon.KNOCKBACK
                hit.vy = -TestWeapon.KNOCKBACK / 2
                hit.damage(TestWeapon.DAMAGE)
        # Resets sprite
        self.image = pg.image.load(path.join(WEAPONS, 'TestWeapon.png')).convert()
        if self.direction == 'l':
            self.image = pg.transform.rotate(self.image, 110)
            self.image = pg.transform.flip(self.image, False, True)
        else:
            self.image = pg.transform.rotate(self.image, 290)
        self.image.set_colorkey(BLACK)
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
            self.rect.midleft = self.fighter.get_hand_loc()
        else:
            self.rect.midright = self.fighter.get_hand_loc()
