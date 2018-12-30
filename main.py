from settings import *
from objects import Ground
from fighters import Test
import sys


class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(SIZE)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

        # Sprite groups
        self.all_sprites = pg.sprite.Group()
        self.all_objects = pg.sprite.Group()
        self.all_fighters = pg.sprite.Group()

    def new(self):
        # Test ground
        self.ground = Ground()
        self.all_sprites.add(self.ground)
        self.all_objects.add(self.ground)
        # Test fighter
        self.test = Test(self)
        self.all_sprites.add(self.test)
        self.all_fighters.add(self.test)
        self.run()

    def run(self):
        self.playing = True
        self.screen.fill(WHITE)
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.updates()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key == SPACE:
                self.test.jump()

    def updates(self):
        # All fighters update
        self.all_fighters.update()
        # Ground collision
        if self.test.vy > 0:
            coll = pg.sprite.spritecollide(self.test, self.all_objects, False)
            if coll:
                self.test.posy = coll[0].rect.top
                self.test.vy = 0

    def draw(self):
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        pg.display.flip()


g = Game()
while g.running:
    g.new()


pg.quit()
