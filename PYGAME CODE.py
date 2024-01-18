import pygame

import os
import time

TITLE = "Draw grid"
WINDOWS_LOCATION = '100,100'
WIDTH = 710
HEIGHT = 710
FPS = 1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

CELL_SIZE = 15
GRID_COORD_MARGIN_SIZE = 20

class Grid():
    def __init__(self, surface, cellSize, axisLabels):
        self.surface = surface
        self.colNb = surface.get_width() // cellSize
        self.lineNb = surface.get_height() // cellSize
        self.cellSize = cellSize
        self.axisLabels = axisLabels
        self.grid = [[0 for i in range(self.colNb)] for j in range(self.lineNb)]
        self.font = pygame.font.SysFont('arial', 12, False)

    def drawUseRect(self):
        for li in range(self.lineNb):
            liCoord = GRID_COORD_MARGIN_SIZE + li * CELL_SIZE
            if self.axisLabels:
                if li < 10:
                    ident = '   '
                else:
                    ident = '  '
                text = self.font.render(ident + str(li), 1, (0, 0, 0))
                self.surface.blit(text, (0, liCoord))
            for co in range(self.colNb):
                colCoord = GRID_COORD_MARGIN_SIZE + co * CELL_SIZE
                if self.axisLabels:
                    if co < 10:
                        ident = '  '
                    else:
                        ident = ' '
                    text = self.font.render(ident + str(co), 1, (0, 0, 0))
                    self.surface.blit(text, (colCoord, 1))
                pygame.draw.rect(self.surface, BLACK, pygame.Rect(liCoord, colCoord, CELL_SIZE, CELL_SIZE), 1)

    def drawUseLine(self):
        for li in range(self.lineNb):
            liCoord = GRID_COORD_MARGIN_SIZE + li * CELL_SIZE
            if self.axisLabels:
                if li < 10:
                    ident = '   '
                else:
                    ident = '  '
                text = self.font.render(ident + str(li), 1, (0, 0, 0))
                self.surface.blit(text, (0, liCoord))
            pygame.draw.line(self.surface, BLACK, (GRID_COORD_MARGIN_SIZE, liCoord), (self.surface.get_width(), liCoord))
        for co in range(self.colNb):
            colCoord = GRID_COORD_MARGIN_SIZE + co * CELL_SIZE
            if self.axisLabels:
                if co < 10:
                    ident = '  '
                else:
                    ident = ' '
                text = self.font.render(ident + str(co), 1, (0, 0, 0))
                self.surface.blit(text, (colCoord, 1))
            pygame.draw.line(self.surface, BLACK, (colCoord, GRID_COORD_MARGIN_SIZE), (colCoord,self.surface.get_height()))

# setting Pygame window position (ok on Windows ...)
os.environ['SDL_VIDEO_WINDOW_POS'] = WINDOWS_LOCATION

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
running = True
axisLabels = False

grid = Grid(surface=screen, cellSize=CELL_SIZE, axisLabels=axisLabels)

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    start = time.time()
    grid.drawUseRect()
    print("draw using rect: {}".format(time.time() - start))

    start = time.time()
    grid.drawUseLine()
    print("draw using line: {}".format(time.time() - start))

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
