import numpy
import networkx
import matplotlib.pyplot as plt
from collections import deque



def breadthFirst(vertex):
	q = deque([vertex])

	for node in graph.nodes():
		visitedNodes[node] = False # o(n)
 
	while len(q) > 0: # o(n)
		node = q.pop()

		if visitedNodes[node]:
			continue

		visitedNodes[node] = True

		for neighbor in graph.neighbors(node):
			if (not visitedNodes[neighbor]):
				q.appendleft(neighbor) # o(n^2-n)



def depthFirst(vertex):
	S = []

	for node in graph.nodes():
		visitedNodes[node] = False # o(n)

	S.append(vertex)
         
	while (S): # o(n)
		u = S.pop()

		if (not visitedNodes[u]):
			visitedNodes[u] = True

			for neighbor in graph.neighbors(u):
				if (not visitedNodes[neighbor]):
					S.append(neighbor) # o(n^2-n)



isConnectedGraph = True
visitedNodes = {}



print("Enter each row of adjacency matrix using ; to denote a new row:")
userInput = input()

adjacencyMatrix = numpy.matrix(userInput)

print(adjacencyMatrix)
graph = networkx.from_numpy_matrix(adjacencyMatrix, create_using=networkx.MultiDiGraph())
graph.edges(data=True)



# CODE TO DRAW GRAPH WITH MATPLOTLIB.PYPLOT
pos = networkx.shell_layout(graph)
networkx.draw(graph)
plt.show()



# depthFirst(graph.nodes()[0])

breadthFirst(graph.nodes()[0])

for key, value in visitedNodes.items():
	if (value == False):
		isConnectedGraph = False;

print(isConnectedGraph)