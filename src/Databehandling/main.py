# main.py

import sys

import pygame as pg
from Databehandling.utilities.utils import PlotOverview
from utilities import Menu
from settings import *

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Tittel')
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.current_state = Menu()

    def run(self):
        while True:
            current_state = self.current_state
            
            events = pg.event.get()
            navigation, metadata = current_state.handle_events(events)
            
            self.current_state = current_state
            
            if navigation == "start_spill":
                current_state = GameState()
            
            
            if navigation == "quit":
                pg.quit()
                sys.exit()
            
            
            current_state.draw(self.screen)
            pg.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    app = App()
    app.run()