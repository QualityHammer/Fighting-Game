from settings import *
vec = pg.math.Vector2


# Test fighter
class Test(pg.sprite.Sprite):

    # Test fighter stats
    GRAVITY = 0.8
    ACCEL = 1.5
    JUMP = -16
    FRICTION = -0.12

    def __init__(self, game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        # IMAGE IS NOT READY
        # self.image = pg.image.load(path.join(FIGHTERS, 'TestFighter.png')).convert()
        # self.image = pg.transform.scale(self.image, (60, 100))
        # self.image.set_colorkey(BLACK)
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
        # If fighter is on the ground, jumps
        hits = self.ycollide(1)
        if hits:
            self.vy = Test.JUMP
        else:
            self.wall_jump(1)
            self.wall_jump(-1)

    def wall_jump(self, direction):
        # If fighter is grabbing a wall, jumps
        hits = self.xcollide(direction)
        if hits:
            self.vy = Test.JUMP
            self.vx = Test.JUMP * direction

    def xcollide(self, direction):
        # Checks collision with walls
        # direction; -1 to check left and 1 for right
        self.rect.x += direction
        hits = pg.sprite.spritecollide(self, self.game.all_objects, False)
        self.rect.x -= direction
        return hits

    def ycollide(self, direction):
        # Checks collision with ground (potentially ceiling)
        # direction; -1 to check ground
        self.rect.y += direction
        hits = pg.sprite.spritecollide(self, self.game.all_objects, False)
        self.rect.y -= direction
        return hits

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
        self.rect.x += self.vx + self.ax * 0.5
        self.rect.y += self.vy + self.ay * 0.5
