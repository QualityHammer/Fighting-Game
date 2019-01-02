from settings import *
vec = pg.math.Vector2


# Test fighter
class Test(pg.sprite.Sprite):

    # Test fighter base stats
    GRAVITY = 0.8
    ACCEL = 1.5
    JUMP = -16
    FRICTION = -0.12

    def __init__(self, game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        # Temp images
        self.STANDR = pg.image.load(path.join(FIGHTERS, 'TestFighter.png')).convert()
        self.STANDL = pg.transform.flip(self.STANDR, True, False)
        # TEST IMAGE
        self.image = self.STANDR
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = CENTER
        # Acceleration
        self.ax = 0
        self.ay = 0
        # Velocity
        self.vx = 0
        self.vy = 0
        self.direction = 'r'

    # If fighter is on the ground, jumps
    def jump(self):
        # Calls ycollide to check if fighter is on ground
        hits = self.ycollide(1)
        if hits:
            self.vy = Test.JUMP
        # If fighter isn't on ground, calls wall_jump
        else:
            self.wall_jump(1)
            self.wall_jump(-1)

    # If fighter is grabbing a wall, jumps
    def wall_jump(self, direction):
        # Calls xcollide to check if fighter is grabbing a wall
        hits = self.xcollide(direction)
        if hits:
            # Motion
            self.vy = Test.JUMP
            self.vx = Test.JUMP * direction

    # Checks collision with walls
    # direction; -1 to check left and 1 for right
    def xcollide(self, direction):
        self.rect.x += direction
        hits = pg.sprite.spritecollide(self, self.game.all_objects, False)
        self.rect.x -= direction
        return hits

    # Checks collision with ground (potentially ceiling)
    # direction; -1 to check ground
    def ycollide(self, direction):
        self.rect.y += direction
        hits = pg.sprite.spritecollide(self, self.game.all_objects, False)
        self.rect.y -= direction
        return hits

    # Will animate in the future
    # For now this controls the fighter direction
    def animate(self):
        if self.vx != 0:
            # Right
            if self.vx > 0:
                self.image = self.STANDR
                self.direction = 'r'
            # Left
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


class PunchBag(pg.sprite.Sprite):

    GRAVITY = 0.8

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((60, 100))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH * .75, HEIGHT / 2)
        # Acceleration
        self.ax = 0
        self.ay = 0
        # Velocity
        self.vx = 0
        self.vy = 0

    def update(self):
        # Applies gravity
        self.ax = 0
        self.ay = PunchBag.GRAVITY
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
