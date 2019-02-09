from DecisionFactory import DecisionFactory  
import pygame, sys
from pygame.locals import *


black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
grey = (50, 50, 50)

colours = {
            0 : white,
            1 : grey,
            2 : green,
            3 : blue,
            4 : red
            }

Grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 2, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 3, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


TILESIZE = 50
MAPWIDTH = 10
MAPHEIGHT = 10

#current position of player [row, col]
POSITION = [3,3]

#PLAYER HAS FOUND GOAL
FINISHED = False

#gets decision & checks if valid
def validate_move(DF):
    global FINISHED
    global POSITION
    global Grid
    choice = DF.get_decision()
    if choice == 'up':
        check_pos = [POSITION[0],POSITION[1]+1]
    if choice == 'down':
        check_pos = [POSITION[0],POSITION[1]-1]
    if choice == 'left':
        check_pos = [POSITION[0]-1,POSITION[1]]
    if choice == 'right':
        check_pos = [POSITION[0]+1,POSITION[1]+1]
    if choice == 'wait':
        check_pos = [POSITION[0],POSITION[1]]
    tile = Grid[check_pos[0]][check_pos[1]]
    if tile == 3:
        FINISHED = True
        return 'success'
    if tile == 0:
        Grid[POSITION[0]][POSITION[1]] = 0
        POSITION[0] = check_pos[0]
        POSITION[1] = check_pos[1]
        Grid[POSITION[0]][POSITION[1]] = 2
        return 'success'
    else: 
        return 'fail'
    
def main():
	 # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
    pygame.display.set_caption('490 AI')

    #instantiate DF
    DF = DecisionFactory()

    # Event loop
    while not FINISHED:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
 
	
    	for row in range(10):
			for col in range(10):
				pygame.draw.rect(screen, colours[Grid[row][col]], [col*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE])
         
        
    	
        DF.put_result(validate_move(DF))   
        pygame.display.update()

if __name__ == '__main__': main()