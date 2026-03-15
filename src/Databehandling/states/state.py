# utils.py


import pygame
import matplotlib
import matplotlib.backends.backend_agg as agg
import pylab

import sys

from plot.linje import plot_to_figure
from utilities import Button, returnData, returnAar,returnAntRom, returnSoner
from settings import PLOT_POS, COLORS, PLOT_WIDTH_INCHES, PLOT_HEIGHT_INCHES, DPI
from utilities import Slider

# from plot.linje import plotLinje, plotter

# import threading
# import multiprocessing

class Menu():
    """ Menu
    """
    def __init__(self):
        self.plot = None
        
        self.show_axis_labels_button = Button(( 50,  50),  "Aksetitler", COLORS["Black"], 24, "Arial", (110, 110), COLORS["Blue"], "axis_title", True, True, self)
        self.show_legend_button = Button(( 50, 175), "Legend", COLORS["Black"], 24, "Arial", (110, 110), COLORS["Blue"], "legend", True, True, self)
        self.show_average_button = Button(( 50, 300), "Gjennomsnitt", COLORS["Black"], 24, "Arial", (110, 110), COLORS["Blue"], "average", True, True, self)
        self.show_inflation_button = Button(( 50, 425), "Inflasjon", COLORS["Black"], 24, "Arial", (110, 110), COLORS["Blue"], "inflasjon", True, True, self)
        self.show_grid_button = Button(( 50, 550), "Grid", COLORS["Black"], 24, "Arial", (110, 110), COLORS["Blue"], "grid", True, True, self)
        self.show_y_lim_button = Button(( 50, 675), "y-lim 0", COLORS["Black"], 24, "Arial", (110, 110), COLORS["Blue"], "ylim", True, True, self)
        
        self.show_rom_button = Button((300,  50), "Antal Rom", COLORS["Black"], 24, "Arial", (110, 110), COLORS["Red"], "rom", True, False, self, False)
        self.show_soner_button = Button((450,  50), "Soner", COLORS["Black"], 24, "Arial", (110, 110), COLORS["Red"], "soner", True, False, self, False)
        

        self.buttons = [
            self.show_average_button,
            self.show_axis_labels_button,
            self.show_legend_button,
            self.show_grid_button,
            self.show_y_lim_button,
            self.show_inflation_button,
            self.show_rom_button,
            self.show_soner_button
        ]

        self.buttonsRoms = self.Selctor((300,210), (500,300), (110,110), 5, returnAntRom())
        self.buttonsSoner = self.Selctor((450,210), (500,300), (110,110), 5, returnSoner())


        self.slider = Slider(300, 20, 600, 95, COLORS["Red"], returnAar())
        
        self.create_plot()

        
    def handle_events(self, events):
        
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    returnValue = button.click(pygame.mouse.get_pos())
                    if returnValue == "soner":                          
                        self.show_rom_button.update(False)
         
                    if returnValue == "rom":
                        self.show_soner_button.update(False)
                
                
                if self.show_rom_button.active:
                    for Button in self.buttonsRoms:
                        Button.click(pygame.mouse.get_pos())
                            
                if self.show_soner_button.active:
                    for Button in self.buttonsSoner:
                        Button.click(pygame.mouse.get_pos())

        
                
        self.slider.drag_slider()
    
    
    def draw(self, screen):
        screen.fill((200, 200, 200))
        
        
        if self.plot:
            screen.blit(self.plot, PLOT_POS)
            
        for button in self.buttons:
            button.draw(screen)

        if self.show_rom_button.active:
            for Button in self.buttonsRoms:
                Button.draw(screen)
                
        if self.show_soner_button.active:
            for Button in self.buttonsSoner:
                Button.draw(screen) 


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

            button = Button((((buttnSize[0]+padding)*x+boxPos[0],(buttnSize[1]+padding)*y+boxPos[1])), str(elemwnt), COLORS["Black"], 24, None, buttnSize, COLORS["Red"], i, True, True, self, False)
            arr.append(button)
            x+=1
            i+=1
        return arr
    

    def create_plot(self):
                
        matplotlib.use("Agg")

        # Create the data array
        data = returnData()
        plotData = []
        
        rom_soner_index = []
        antRom = returnAntRom()
        sone = returnSoner()

        for buttonRom in self.buttonsRoms:
            if buttonRom.active:
                temp = []
                for buttonSoner in self.buttonsSoner:
                    if buttonSoner.active:
                        rom = antRom[buttonRom.returnValue]
                        soner = sone[buttonSoner.returnValue]
                        
                        rom_soner_index.append(f"{rom}, {soner}")
                        temp.append(data[buttonRom.returnValue][buttonSoner.returnValue])
                plotData.append(temp)
                

        fig = pylab.figure(figsize=[PLOT_WIDTH_INCHES, PLOT_HEIGHT_INCHES], dpi=DPI)
        
        plot_to_figure(
            fig=fig,
            data=plotData,
            rom_soner_index=rom_soner_index,
            aar=returnAar(),
            show_legend=self.show_legend_button.active,
            show_grid=self.show_grid_button.active,
            show_axis_labels=self.show_axis_labels_button.active,
            y_lim_zero=self.show_y_lim_button.active,
            show_inflation=self.show_inflation_button.active,
            show_average=self.show_average_button.active,
            title="Leiepris gitt antall rom, områder og år.",
            x_label="År",
            y_label="Leiepris"
        )

        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_argb()
        size = canvas.get_width_height()

        surf = pygame.image.fromstring(raw_data, size, "ARGB")
        self.plot = surf
        