#!/usr/bin/python

class Cell:
	'Represents a maze cell in the grid'

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.walls = [1,1,1,1]

	def removeWall(self, loc):
		'removes the north, east, south, or west cell wall with loc=0, 1, 2, or 3, respectively'
		
		self.walls[loc] = 0
		# also remove the wall from the neighbor cell
		self.getNeighbors()[loc].walls[(loc + 2) % 4] = 0

	def removeWallBetween(self, other):
		'removes the wall between the calling cell and other'

		if self.y + 1 == other.y: # N to S
			self.walls[0]  = 0
			other.walls[2] = 0
		if self.x + 1 == other.x: # E to W
			self.walls[1]  = 0
			other.walls[3] = 0
		if self.y - 1 == other.y: # S to N
			self.walls[2]  = 0
			other.walls[0] = 0
		if self.x - 1 == other.x: # W to E
			self.walls[3]  = 0
			other.walls[1] = 0

	def isConnectedTo(self, other):
		'Returns true iff self and other are neighbors and there is not a wall between them'

		return (self.x + 1 == other.x and not self.walls[1]) or
		       (self.x - 1 == other.x and not self.walls[3]) or
		       (self.y + 1 == other.y and not self.walls[0]) or
		       (self.y - 1 == other.y and not self.walls[2])

	def getNeighbors(self):
		
		neighbors = []
		neighbors.append(Cell.getCell(self.x, self.y + 1)) # North
		neighbors.append(Cell.getCell(self.x + 1, self.y)) # East
		neighbors.append(Cell.getCell(self.x, self.y - 1)) # South
		neighbors.append(Cell.getCell(self.x - 1, self.y)) # West
		return neighbors


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