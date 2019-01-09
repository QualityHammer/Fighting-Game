from settings import *
from objects import Ground, Wall
from fighters import Test, PunchBag
from weapons import TestWeapon
from stages import Background
from hud import HealthBar
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
        self.all_throwables = pg.sprite.Group()
        self.HUD = pg.sprite.Group()

    def new(self):
        # Health bars
        self.t_health = HealthBar(self.screen, 1)
        self.d_health = HealthBar(self.screen, 2)
        self.HUD.add(self.t_health)
        self.HUD.add(self.d_health)

        # Test ground
        self.ground = Ground()
        self.all_sprites.add(self.ground)
        self.all_objects.add(self.ground)
        # Test walls
        self.lwall = Wall('l')
        self.all_sprites.add(self.lwall)
        self.all_objects.add(self.lwall)
        self.rwall = Wall('r')
        self.all_sprites.add(self.rwall)
        self.all_objects.add(self.rwall)
        # Test fighter
        self.test = Test(self, self.t_health)
        self.all_sprites.add(self.test)
        self.all_fighters.add(self.test)
        # Test weapon
        self.weapon = TestWeapon(self.test)
        self.all_sprites.add(self.weapon)
        self.all_weapons.add(self.weapon)
        # Test Dummy
        self.dummy = PunchBag(self.d_health)
        self.all_sprites.add(self.dummy)
        self.all_fighters.add(self.dummy)
        # Test background
        self.background = Background()
        self.all_sprites.add((self.background))

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
        # Test Fighter Collision handler
        coll = pg.sprite.spritecollide(self.test, self.all_objects, False)
        for c in coll:
            # Ground collision
            if c.ID == 'GND':
                self.test.rect.bottom = c.rect.top
                self.test.vy = 0
            # Wall collisions
            elif c.ID == 'WLL':
                if c.direction == 'l':
                    # Sets wall clinging flag
                    self.test.grab_wall = 'l'
                    self.test.rect.left = c.rect.right
                    self.test.vx = 0
                else:
                    # Sets wall clinging flag
                    self.test.grab_wall = 'r'
                    self.test.rect.right = c.rect.left
                    self.test.vx = 0
        # Dummy Collision handler
        coll = pg.sprite.spritecollide(self.dummy, self.all_objects, False)
        for c in coll:
            # Ground collision
            if c.ID == 'GND':
                self.dummy.rect.bottom = c.rect.top
                self.dummy.vy = 0
            # Wall collisions
            elif c.ID == 'WLL':
                if c.direction == 'left':
                    self.dummy.rect.left = c.rect.right
                    self.dummy.vx = 0
                else:
                    self.dummy.rect.right = c.rect.left
                    self.dummy.vx = 0

    def events(self):
        # Event handler
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == SPACE:
                    self.test.jump()
                elif event.key == C:
                    self.weapon.attack()
                elif event.key == X:
                    self.test.throw()
                # Damage test
                elif event.key == Z:
                    self.test.damage(20)

    def updates(self):
        # All fighters update
        self.all_fighters.update()
        self.all_weapons.update()
        # Collisions
        self.collisions()
        self.all_throwables.update()

    def draw(self):
        # Pygame draw
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        self.all_fighters.draw(self.screen)
        self.all_weapons.draw(self.screen)
        self.HUD.draw(self.screen)
        pg.display.flip()

    def debug(self):
        # Prints test fighter's velocity, acceleration, and position every frame
        print('Test vel:', self.test.vx, self.test.vy)
        print('Test acc:', self.test.ax, self.test.ay)
        print('Test pos:', self.test.rect.center)
        print('Dummy vel:', self.dummy.vx, self.dummy.vy)


g = Game()
while g.running:
    g.new()


pg.quit()
