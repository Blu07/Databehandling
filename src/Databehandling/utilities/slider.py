import pygame as pg
from settings import colors

class Slider:
    def __init__(self, width, height, x, y, box_col, options: list[int]):
        """ Slider class

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int): x position of the rectangle
            y (int): y position of the rectangle
            box_col (tuple): a tuple with a color value
            options (list, optional): list of total years. Defaults to list.
            radius (int): radius of the circle
            circle_x (int): x position of the circle
            circl_y (int): y position of the circle
        """
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
        """ Drag function for the slider

            Adding and extra 100 on the y-height for the hitbox so that you can drag even when you are slightly off in y-value
            Also adds a limit so you can't drag the circle outside of the rectangle.
        """
        if pg.mouse.get_pressed()[0] and self.rect(100).collidepoint(pg.mouse.get_pos()):
            if pg.mouse.get_pos()[0] >= self.pos_x + self.width:
                print(self.circle_x)
                self.circle_x = self.pos_x + self.width
            elif pg.mouse.get_pos()[0] <= self.pos_x:
                self.circle_x = self.pos_x
            else:
                self.circle_x = pg.mouse.get_pos()[0]
            

    def rect(self, extra_height):
        """ Rect object for the slider

        Args:
            extra_height (int): used to create a larger hitbox on the y-axis so that you can more easily move the slider

        Returns:
            rect: Rect object for slider
        """
        return pg.Rect(self.pos_x, self.pos_y - extra_height, self.width, self.height + extra_height * 2)

    def draw(self, screen):
        """ Drawing the rectangle and circle for the slider

        Args:
            screen (surface): surface
        """
        pg.draw.rect(screen, self.box_col, self.rect(0))    # Zero extra y-height for the red rectangle
        pg.draw.circle(screen, colors["White"], (self.circle_x, self.circle_y), self.radius)