#!/usr/bin/python

class Cell:
	'Represents a maze cell in the grid'

	def __init__(self, x, y, grid):
		self.x = x
		self.y = y
		self.walls = [1,1,1,1]
		self.grid = grid

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

		return ((self.x + 1 == other.x and not self.walls[1]) or
		       (self.x - 1 == other.x and not self.walls[3]) or
		       (self.y + 1 == other.y and not self.walls[0]) or
		       (self.y - 1 == other.y and not self.walls[2]))

	def getNeighbors(self):
		
		neighbors = []
		neighbors.append(self.grid.getCell(self.x, self.y + 1)) # North
		neighbors.append(self.grid.getCell(self.x + 1, self.y)) # East
		neighbors.append(self.grid.getCell(self.x, self.y - 1)) # South
		neighbors.append(self.grid.getCell(self.x - 1, self.y)) # West
		return neighbors

class Grid:
	'A 2-d array of cells'

	def __init__(self, w, h):
		'Instantiate a grid, represented as a 2d list, of new cells of width w and height h'

		self.cells = []
		for i in range(w):
			self.cells.append([])
			for j in range(h):
				self.cells[i].append(Cell(i, j, self))

	def getCell(self, x, y):
		'Return the cell object with coordinates x, y. If none exists, return None'
		
		try:
			if x >= 0 and y >= 0:
				return self.cells[x][y]
			else:
				return None # prevent wrapping from negative indexing
		except IndexError:
			return None # if we're looking for a cell with larger indices than exist, just give None



def test():
	my_grid = Grid(10, 10)

	assert(my_grid.getCell(0, 0) is not None)
	assert(my_grid.getCell(10, 0) is None)

	assert(my_grid.getCell(0, 0).getNeighbors() == [my_grid.getCell(0, 1), my_grid.getCell(1, 0), None, None])
	assert(my_grid.getCell(9, 9).getNeighbors() == [None, None, my_grid.getCell(9, 8), my_grid.getCell(8, 9)])
	assert(my_grid.getCell(5, 5).getNeighbors() == [my_grid.getCell(5, 6), my_grid.getCell(6, 5), my_grid.getCell(5, 4), my_grid.getCell(4, 5)])

	assert(my_grid.getCell(0, 0).isConnectedTo(my_grid.getCell(1, 1)) == False)
	assert(my_grid.getCell(0, 0).isConnectedTo(my_grid.getCell(1, 0)) == False)
	my_grid.getCell(0, 0).removeWall(1) # remove east wall
	assert(my_grid.getCell(0, 0).isConnectedTo(my_grid.getCell(1, 0)) == True)
	assert(my_grid.getCell(1, 0).isConnectedTo(my_grid.getCell(0, 0)) == True)
	my_grid.getCell(0, 0).removeWallBetween(my_grid.getCell(0, 1)) # remove south wall
	assert(my_grid.getCell(0, 0).isConnectedTo(my_grid.getCell(0, 1)) == True)
	assert(my_grid.getCell(0, 1).isConnectedTo(my_grid.getCell(0, 0)) == True)

if __name__ == '__main__':
	test()
	print "Test passes"