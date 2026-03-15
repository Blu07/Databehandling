import pygame
from settings import colors


pygame.font.init()

def returnTextWithLine(self, InText:str):
        """
        self (list): classe
        text (str): txt som skal opp deles.
        """
        text = list(InText.split())
        new = []
        i = 0
        while i  < len(text):
            try: 
                # print(new[-1],"::" , text[i])
                int(new[-1][-1])
                int(text[i][0])
                new.append(str(new[-1])+ " "+ str(text[i]))
                new.pop(-2)
                i+=1
            except:
                new.append(text[i])
                i+=1
        # new.append(text[-1])
        text = new
        print(text)
        arrTextSize = []
        for tex in text:
            arrTextSize.append(self.font.size(tex))
        print(arrTextSize)

        new = [text[0]]
        y = 0
        for i in range(len(arrTextSize)-1):
            print(new)
            if self.font.size(new[y])[0] + arrTextSize[i+1][0] < self.buttonsize[0]-5:

                    new[y] = (str(new[y])+ " "+ str(text[i+1]))
                    print(new[y])
            else:
                new.append(text[i+1])
                y+=1
        # print(new)

        return new


class Button:
    def __init__(self,pos,text="none",textCooler=(0,0,0), fontSize = 11, font="Arial" , buttonsize=(100, 100), buttonCooler = (0, 0, 0), returnValue=True, toggle=True, active=True):
        """_summary_
            for å lagge en knap som returner
        Args:
            pos (list): kordinater til knapen
            text (str, optional): Hva som skal sto po kanpen. Defaults to "none".
            textCooler (tuple, optional): farge po teksten. Defaults to (0,0,0).
            fontSize (int, optional): storelse po teksten. Defaults to 11.
            font (str, optional): hvilken type font po texten. Defaults to "Arial".
            buttonsize (tuple, optional): dimisionen po kanppen. Defaults to 100x100 px.
            buttonCooler (tuple, optional): farge po knapen. Defaults to (255,255,255).
            returnValue (bool, optional): hvilken verdi den returner. Defaults to True.
        """
        self.pos = list(pos)
        self.buttonsize = buttonsize

        self.textCooler = textCooler
        self.fontSize = fontSize
        self.font = pygame.font.SysFont(font, fontSize)

        self.toggle = toggle
        self.active = active
        self.returnValue = returnValue # For å velge hvilken verdie som retunerer
        
        self.text = returnTextWithLine(self,text) 

        
        # if buttonsize == True: 
        #     text_width, text_height = self.font.size(self.text)
        #     self.buttonsize = [round(text_width,-1)+50,round(text_height,-1)+10]
        # else:
        #     self.buttonsize = list(buttonsize)
        # print(self.buttonsize)
        self.buttonColer = buttonCooler
        
        
    
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
            if self.toggle and self.active:
                self.active = False
                self.buttonColer = colors["Red"]
            elif self.toggle:
                self.active = True
                self.buttonColer = colors["Blue"]

            return self.returnValue
        return False
    
    def update(self, asd):
        if asd:
            self.active = True
            self.buttonColer = colors["Blue"]
        if asd == False:
            self.active = False
            self.buttonColer = colors["Red"]



    # def draw(self, surface,offset=[0,0]):
    #     """_summary_

    #     Args:
    #         surface (pygame display): hvilken surface som skal bli tegnet po
    #         offset (list, optional): en offset på hvor knappe skal bli tegnet. Defaults to [0,0].
    #     """
    #     button = pygame.Surface((self.buttonsize[0],self.buttonsize[1]), pygame.SRCALPHA, 32).convert_alpha()
    #     button.fill(self.buttonColer)
    #     textimg = self.font.render(self.text, True, self.textCooler)
        
    #     text_width, text_height = self.font.size(self.text)
    #     # rect = self.rect()
    #     center_x =  (self.buttonsize[0]-text_width)/2
    #     center_y =  (self.buttonsize[1]-text_height)/2
    #     button.blit(textimg,(center_x, center_y))
    #     surface.blit(button,(self.pos[0] + offset[0], self.pos[1]+ offset[1]))

    def draw(self,surface, offset=[0,0]):
        """_summary_

        Args:
            surface (pygame display): hvilken surface som skal bli tegnet po
            offset (list, optional): en offset på hvor knappe skal bli tegnet. Defaults to [0,0].
        """
        button = pygame.Surface((self.buttonsize[0],self.buttonsize[1]), pygame.SRCALPHA, 32).convert_alpha()
        button.fill(self.buttonColer)
        textSize_y = 0
        for text in self.text:
            textSize_y += self.font.size(text)[1]+1
        y = (self.buttonsize[1]-textSize_y)/2
        for text in self.text:
            textimg = self.font.render(text, True, self.textCooler)
            
            text_width, text_height = self.font.size(text)
            center_x =  (self.buttonsize[0]-text_width)/2
            button.blit(textimg,(center_x, y))
            y +=  text_height
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

    