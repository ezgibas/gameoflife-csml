import sys
import pygame
import game
from cell_class import Cell
from button_class import Button

WIDTH, HEIGHT = 700, 700 #size of game window
BACKGROUND = (147, 149, 211) #background color of window
FPS = 60 #how fast the frames will change

"""

GAME MAINTAINING FUNCTIONS

contains 3 versions of these functions:

get_events(): checks if you clicked quit, or if you clicked the mouse
update(): updates the window and buttons
draw(): draws the components of the game

versions:
'setting' state: before the game starts
'running' state: while game is running
'paused' state: game is paused

"""
# ------------------------------------------
"""SETTING STATE FUNCTIONS"""
def get_events():
    global running
    for event in pygame.event.get():
        #turning off game
        if event.type == pygame.QUIT:
            running = False
        #Mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:   
            mouse_pos = pygame.mouse.get_pos() #get position of mouse
            #if mouse is on grid, make cells alive/dead
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            #if mouse isn't on grid, check if it's on buttons
            else:
                for button in buttons:
                    button.click()
def update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos)
def draw():
    window.fill(BACKGROUND)
    game_window.draw()
    for button in buttons:
        button.draw()
# -----------------------------------------------------------------------

"""RUNNING STATE FUNCTIONS"""
def running_get_events():
    global running
    for event in pygame.event.get():
        #turning off game
        if event.type == pygame.QUIT:
            running = False
        #Mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:   
            mouse_pos = pygame.mouse.get_pos() #get position of mouse
            #if mouse is on grid, make cells alive/dead
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            #if mouse isn't on grid, check if it's on buttons
            else:
                for button in buttons:
                    button.click()
def running_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos)
    if frame_count%(FPS//10) == 0:
        game_window.rules()
    #game_window.rules()
def running_draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()
    
# ------------------------------------------------------------------------

"""PAUSED STATE FUNCTIONS"""
def paused_get_events():
    global running
    for event in pygame.event.get():
        #turning off game
        if event.type == pygame.QUIT:
            running = False
        #Mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:   
            mouse_pos = pygame.mouse.get_pos() #get position of mouse
            #if mouse is on grid, make cells alive/dead
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            #if mouse isn't on grid, check if it's on buttons
            else:
                for button in buttons:
                    button.click()
def paused_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos)
def paused_draw():
    window.fill(BACKGROUND)
    game_window.draw()
    for button in buttons:
        button.draw()
# --------------------------------------------------------------------------

"""MOUSE POSITION & CLICKING FUNCTIONS"""
def mouse_on_grid(pos):
    #check x coordinates first, it should be between origin_x and the end of the game window (80 to 650)
    if pos[0] > origin_x and pos[0] <  (origin_x + game_window.width):
        #check y coordinates, between origin_y and end of window (80 to 650)
        if pos[1] > origin_y and pos[1] <  (origin_y + game_window.height):
            return True
    return False

def click_cell(pos):
    #adjust pos variable to match up with cells on the grid 
    # (since origin of Game_window isn't 0,0 and cells aren't 1 pixel)
    grid_pos = [pos[0]-origin_x, pos[1]-origin_y]
    grid_pos[0] = grid_pos[0]//Cell.get_size(Cell)
    grid_pos[1] = grid_pos[1]//Cell.get_size(Cell)
    #make cell alive if dead, make cell dead if alive
    game_window.grid[grid_pos[1]][grid_pos[0]].alive = not game_window.grid[grid_pos[1]][grid_pos[0]].alive
# -----------------------------------------------------------------------------

"""BUTTON FUNCTIONS"""
#making buttons
def make_buttons():
    buttons = []
    #RUN button
    buttons.append(Button(window, WIDTH//5-50, 30, 100, 30, text="RUN", 
        color = (95, 173, 86), hover_color=(118, 207, 107), function=run_game))
    #PAUSE button
    buttons.append(Button(window, WIDTH//2-50, 30, 100, 30, text="PAUSE", 
        color = (242, 193, 78), hover_color=(255, 209, 102), function=pause_game))
    #RESET button
    buttons.append(Button(window, WIDTH//1.2-50, 30, 100, 30, text="RESET", 
        color = (175, 90, 153), hover_color=(222, 126, 197), function=reset_game))
    return buttons

#give buttons functionality
def run_game():
    global state
    state = 'running'
def pause_game():
    global state
    state = 'paused'
def reset_game():
    global state
    state = 'setting'
    game_window.reset_grid()
# -----------------------------------------------------

"""
START AND RUN THE GAME
"""

#-----------SET UP--------------
pygame.init()
window = pygame.display.set_mode(size=(WIDTH, HEIGHT))
#clock runs at rate of pygame Clock
clock = pygame.time.Clock()
#variables for the position of the game window
origin_x = 80
origin_y = 80
game_window = game.Game_window(window,origin_x,origin_y) #Game_window(window, x position, y position)
buttons = make_buttons()
state = 'setting'
frame_count = 0

#----------START AND RUN-----------------
running = True
while running:
    frame_count += 1
    mouse_pos =  pygame.mouse.get_pos()
    if state == 'setting':
        get_events()
        update()
        draw()
        print('setting')
    if state == 'running':
        running_get_events()
        running_update()
        running_draw()
        print('running')
    if state == 'paused':
        paused_get_events()
        paused_update()
        paused_draw()
        print('paused')
    pygame.display.update()
    #controls frames per second
    clock.tick(FPS)

#exits game when running set to False
pygame.quit()
sys.exit()