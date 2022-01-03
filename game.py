import pygame
import copy
import cell_class
import random
vec = pygame.math.Vector2
GAMECOLOR = (240, 83, 101)

class Game_window:
    def __init__(self, screen, x, y):
        self.rows = 38
        self.cols = 38
        self.screen = screen
        self.pos = vec(x,y)
        self.width, self.height = 570, 570
        #set up game surface (where the game will run)
        self.image = pygame.Surface((self.width, self.height))
        #pygameSurface has a method get_rect that returns a rectangle its size
        self.rect = self.image.get_rect()        
        #list of list of Cell objects, size: rows, cols
        self.grid = [[cell_class.Cell(self.image, x, y, self.rows, self.cols) for x in range(self.cols)] for y in range(self.rows)]
        for row in self.grid:
            for cell in row:
                cell.get_neighbors(self.grid)
    def update(self):
        #put rectangle in the position we want
        self.rect.topleft = self.pos
        for row in self.grid:
            for cell in row:
                cell.update()
    def draw(self):
        self.image.fill(GAMECOLOR)
        for row in self.grid:
            for cell in row:
                cell.draw()
        self.screen.blit(self.image, (self.pos.x, self.pos.y))
    def reset_grid(self):
        self.grid = [[cell_class.Cell(self.image, x, y, self.rows, self.cols) for x in range(self.cols)] for y in range(self.rows)]
    #what will control the game
    def rules(self):
        #count number of alive neig
        for row in self.grid:
            for cell in row:
                cell.live_neighbors()
        #replicate grid, don't want to manipulate original grid
        grid_copy = copy.copy(self.grid)
        #go through original grid, update grid_copy
        for yidx, row in enumerate(self.grid):
            for xidx, cell in enumerate(row):
                if cell.alive:
                    #live cell with less than 2 live neighbors dies
                    if cell.alive_neighbors < 2:
                        grid_copy[yidx][xidx].alive = False
                    #live cell with more than 3 live neighbors dies
                    elif cell.alive_neighbors > 3:
                        grid_copy[yidx][xidx].alive = False
                    #live cell with 2 or 3 live neighbors lives
                    elif cell.alive_neighbors == 2 or cell.alive_neighbors == 3 and cell.alive:
                        grid_copy[yidx][xidx].alive = True
                #dead cell with 3 neighbors comes alive
                else:
                    if cell.alive_neighbors == 3:
                        grid_copy[yidx][xidx].alive = True
        self.grid = grid_copy
                
                
