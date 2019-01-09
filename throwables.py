from settings import *


# Throwing star object
class ThrowStar(pg.sprite.Sprite):

    # Throw star stats
    DAMAGE = 5
    SPEED = 15
    KNOCKBACK = 15
    COOLDOWN = 300

    # fighter; fighter object holding weapon, game; game object, direction; -1 - left, 1 - right
    def __init__(self, fighter, game, direction):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(path.join(WEAPONS, 'ThrowStar.png'))
        self.rect = self.image.get_rect()
        self.fighter = fighter
        self.direction = direction
        self.game = game
        if self.direction < 0:
            self.rect.center = fighter.rect.midleft
        else:
            self.rect.center = self.fighter.rect.midright
        self.vx = ThrowStar.SPEED * self.direction

    # Fighter collision handler
    def collisions(self):
        hits = pg.sprite.spritecollide(self, self.game.all_fighters, False)
        for hit in hits:
            if hit != self.fighter:
                hit.damage(ThrowStar.DAMAGE)
                hit.vx = ThrowStar.KNOCKBACK * self.direction
                hit.vy = -ThrowStar.KNOCKBACK / 2
                self.kill()

    def update(self):
        # Applies velocity
        self.rect.x += self.vx
        # Kills sprite if it hits a wall
        if self.rect.right > WIDTH - 166 or self.rect.left < 166:
            self.kill()
        self.collisions()
