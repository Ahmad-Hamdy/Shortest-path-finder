from queue import PriorityQueue
from math import sqrt

class node:
	"""A class to represent a cell on the grid"""
	def __init__(self, x, y, parent = None):
		self.__X = x
		self.__Y = y
		self.parent = parent
		self.__F_distance = 0
		self._status = "blank"

	""" Dunder methods defining th comparison operators """
	def __lt__(self, Node):
		return self.F_distance < Node.F_distance
	def __le__(self, Node):
		return self.F_distance <= Node.F_distance
	def __gt__(self, Node):
		return self.F_distance > Node.F_distance
	def __ge__(self, Node):
		return self.F_distance >= Node.F_distance

	def __eq__(self, Node):
		return self.x == Node.x and self.y == Node.y

	""" Representative function to print(x,y) coordinates of a node when print() is used """
	def __repr__(self):
		return f"({self.x}, {self.y})"


	"""
	Getter methods for X and Y with no setters

	As the x,y coordinates of a point
	Should never change on runtime

	"""
	@property
	def x(self):
		return self.__X
	@property
	def y(self):
		return self.__Y

	@property
	def F_distance(self):
		return self.__F_distance

	@F_distance.setter
	def F_distance(self, distance):
		if type(distance) is int and distance > 0:
			self.__F_distance = distance

	@property
	def status(self):
		return self._status

	@status.setter
	def status(self, string):
		if string.lower() in ["blank", "barrier", "open", "closed"]:
			self._status = string.lower()
		else:
			raise ValueError("Invalid status value")

	""" 
	A functiom to calculate the g_cost of a node

	By tracing the distance between the node 
	And it's ancestors back to the starting node.
	"""
	def G_distance(self):
		if not self.parent:
			return 0

		if self.x == self.parent.x or self.y == self.parent.y:
			return 10 + self.parent.G_distance()
		else:
			return 14 + self.parent.G_distance()

	""" 
	A functiom to calculate the h_cost of a node

	Using euclidean distance heuristic in which
	the absolute distance between the current node 
	And the target node is calculated using 
	straight line equation.
	"""
	def H_distance(self, destination):
		return int(sqrt(
			pow((destination.x - self.x), 2)
			+ pow((destination.y - self.y), 2)
			) * 10)


""" 
	The main function resposible for finding the shortest path
	between two points using A* algorithm
"""
def find_shortest_path(grid, start_coordinates, target_coordinates):
	Open = PriorityQueue()
	shortest_path = list()

	# forming a matrix of nodes using the grid recieved
	nodes = [ [node(row, column) for column in range(len(grid[0]))] for row in range(len(grid))]

	# defining the start node
	x,y = start_coordinates
	start = nodes[x][y]

	# defining the target node
	x,y = target_coordinates
	target = nodes[x][y]

	# marking the nodes with value 0 in the grid as barriers
	for row in range(len(grid)):
		for column in range(len(grid[0])):
			if not grid[row][column]:
				nodes[row][column].status = "barrier"

	# Adding the stat node to the open list to start the main loop
	Open.put(start)

	# main loop that checks all the nodes in the empty list to form the path
	while not Open.empty():

		# marking the checked nodes as closed (to avoid re-checking them)
		current = Open.get()
		current.status = "closed"

		# when reaching the target node Quit the loop
		if current == target:
			break

		# looping over all the neigbours of the currently checked node
		for row in range(current.x - 1, current.x + 2):
			for column in range(current.y - 1, current.y + 2):

				if 0 <= row < len(grid) and 0 <= column < len(grid[0]):
					successor = nodes[row][column]

					# skip the neighbour if it's already checked
					# or if it's not traversable (barrier)
					if (successor.status == "closed" or 
						successor.status == "barrier"):
						continue

					else:
						# get the cost of the path leading to that neighbour
						path = current.G_distance() + 10 if (
							successor.x == current.x or successor.y == current.y
							) else  14

						# update the neighbour if it's never updated(blank)
						# or the current path leading to it 
						# is less than the path from it's parent 
						if successor.status != "open" or successor.G_distance() > path:
							successor.parent = current
							successor.F_distance = successor.G_distance() + successor.H_distance(target)

							# add the neighbour to open list if it's not already there
							if successor.status != "open":
								Open.put(successor)
								successor.status = "open"
				
				# skip everything if the coordinates lies outside the grid
				# applies for nodes at the edges of the grid
				else:
					continue

	else:
		print("Target not found")

	# when the target is found 
	# trace the path leading to it 
	# and return a list of path nodes 
	while current:
		shortest_path.append(current)
		current = current.parent

	return shortest_path[::-1]



#grid = [ [ 1 for j in range(5)] for i in range(5)]

grid = [ [1, 1, 1, 1, 1, 1, 1, 1, 1], 
         [0, 1, 0, 0, 0, 0, 0, 0, 1], 
         [0, 0, 1, 0, 0, 0, 0, 0, 1], 
         [0, 0, 0, 1, 1, 1, 0, 0, 1], 
         [0, 0, 0, 1, 1, 1, 1, 0, 1], 
         [0, 0, 0, 0, 0, 0, 1, 0, 1], 
         [0, 0, 0, 0, 0, 0, 0, 0, 1], 
         [0, 0, 0, 0, 0, 0, 0, 1, 1], 
         [0, 0, 0, 0, 0, 0, 0, 1, 1] ]

path = find_shortest_path(grid, (0,0), (8,8))

display = [ str(Node) for Node in path]
print(" -> ".join(display))
