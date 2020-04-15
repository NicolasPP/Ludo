import random

import pygame, sys
from pygame.locals import *

color = (40, 210, 250)

width = 1
pygame.init()
table = pygame.display.set_mode((1050,950))
pygame.display.set_caption("ludo")
Text = None
Text_1 = None
p_a = 0
p_b = 0

def draw_board():
    ## board lines horizontal
    pygame.draw.line(table, color, (0, 0), (840,0), width)
    pygame.draw.line(table, color, (0, 280), (840,280), width)
    pygame.draw.line(table, color, (0, 560), (840,560), width)
    pygame.draw.line(table, color, (0, 840), (840,840), width)
    ##middle horizontal lines
    pygame.draw.line(table, color, (0, 380), (320,380), width)
    pygame.draw.line(table, color, (0, 460), (320,460), width)
    pygame.draw.line(table, color, (840, 460), (520,460), width)
    pygame.draw.line(table, color, (840, 380), (520,380), width)
    ## board lines verticle
    pygame.draw.line(table, color, (0, 0), (0,840), width)
    pygame.draw.line(table, color, (280, 0), (280,880), width)
    pygame.draw.line(table, color, (560, 0), (560,880), width)
    pygame.draw.line(table, color, (840, 0), (840,840), width)
    ##middle verticle lines
    pygame.draw.line(table, color, (380, 0), (380,320), width)
    pygame.draw.line(table, color, (460, 0), (460,320), width)
    pygame.draw.line(table, color, (460, 840), (460,520), width)
    pygame.draw.line(table, color, (380, 840), (380,520), width)
    ## diagonal lines
    pygame.draw.line(table, color, (280, 560), (560,280), width)
    pygame.draw.line(table, color, (280, 280), (560,560), width)
    ## inner square
    pygame.draw.line(table, color, (320, 520), (520,520), width)
    pygame.draw.line(table, color, (520,520), (520,320), width)
    pygame.draw.line(table, color, (520,320), (320,320), width)
    pygame.draw.line(table, color, (320,320), (320, 520), width)
    ##tile lines bottom
    pygame.draw.line(table, color, (280, 600), (560,600), width)
    pygame.draw.line(table, color, (280, 640), (560,640), width)
    pygame.draw.line(table, color, (280, 680), (560,680), width)
    pygame.draw.line(table, color, (280, 720), (560,720), width)
    pygame.draw.line(table, color, (280, 760), (560,760), width)
    pygame.draw.line(table, color, (280, 800), (560,800), width)
    ##tile lines right
    pygame.draw.line(table, color, (600, 560), (600,280), width)
    pygame.draw.line(table, color, (640, 560), (640,280), width)
    pygame.draw.line(table, color, (680, 560), (680,280), width)
    pygame.draw.line(table, color, (720, 560), (720,280), width)
    pygame.draw.line(table, color, (760, 560), (760,280), width)
    pygame.draw.line(table, color, (800, 560), (800,280), width)
    ##tile lines up
    pygame.draw.line(table, color, (280, 240), (560,240), width)
    pygame.draw.line(table, color, (280, 200), (560,200), width)
    pygame.draw.line(table, color, (280,160), (560,160), width)
    pygame.draw.line(table, color, (280, 120), (560,120), width)
    pygame.draw.line(table, color, (280, 80), (560,80), width)
    pygame.draw.line(table, color, (280, 40), (560,40), width)
    ##tile lines left
    pygame.draw.line(table, color, (240, 280), (240,560), width)
    pygame.draw.line(table, color, (200, 280), (200,560), width)
    pygame.draw.line(table, color, (160, 280), (160,560), width)
    pygame.draw.line(table, color, (120, 280), (120,560), width)
    pygame.draw.line(table, color, (80, 280), (80,560), width)
    pygame.draw.line(table, color, (40, 280), (40,560), width)
    ## blue circles
    pygame.draw.circle(table, (0,0,128), (80,80), 20, 0)
    pygame.draw.circle(table, (0,0,128), (200,80), 20, 0)
    pygame.draw.circle(table, (0,0,128), (80,200), 20, 0)
    pygame.draw.circle(table, (0,0,128), (200,200), 20, 0)
    ## yellow circles
    pygame.draw.circle(table, (255,255,0), (640,80), 20, 0)
    pygame.draw.circle(table, (255,255,0), (760,80), 20, 0)
    pygame.draw.circle(table, (255,255,0), (760,200), 20, 0)
    pygame.draw.circle(table, (255,255,0), (640,200), 20, 0)
    ## red circles
    pygame.draw.circle(table, (255,0,0), (80,640), 20, 0)
    pygame.draw.circle(table, (255,0,0), (80,760), 20, 0)
    pygame.draw.circle(table, (255,0,0), (200,760), 20, 0)
    pygame.draw.circle(table, (255,0,0), (200,640), 20, 0)
    ## green circles
    pygame.draw.circle(table, (0,128,0), (640,640), 20, 0)
    pygame.draw.circle(table, (0,128,0), (640,760), 20, 0)
    pygame.draw.circle(table, (0,128,0), (760,760), 20, 0)
    pygame.draw.circle(table, (0,128,0), (760,640), 20, 0)
    # button
    dice.draw(table,color)
    #line below buttonsdsd
    pygame.draw.line(table, color, (280, 880), (560,880), width)


def dice_roll():
    global Text,Text_1, p_a, p_b
    a = random.randint(1,6)
    b = random.randint(1,6)
    font = pygame.font.SysFont('comicsans', 40)
    if Text_1 and Text:
        Text = font.render(str(p_a), 1, (0,0,0))
        table.blit(Text, (280 + (100/2 - Text.get_width()/2), 840 + (40/2 - Text.get_height()/2)))
        Text_1 = font.render( str(p_b),1, (0,0,0))
        table.blit(Text_1, (460 + (100/2 - Text_1.get_width()/2), 840 + (40/2 - Text_1.get_height()/2)))
    Text = font.render(str(a), 1, (40, 210, 250))
    table.blit(Text, (280 + (100/2 - Text.get_width()/2), 840 + (40/2 - Text.get_height()/2)))
    Text_1 = font.render(str(b), 1, (40, 210, 250))
    table.blit(Text_1, (460 + (100/2 - Text_1.get_width()/2), 840 + (40/2 - Text_1.get_height()/2)))
    p_a = a
    p_b = b



class button():
    def __init__(self, colour, x,y,Width,height, text=''):
        self.colour = colour
        self.x = x
        self.y = y
        self.Width = Width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.Width+4,self.height+4),0)

        pygame.draw.rect(win, self.colour, (self.x,self.y,self.Width,self.height),0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 20)
            text = font.render(self.text, 1, (40, 210, 250))
            win.blit(text, (self.x + (self.Width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.Width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

dice = button((0,0,0),382,842,77,37,"roll dice")


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            dice_roll()

    draw_board()
    pygame.display.update()
