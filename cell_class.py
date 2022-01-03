import pygame
cell_side = 15 #measurement of 1 side of cell (cells are always square, don't need width and height)
class Cell:
    def __init__(self, surface, grid_x, grid_y, game_rows, game_cols):
        self.alive = False #dead by default
        self.surface = surface
        #position x and y
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.image = pygame.Surface((cell_side,cell_side)) 
        self.rect = self.image.get_rect()
        self.neighbors = [] #get_neighbors() will add to this list
        self.alive_neighbors = 0
        #these will be used later (in get_neighbors)
        self.game_rows = game_rows
        self.game_cols = game_cols

    def update(self):
        self.rect.topleft = (self.grid_x*cell_side, self.grid_y*cell_side)
        
    def draw(self):
        if not self.alive:
            self.image.fill((242, 242, 242)) #dark cells are dead
            pygame.draw.rect(self.image, (212, 116, 150), (1,1,20,20)) #second tuple controls the size of the border
        else:
            self.image.fill((242, 242, 242))
            
        self.surface.blit(self.image, (self.grid_x*cell_side, self.grid_y*cell_side))
    def get_size(self):
        return cell_side
    
    def get_neighbors(self, grid):
        #list of the positions of all neighbors relative to the cell itself
        neighbor_list = [[1,1], [-1,-1], [-1,1], [1, -1], [0,-1], [0,1], [1,0], [-1, 0]]
        #add grid_x and grid_y to x and y positions to get absolute positions of neighbors (not relative to cell)
        neighbor_list = [[neighbor[0]+self.grid_x, neighbor[1]+self.grid_y] for neighbor in neighbor_list]
        #cells on the edge have "nonexistent" neighbors, this fixes coordinates of non-existent neighbors
        #every coordinate in neighbor_list will actually be a cell that exists
        for neighbor in neighbor_list:
            if neighbor[0] < 0:
                neighbor[0] += self.game_rows
            if neighbor[1] < 0:
                neighbor[1] += self.game_cols
            if neighbor[0] > self.game_rows-1:
                neighbor[0] -= self.game_rows
            if neighbor[1] > self.game_cols-1:
                neighbor[1] -= self.game_cols
        for neighbor in neighbor_list:
            try:
                self.neighbors.append(grid[neighbor[1]][neighbor[0]])
            except:
                print(neighbor)
    def live_neighbors(self):
        count = 0
        #count number of alive neighbors
        for neighbor in self.neighbors:
            if neighbor.alive:
                count += 1
        self.alive_neighbors = count
            
