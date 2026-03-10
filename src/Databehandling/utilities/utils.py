# utils.py

import pygame as pg
import sys

class BaseState:
    def __init__(self):
        self.font = pg.font.SysFont('Arial', 46)

    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def draw(self, screen):
        screen.fill((0, 0, 0))

class Menu(BaseState):
    """ Menu
    """
    def __init__(self):
        super().__init__()

    def handle_events(self, events):
        super().handle_events(events)
    
    def draw(self, screen):
        super().draw(screen)

        # Temporary
        # self.text = self.font.render("text", True, (255, 255, 255))
        # screen.blit(
        #     self.text,
        #     (
        #         screen.get_width() // 2 - self.text.get_width() // 2,
        #         100
        #     )
        # )

        

class PlotOverview(BaseState):
    """ Plot
    """
    def __init__(self):
        super().__init__()

    def handle_events(self, events):
        super().handle_events(events)

    
    def draw(self, screen):
        super().draw(screen)