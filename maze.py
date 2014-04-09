#!/usr/bin/python

# Programmatic Maze Generation
# en.wikipedia.org/wiki/Maze_generation_algorithm

# Usage:
# python maze.py [WIDTH] [HEIGHT] [ALGORITHM]
# Where WIDTH and HEIGHT are the width and height of the graph used to generate the maze
# and ALGORITHM is the algorithm used to generate the maze

import sys
import pygame
import cell

WIDTH, HEIGHT, ALGORITHM = sys.argv[1:4] # throw away any extra arguments

def getCell(x, y):
	'Return the cell object with coordinates x, y. If none exists, return None'
	
	try:
		if x >= 0 and y >= 0:
			return cells[x][y]
		else:
			return None # prevent wrapping from negative indexing
	except IndexError:
		return None # if we're looking for a cell with larger indices than exist, just give None

def makeGraph(w, h):
	'Instantiate a grid, represented as a 2d list, of new cells of width w and height h'

	cells = [][]
	for i in range(w):
		for j in range(h):
			cells[i][j] = Cell(i, j)
	return cells