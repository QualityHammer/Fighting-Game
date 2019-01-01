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
        # Temp images
        img = pg.image.load(path.join(FIGHTERS, 'TestFighter.png')).convert()
        self.STANDR = pg.transform.scale(img, (60, 100))
        self.STANDL = pg.transform.flip(self.STANDR, True, False)
        # TEST IMAGE
        self.image = self.STANDR
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = CENTER
        self.posx = WIDTH / 2
        self.posy = HEIGHT / 2
        self.ax = 0
        self.ay = 0
        self.vx = 0
        self.vy = 0
        self.direction = 'r'

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

    def animate(self):
        # Will animate in the future
        # For now this controls the fighter direction
        if self.vx != 0:
            if self.vx > 0:
                self.image = self.STANDR
                self.direction = 'r'
            else:
                self.image = self.STANDL
                self.direction = 'l'
            self.image.set_colorkey(BLACK)

    def update(self):
        self.animate()
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
        # Applies acceleration
        self.vx += self.ax
        self.vy += self.ay
        # Stops slow crawl
        if abs(self.vx) < 0.2:
            self.vx = 0
            self.ax = 0
        # Applies velocity and sets position
        self.rect.x += self.vx + self.ax * 0.5
        self.rect.y += self.vy + self.ay * 0.5
