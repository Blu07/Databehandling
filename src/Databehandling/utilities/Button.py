import pygame


pygame.font.init()


class Button:
    def __init__(self,pos,text="none",textCooler=(0,0,0), fontSize = 11, font="Arial" , buttonsize=True, buttonCooler =(255,255,255) , returnValue=True):
        """_summary_
            for å lagge en knap som returner
        Args:
            pos (list): kordinater til knapen
            text (str, optional): Hva som skal sto po kanpen. Defaults to "none".
            textCooler (tuple, optional): farge po teksten. Defaults to (0,0,0).
            fontSize (int, optional): storelse po teksten. Defaults to 11.
            font (str, optional): hvilken type font po texten. Defaults to "Arial".
            buttonsize (bool, optional): dimisionen po kanppen. Defaults to True.
            buttonCooler (tuple, optional): farge po knapen. Defaults to (255,255,255).
            returnValue (bool, optional): hvilken verdi den returner. Defaults to True.
        """
        self.pos = list(pos)
        
        self.text = text
        self.textCooler = textCooler
        self.fontSize = fontSize
        self.font = pygame.font.SysFont(font, fontSize)
        
        if buttonsize == True: 
            text_width, text_height = self.font.size(self.text)
            self.buttonsize = [round(text_width,-1)+50,round(text_height,-1)+10]
        else:
            self.buttonsize = list(buttonsize)
        # print(self.buttonsize)
        self.buttonColer = buttonCooler
        
        

        
        self.returnValue = returnValue # For å velge hvilken verdie som retunerer
        

    
    def rect(self):
        """_summary_

        Returns:
            pygame rect: return rectangl values for the button
        """
        return  pygame.Rect(self.pos[0],self.pos[1],self.buttonsize[0],self.buttonsize[1])
    
    def click(self, pos):
        """_summary_

        Args:
            pos (list:(float, float)): list av mus kordinater

        Returns:
            _type_: retuner ennten en retuner verdi eller True når knappen blir trykt
        """
        rect = self.rect()
        if rect.collidepoint(pos):
            # return True
            return self.returnValue
        return False
    
    def update(self,offset):
        # self.pos[0] += offset[0]
        # self.pos[1] += offset[1]
        # print(self.pos)
        pass


    def draw(self, surface,offset=[0,0]):
        """_summary_

        Args:
            surface (pygame display): hvilken surface som skal bli tegnet po
            offset (list, optional): en offset på hvor knappe skal bli tegnet. Defaults to [0,0].
        """
        button = pygame.Surface((self.buttonsize[0],self.buttonsize[1]), pygame.SRCALPHA, 32).convert_alpha()
        button.fill(self.buttonColer)
        textimg = self.font.render(self.text, True, self.textCooler)
        
        text_width, text_height = self.font.size(self.text)
        # rect = self.rect()
        center_x =  (self.buttonsize[0]-text_width)/2
        center_y =  (self.buttonsize[1]-text_height)/2
        button.blit(textimg,(center_x, center_y))
        surface.blit(button,(self.pos[0] + offset[0], self.pos[1]+ offset[1]))


class ButtonFunk(Button):
        def __init__(self, pos, funk, text="none", textCooler=(0, 0, 0), fontSize=11, font="Arial", buttonsize=True, buttonCooler=(255, 255, 255)):
            super().__init__(pos, text, textCooler, fontSize, font, buttonsize)
            self.funk = funk
            self.buttoncooler = buttonCooler
           
        def click_Funk(self, pos):
            """_summary_
                utfører en funksjon når knappen blir trykt
            Args:
                pos (list:(float, float)): list av mus kordinater
            """
            if self.funk == None:
                print("Error: Det er ikke git en funksjon til knappen")
                return
            rect = self.rect()
            if rect.collidepoint(pos):
                self.funk()

    
