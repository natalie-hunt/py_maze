#!/usr/bin/python

# Programmatic Maze Generation
# en.wikipedia.org/wiki/Maze_generation_algorithm

# Usage:
# python maze.py [WIDTH] [HEIGHT] [ALGORITHM]
# Where WIDTH and HEIGHT are the width and height of the graph used to generate the maze
# and ALGORITHM is the algorithm used to generate the maze

import sys
#import pygame
import random
from cell import *

def main():

	WIDTH, HEIGHT, ALGORITHM = sys.argv[1:4] # throw away any extra arguments
	
	grid = Grid(WIDTH, HEIGHT)

	create_dfs(grid)


def create_dfs(grid):
	'Creates a maze using a randomized depth-first search algorithm'

	# randomly choose a starting location on the west edge
	cell = grid.getCell(0, random.randint(0, grid.h-1))
	cell.removeWall(3) # remove the west wall
	cell.exit = True
	cell.discovered = True
	
	s = list()
	s.append(cell)
	while len(s) > 0:
		prev = cell
		cell = s.pop()
		if not cell.discovered:
			cell.discovered = True
			cell.removeWallBetween(prev)
			neighbors = cell.getNeighbors()
			random.shuffle(neighbors)
			neighbors = [n for n in neighbors if n is not None]
			for n in neighbors:
				s.append(n)

if __name__ == "main":
	main()