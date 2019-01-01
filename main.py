from settings import *
from objects import Ground, Wall
from fighters import Test
from weapons import TestWeapon
import sys


class Game:

    def __init__(self):
        # Pygame initialization
        pg.init()
        self.screen = pg.display.set_mode(SIZE)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

        # Sprite groups
        self.all_sprites = pg.sprite.Group()
        self.all_objects = pg.sprite.Group()
        self.all_fighters = pg.sprite.Group()
        self.all_weapons = pg.sprite.Group()

    def new(self):
        # Test ground
        self.ground = Ground()
        self.all_sprites.add(self.ground)
        self.all_objects.add(self.ground)
        # Test walls
        self.lwall = Wall('left')
        self.all_sprites.add(self.lwall)
        self.all_objects.add(self.lwall)
        self.rwall = Wall('right')
        self.all_sprites.add(self.rwall)
        self.all_objects.add(self.rwall)
        # Test fighter
        self.test = Test(self)
        self.all_sprites.add(self.test)
        self.all_fighters.add(self.test)
        # Test weapon
        self.weapon = TestWeapon(self.test)
        self.all_sprites.add(self.weapon)
        self.all_weapons.add(self.weapon)
        self.run()

    def run(self):
        # Main loop switch
        self.playing = True
        # Game loop
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.updates()
            self.draw()
            if DEBUG:
                self.debug()

    def collisions(self):
        # Collision handler
        coll = pg.sprite.spritecollide(self.test, self.all_objects, False)
        for c in coll:
            # Ground collision
            if c.ID == 'GND':
                self.test.rect.bottom = c.rect.top
                self.test.vy = 0
            # Wall collisions
            elif c.ID == 'WLL':
                if c.direction == 'left':
                    self.test.rect.left = c.rect.right
                    self.test.vx = 0
                else:
                    self.test.rect.right = c.rect.left
                    self.test.vx = 0

    def events(self):
        # Event handler
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key == SPACE:
                self.test.jump()

    def updates(self):
        # All fighters update
        self.all_fighters.update()
        self.all_weapons.update()
        # Collisions
        self.collisions()

    def draw(self):
        # Pygame draw
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def debug(self):
        # Prints test fighter's velocity, acceleration, and position every frame
        print(self.test.vx, self.test.vy)
        print(self.test.ax, self.test.ay)
        print(self.test.rect.center)


g = Game()
while g.running:
    g.new()


pg.quit()
