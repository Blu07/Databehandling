# main.py

import pygame as pg
from states import Menu
from settings import *

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Databehandling')
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.state = Menu()

    def run(self):
        while True:
            self.events = pg.event.get()
            self.state.handle_events(self.events)
            self.state.draw(self.screen)
            pg.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    app = App()
    app.run()