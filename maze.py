#!/usr/bin/python

# Programmatic Maze Generation
# en.wikipedia.org/wiki/Maze_generation_algorithm

# Usage:
# python maze.py [WIDTH] [HEIGHT] [ALGORITHM]
# Where WIDTH and HEIGHT are the width and height of the graph used to generate the maze
# and ALGORITHM is the algorithm used to generate the maze

import sys
import pygame
import random
from cell import *

def main():

	WIDTH, HEIGHT, ALGORITHM = sys.argv[1:4] # throw away any extra arguments
	
	grid = Grid(WIDTH, HEIGHT)


def create_dfs(grid):
	'Creates a maze using a randomized depth-first search algorithm'

	# randomly choose a starting location on the west edge
	cell = grid.getCell(0, random.randint(0, grid.h-1))
	cell.removeWall(3) # remove the west wall
	
	s = list()
	s.append(cell)
	while len(s) > 0:
		cell = s.pop()

