from settings import *
vec = pg.math.Vector2


# Test fighter
class Test(pg.sprite.Sprite):

    GRAVITY = 0.8
    ACCEL = 1.5
    JUMP = -25
    FRICTION = -0.12

    def __init__(self, game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((60, 100))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = CENTER
        self.posx = WIDTH / 2
        self.posy = HEIGHT / 2
        self.ax = 0
        self.ay = 0
        self.vx = 0
        self.vy = 0

    def jump(self):
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.game.all_objects, False)
        self.rect.y -= 1
        if hits:
            self.vy = Test.JUMP

    def update(self):
        # Resets acceleration and applies gravity
        self.ax = 0
        self.ay = Test.GRAVITY
        # Horizontal movement
        keys = pg.key.get_pressed()
        if keys[LEFT]:
            self.ax = -Test.ACCEL
        elif keys[RIGHT]:
            self.ax = Test.ACCEL
        # Applies friction
        self.ax += self.vx * Test.FRICTION
        # Stops slow crawl
        if abs(self.vx) < 0.1:
            self.vx = 0
        # Applies acceleration
        self.vx += self.ax
        self.vy += self.ay
        # Applies velocity and sets position
        self.posx += self.vx + self.ax * 0.5
        self.posy += self.vy + self.ay * 0.5
        self.rect.midbottom = (self.posx, self.posy)
