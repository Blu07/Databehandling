# utils.py

import pygame as pg
import sys
import threading
import matplotlib.pyplot as plt
from utilities import Button, returnData, returnAar
from settings import colors
from utilities import Slider
import matplotlib.pyplot as plt
from plot.linje import plotLinje

class Menu():
    """ Menu
    """
    def __init__(self):
        self.axis_title = True
        self.legend = True
        self.average = True
        self.grid = True

        self.showRom = False

        self.dataPath = "data/leieMonde.json"

        self.buttons = [
            Button((100, 50), "Aksetitler", colors["Black"], 24, None, (110, 110), colors["Blue"], "axis_title", True),
            Button((100, 175), "Legend", colors["Black"], 24, None, (110, 110), colors["Blue"], "legend", True),
            Button((100, 300), "Gjennomsnitt", colors["Black"], 24, None, (110, 110), colors["Blue"], "average", True),
            Button((100, 425), "Grid", colors["Black"], 24, None, (110, 110), colors["Blue"], "grid", True),
            Button((300, 50), "Antal Rom", colors["Black"], 24, None, (110, 110), colors["Blue"], "rom", True),
            Button((650, 425), "Plott", colors["Black"], 24, None, (250, 110), colors["Green"], "plot", False)
        ]
        self.buttonsRoms=[]
        anttalKnappIx = 500//110
        anttalKnappIy = 300//110
        x = 0
        y = 0
        for rom in range(5):

            if x!=0 and anttalKnappIx%rom:
                y+=1
                x=0

            button = Button(((120*x+500,120*y+50)), "Rom "+ str(rom+1), colors["Black"], 24, None, (110,110), colors["Blue"], True, True ,False)
            self.buttonsRoms.append(button)
            x+=1

        self.slider = Slider(300, 20, 300, 400, colors["Red"], returnAar(self.dataPath))

    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if self.showRom:
                    for button in self.buttonsRoms:
                        button.click(pg.mouse.get_pos())

                for button in self.buttons:
                    if button.click(pg.mouse.get_pos()):
                        if button.returnValue == "axis_title":
                            self.axis_title = not self.axis_title
                            print(self.axis_title)
                        elif button.returnValue == "legend":
                            self.legend = not self.legend
                            print(self.legend)
                        elif button.returnValue == "average":
                            self.average = not self.average
                            print(self.average)
                        elif button.returnValue == "grid":
                            self.grid = not self.grid
                            print(self.grid)
                        elif button.returnValue == "rom":
                            self.showRom = not self.showRom
                        elif button.returnValue == "plot":
                            self.plot(self.axis_title, self.legend, self.average, self.grid)
        self.slider.drag_slider()
    
    def draw(self, screen):
        screen.fill((200, 200, 200))
        pg.draw.rect(screen,colors["Red"],(500,50,500,300))
        for button in self.buttons:
            button.draw(screen)

        if self.showRom:
            for Button in self.buttonsRoms:
                Button.draw(screen) 

        self.slider.draw(screen)
        

    def Selctor(self,screen):
        pass

    def plot(self, axis_title, legend, average, grid):
        t = threading.Thread(target=plotLinje,name="ploting",args=((returnData(self.dataPath)[0],returnAar(self.dataPath))))
        t.daemon = True # Gjøre at den nye treaden vil avslutte når hoved treaden avsluter
        t.start()
        # plotLinje(returnData(self.dataPath),returnAar(self.dataPath))
        # print("plotting graph", returnData(self.dataPath))