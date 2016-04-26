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



def depthFirst(vertex):
	S = [] # empty stack

	for node in graph.nodes():
		nodes[node] = False
         
	S.append(vertex)
         
	while (S):
		u = S.pop()

		if (not nodes[u]):
			nodes[u] = True

			for neighbor in graph.neighbors(u):
				if (not nodes[neighbor]):
					S.append(neighbor)



isConnectedGraph = True
nodes = {}



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



depthFirst(graph.nodes()[0])

for key, value in nodes.items():
	if (value == False):
		isConnectedGraph = False;

print(isConnectedGraph)