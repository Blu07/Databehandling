import pygame as pg
from settings import COLORS

class Slider:
    def __init__(self, width, height, x, y, box_col, options=list):
        self.width = width
        self.height = height
        self.pos_x = x
        self.pos_y = y
        self.box_col = box_col
        self.option_select = 0
        self.options = options
        self.radius = 15
        self.circle_x = self.pos_x
        self.circle_y = self.pos_y + 10

    def drag_slider(self):
        if pg.mouse.get_pressed()[0] and self.rect(100).collidepoint(pg.mouse.get_pos()):
            if pg.mouse.get_pos()[0] >= self.pos_x + self.width:
                print(self.circle_x)
                self.circle_x = self.pos_x + self.width
            elif pg.mouse.get_pos()[0] <= self.pos_x:
                self.circle_x = self.pos_x
            else:
                self.circle_x = pg.mouse.get_pos()[0]
            

    def rect(self, extra_height):
        return pg.Rect(self.pos_x, self.pos_y - extra_height, self.width, self.height + extra_height * 2)

    def draw(self, screen):
        pg.draw.rect(screen, self.box_col, self.rect(0))
        pg.draw.circle(screen, COLORS["White"], (self.circle_x, self.circle_y), self.radius)