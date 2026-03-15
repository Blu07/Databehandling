# utils.py

import pygame as pg
import sys
import threading
import matplotlib.pyplot as plt
from utilities import Button, returnData, returnAar,returnAntRom, returnSoner
from settings import colors
from utilities import Slider
import matplotlib.pyplot as plt
from plot.linje import plotLinje

import multiprocessing

class Menu():
    """ Menu
    """
    def __init__(self):
        self.axis_title = True
        self.legend = True
        self.average = True
        self.grid = True

        self.showRom = False
        self.showSoner = False

        self.dataPath = "data/leieMonde.json"

        self.buttons = [
            Button((100, 50), "Aksetitler", colors["Black"], 24, None, (110, 110), colors["Blue"], "axis_title", True),
            Button((100, 175), "Legend", colors["Black"], 24, None, (110, 110), colors["Blue"], "legend", True),
            Button((100, 300), "Gjennomsnitt", colors["Black"], 24, None, (110, 110), colors["Blue"], "average", True),
            Button((100, 425), "Grid", colors["Black"], 24, None, (110, 110), colors["Blue"], "grid", True),
            Button((300, 50), "Antal Rom", colors["Black"], 24, None, (110, 110), colors["Red"], "rom", True, False),
            Button((300, 175), "Soner", colors["Black"], 24, None, (110, 110), colors["Red"], "soner", True, False),
            Button((650, 425), "Plott", colors["Black"], 24, None, (250, 110), colors["Green"], "plot", False)
        ]

        self.buttonsRoms= self.Selctor((500,50),(500,300),(120,120),5,returnAntRom(self.dataPath))
        self.buttonsSoner= self.Selctor((500,50),(500,300),(120,120),5, returnSoner(self.dataPath))


        self.slider = Slider(300, 20, 300, 450, colors["Red"], returnAar(self.dataPath))

    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if self.showRom:
                    for button in self.buttonsRoms:
                        button.click(pg.mouse.get_pos())
                elif self.showSoner:
                    for button in self.buttonsSoner:
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
                            self.showSoner = False
                        elif button.returnValue == "soner":
                            self.showSoner = not self.showSoner
                            self.showRom = False
                        elif button.returnValue == "plot":
                            self.plot(self.axis_title, self.legend, self.average, self.grid)
        self.slider.drag_slider()
        for button in self.buttons:
            if button.returnValue == "rom":
                button.update(self.showRom)
            elif button.returnValue == "soner":
                button.update(self.showSoner)
                
                

    
    def draw(self, screen):
        screen.fill((200, 200, 200))
        # pg.draw.rect(screen,colors["Red"],(500,50,500,300)) # viser hvor knapper kommer
        for button in self.buttons:
            button.draw(screen)

        if self.showRom:
            for button in self.buttonsRoms:
                button.testDraw(screen) 
        elif self.showSoner:
            for button in self.buttonsSoner:
                button.testDraw(screen) 


        self.slider.draw(screen)
        

    def Selctor(self,boxPos,boxSize, buttnSize, padding, elements):
        anttalKnappIx = boxSize[0]//buttnSize[0]
        anttalKnappIy = boxSize[1]//buttnSize[1] # kan brukes for finn ut om knappen tar for mye plass
        x = 0
        y = 0
        i = 0
        arr = []
        for elemwnt in elements:

            if x!=0 and anttalKnappIx%x:
                y+=1
                x=0

            button = Button((((buttnSize[0]+padding)*x+boxPos[0],(buttnSize[1]+padding)*y+boxPos[1])), str(elemwnt), colors["Black"], 24, None, buttnSize, colors["Red"],i , True ,False)
            arr.append(button)
            x+=1
            i+=1
        return arr
            

    def plot(self, axis_title, legend, average, grid):

        data = returnData(self.dataPath)
        plotData = []

        for buttonRom in self.buttonsRoms:
            if buttonRom.active:
                temp = []
                for buttonSoner in self.buttonsSoner:
                    if buttonSoner.active:
                        temp.append(data[buttonRom.returnValue][buttonSoner.returnValue])
                plotData.append(temp)
        
        # print(plotData)

        p = multiprocessing.Process(target=plotLinje, args=(plotData,returnAar(self.dataPath)))
        p.daemon = True
        p.start()
        # t = threading.Thread(target=plotLinje,name="ploting",args=((plotData,returnAar(self.dataPath))))
        # t.daemon = True # Gjøre at den nye treaden vil avslutte når hoved treaden avsluter
        # t.start()
        

        # print("plotting graph", returnData(self.dataPath))