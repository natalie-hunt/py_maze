#!/usr/bin/python

# Programmatic Maze Generation
# en.wikipedia.org/wiki/Maze_generation_algorithm

# Usage:
# python maze.py [WIDTH] [HEIGHT] [ALGORITHM]
# Where WIDTH and HEIGHT are the width and height of the graph used to generate the maze
# and ALGORITHM is the algorithm used to generate the maze

'''
Invictus

Out of the night that covers me,
Black as the pit from pole to pole,
I thank whatever gods may be
for my unconquerable soul.

In the fell clutch of circumstance
I have not winced nor cried aloud.
Under the bludgeonings of chance
my head is bloody but unbowed.

Beyond this place of wrath and tears
looms but the horror of the shade
And yet the menace of the years
finds, and shall find, me unafraid.

It matters not how straight the gate,
how charged with punishments the scroll;
I am the master of my fate:
I am the captain of my soul.
'''

import sys
import pygame
import random
from pygame.locals import *
from cell import *

def drawCell(cell, active=False, initialize=False):
	'Creates the pygame graphical representation of a cell and returns it as a surface with coordinates'

	# Translate coordinates: the grid represents x and y increasing in right, up directions
	# pygame represents coordinates x and y as increasing right and down, and uses top left corner
	global CELLSIZE, WIDTH, HEIGHT
	global BLACK, WHITE, DGRAY, LGRAY, RED, GREEN
	global windowSurfaceObj

	x = CELLSIZE * cell.x
	y = CELLSIZE * (HEIGHT - cell.y - 1) # invert y for pygame's coordinate system

	cellSurf = pygame.Surface((CELLSIZE, CELLSIZE))
	
	if active:
		cellSurf.fill(RED)
	elif cell.discovered:
		cellSurf.fill(WHITE)
	else:
		cellSurf.fill(DGRAY)
	
	# draw walls
	if cell.discovered:
		wallColor = BLACK
	else:
		wallColor = LGRAY

	WALLTHICKNESS = 5 # bigger number means thinner walls

	if cell.walls[0] == 1: # North Wall
		pygame.draw.rect(cellSurf, wallColor, (0, 0, CELLSIZE, CELLSIZE/WALLTHICKNESS))
	if cell.walls[1] == 1: # East Wall
		pygame.draw.rect(cellSurf, wallColor, (CELLSIZE-CELLSIZE/WALLTHICKNESS, 0, CELLSIZE/WALLTHICKNESS, CELLSIZE))
	if cell.walls[2] == 1: # South Wall
		pygame.draw.rect(cellSurf, wallColor, (0, CELLSIZE-CELLSIZE/WALLTHICKNESS, CELLSIZE, CELLSIZE/WALLTHICKNESS))
	if cell.walls[3] == 1: # West Wall
		pygame.draw.rect(cellSurf, wallColor, (0, 0, CELLSIZE/WALLTHICKNESS, CELLSIZE))

	windowSurfaceObj.blit(cellSurf, (x, y))
	pygame.display.update()
	if not initialize: # avoid slowing down the initial population of the grid
		checkQuit()
		fpsClock.tick(FPS)

def checkQuit():
	for event in pygame.event.get():
			if event.type == QUIT:			
				pygame.quit()
				sys.exit()

##################################
### Maze Generation Algorithms ###
##################################

def create_dfs(grid):
	'Creates a maze using a randomized depth-first search algorithm'

	# randomly choose a starting location on the west edge
	cell = grid.getCell(0, random.randint(0, grid.h-1))
	cell.removeWall(3) # remove the west wall
	cell.exit = True
	
	s = list()
	s.append(cell)
	s.append(cell)
	while len(s) > 0:
		cell = s.pop()
		prev = s.pop()
		drawCell(cell, True)
		drawCell(cell, False, True) # Draw twice: once to get the red cursor, next to get rid of it
		if not cell.discovered:
			cell.discovered = True
			cell.removeWallBetween(prev)
			drawCell(prev)
			drawCell(cell)
			neighbors = cell.getNeighbors()
			random.shuffle(neighbors) # choose randomly where to go next
			neighbors = [n for n in neighbors if n is not None]
			for n in neighbors:
				s.append(cell)
				s.append(n)
	
	# make the exit on the east edge
	cell = grid.getCell(grid.w-1, random.randint(0, grid.h-1))
	cell.removeWall(1) # Remove the east wall
	cell.exit = True
	drawCell(cell)
			


######################################
######### Main control code ##########
######################################

if __name__ == "__main__":

	CELLSIZE = 20 # Cells are represented as 20px by 20px
	WIDTH, HEIGHT, ALGORITHM = sys.argv[1:4] # throw away any extra arguments
	WIDTH  = int(WIDTH)
	HEIGHT = int(HEIGHT)

	if len(sys.argv) != 4:
		print "Exactly three arguments are required: grid width, grid height, and algorithm choice."
		sys.exit()

	pygame.init() # must come before any other pygame calls

	# Set up colors
	BLACK = pygame.Color(  0,   0,   0)
	WHITE = pygame.Color(255, 255, 255)
	DGRAY = pygame.Color(100, 100, 100)
	LGRAY = pygame.Color(200, 200, 200)
	RED   = pygame.Color(255,   0,   0)
	GREEN = pygame.Color(  0, 255,   0)

	grid = Grid(WIDTH, HEIGHT)

	# pygame setup 
	# ===============================
	windowSurfaceObj = pygame.display.set_mode((CELLSIZE*WIDTH, CELLSIZE*HEIGHT))
	fpsClock = pygame.time.Clock() # Limit update speed
	FPS = 30

	# Set up display
	pygame.display.set_caption('Maze Generation')

	windowSurfaceObj.fill(WHITE)
	pygame.display.update()
	fpsClock.tick(FPS)

	for row in grid.cells:
		for cell in row:
			drawCell(cell, False, True)
	pygame.display.update()

	for i in range(0, 2*FPS): # wait two seconds before starting
		fpsClock.tick(FPS)

	create_dfs(grid)

	while True:
		checkQuit()
		fpsClock.tick(FPS)