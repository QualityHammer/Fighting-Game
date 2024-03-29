from settings import *
from throwables import ThrowStar
vec = pg.math.Vector2


# Test fighter
class Test(pg.sprite.Sprite):

    # Test fighter base stats and details
    HEALTH = 100
    GRAVITY = 0.8
    ACCEL = 1.5
    JUMP = -20
    FRICTION = -0.12
    # Position where the sprite hand is located
    HAND_LOC = (16, 49)
    # Base throwable
    THROWABLE = ThrowStar

    # game; Game class, bar; Health bar
    def __init__(self, game, bar):
        self.game = game
        self.bar = bar
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
        # Direction; 'r' if Right, 'l' if Left
        self.direction = 'r'
        # Wall sliding flag; 'r' if clinging to right wall, 'l' if left, 'n' if not clinging to wall
        self.grab_wall = 'n'
        # Health
        self.health = Test.HEALTH
        # Timer to track throwable cooldown time
        self.throw_last_used = pg.time.get_ticks()
        print(self.throw_last_used)

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

    # Damages fighter and moves health bar
    def damage(self, num):
        self.health -= num
        self.bar.damage(Test.HEALTH, num)

    # Returns tuple of x and y coordinates of hand location
    def get_hand_loc(self):
        if self.direction == 'r':
            x = self.HAND_LOC[0] + self.rect.x
        else:
            x = self.rect.right - self.HAND_LOC[0]
        y = self.HAND_LOC[1] + self.rect.y
        pos = (x, y)
        return pos

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

    # Uses throwable (throwing star)
    def throw(self):
        if pg.time.get_ticks() - self.THROWABLE.COOLDOWN > self.throw_last_used:
            if self.direction == 'r':
                star = ThrowStar(self, self.game, 1)
            else:
                star = ThrowStar(self, self.game, -1)
            self.game.all_sprites.add(star)
            self.game.all_throwables.add(star)
            self.throw_last_used = pg.time.get_ticks()

    def update(self):
        self.animate()
        # Resets acceleration and applies gravity
        self.ax = 0
        self.ay = Test.GRAVITY
        # Horizontal movement
        keys = pg.key.get_pressed()
        if keys[LEFT]:
            self.ax = -Test.ACCEL
            # If clinging to right wall, resets grab_wall to 'n'
            if self.grab_wall == 'r':
                self.grab_wall = 'n'
        elif keys[RIGHT]:
            self.ax = Test.ACCEL
            # If clinging to left wall, resets grab_wall to 'n'
            if self.grab_wall == 'l':
                self.grab_wall = 'n'
        # Applies friction
        self.ax += self.vx * Test.FRICTION
        # Applies acceleration
        self.vx += self.ax
        self.vy += self.ay
        # Stops slow crawl
        if abs(self.vx) < 0.2:
            self.vx = 0
            self.ax = 0
        # Limits velocity to CLING_VLIMIT if fighter is clinging to a wall
        if self.grab_wall != 'n':
            if self.vy > CLING_VLIMIT:
                self.vy = CLING_VLIMIT
        # Applies velocity and sets position
        self.rect.x += self.vx + self.ax * 0.5
        self.rect.y += self.vy + self.ay * 0.5

    # If fighter is grabbing a wall, jumps
    def wall_jump(self, direction):
        # Calls xcollide to check if fighter is grabbing a wall
        hits = self.xcollide(direction)
        if hits:
            # Motion
            self.vy = Test.JUMP
            self.vx = Test.JUMP * direction
            # Resets wall clinging flag to 'n'
            self.grab_wall = 'n'

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


class PunchBag(pg.sprite.Sprite):

    # Dummy stats
    HEALTH = 1000
    GRAVITY = 0.8

    # bar; Health bar
    def __init__(self, bar):
        self.bar = bar
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
        # Health
        self.health = PunchBag.HEALTH

    # Damages fighter and moves health bar
    def damage(self, num):
        self.health -= num
        self.bar.damage(PunchBag.HEALTH, num)

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
