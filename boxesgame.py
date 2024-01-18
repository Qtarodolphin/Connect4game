import sys,os,pygame,time
from pygame.locals import * 

class BoxesGame():
    def initGraphics(self):
        self.normallinev=pygame.image.load("normalline.png")
        self.normallineh=pygame.transform.rotate(pygame.image.load("normalline.png"), -90)
        self.bar_donev=pygame.image.load("bar_done.png")
        self.bar_doneh=pygame.transform.rotate(pygame.image.load("bar_done.png"), -90)
        self.hoverlinev=pygame.image.load("hoverline.png")
        self.hoverlineh=pygame.transform.rotate(pygame.image.load("hoverline.png"), -90)
        
    def _init_(self):
        pygame.init()
        width, height=389,489

        self.screen=pygame.display.set_mode((width, height))
        pygame.display.set_caption("Boxes")

        self.clock=pygame.time.Clock()
        self.boardh = [[False for x in range(6)] for y in range(7)]
        self.boardv = [[False for x in range(7)] for y in range(6)]
        
        self.initGraphics()
        
        

    def update(self):
        self.clock.tick(60)

        self.screen.fill(0,244,254)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()

        pygame.display.flip()

bg=BoxesGame()
while 1:
    bg._init_()
    bg.update()
