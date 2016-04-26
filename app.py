# undirected connected
# 0 1 1 0 0 0;1 0 0 0 0 1;1 0 0 1 1 0;0 0 1 0 0 0;0 0 1 0 0 0;0 1 0 0 0 0

# undirected disconnected
# 0 1 1 0 0 0;1 0 0 0 0 0;1 0 0 1 1 0;0 0 1 0 0 0;0 0 1 0 0 0;0 0 0 0 0 0

# directed connected
# 0 1 0 0 0 0;0 0 1 0 0 0;0 0 0 0 0 1;1 0 0 0 0 0;0 0 0 1 0 0;0 0 0 0 1 0

# directed disconnected
# 0 0 0 0 0 0;1 0 1 0 0 0;0 0 0 0 0 0;1 0 0 0 0 0;0 0 0 1 0 0;0 0 1 0 1 0



import numpy
import networkx
# import matplotlib.pyplot as plt
from collections import deque



def depthFirst(vertex):
	S = [] # empty stack

	for node in graph.nodes(): # set all nodes as not being visited yet
		visitedNodes[node] = False
         
	S.append(vertex)
         
	while (S):
		u = S.pop()

		if (not visitedNodes[u]):
			visitedNodes[u] = True

			for neighbor in graph.neighbors(u):
				if (not visitedNodes[neighbor]):
					S.append(neighbor)



def breadthFirst(vertex):
	q = deque([vertex]) # queue containing vertex

	for node in graph.nodes(): # set all nodes as not being visited yet
		visitedNodes[node] = False

 
	while len(q) > 0:
		node = q.pop()

		if visitedNodes[node]:
			continue

		visitedNodes[node] = True

		for neighbor in graph.neighbors(node):
			if (not visitedNodes[neighbor]):
				q.appendleft(neighbor)



isConnectedGraph = True
visitedNodes = {}



print("Enter each row of adjacency matrix using ; to denote a new row:")
userInput = input()

adjacencyMatrix = numpy.matrix(userInput)

print(adjacencyMatrix)
graph = networkx.from_numpy_matrix(adjacencyMatrix, create_using=networkx.MultiDiGraph())
graph.edges(data=True)



# CODE TO DRAW GRAPH WITH MATPLOTLIB.PYPLOT
# pos = networkx.shell_layout(graph)
# networkx.draw(graph)
# plt.show()



# depthFirst(graph.nodes()[0])

# breadthFirst(graph.nodes()[0])

for key, value in visitedNodes.items():
	if (value == False):
		isConnectedGraph = False;

print(isConnectedGraph)