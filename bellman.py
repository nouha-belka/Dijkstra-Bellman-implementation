import pygame
from pygame.locals import *
from node import*
from main import*
from edge import*

def bellman_ford_algo(departure_node,nodess,edgess):
	source_node = departure_node
	for node in nodess:
		node.temporary_dis = float('inf')
	source_node.temporary_dis = 0

	for edge in edgess:
		edge.end_node.source = False
	for node in nodess:

		print(node.text,"         ",node.source)


	for x in range(len(nodess)):
		for edge in edgess:
			if (edge.begining_node.temporary_dis + edge.distance) < edge.end_node.temporary_dis:
				edge.end_node.temporary_dis = (edge.begining_node.temporary_dis + edge.distance)
				edge.end_node.former = edge.begining_node
				edge.end_node.former_link = edge.distance

	for x in range(len(nodess)):
		for edge in edgess:
			if (edge.begining_node.temporary_dis + edge.distance) < edge.end_node.temporary_dis:
				edge.end_node.temporary_dis = float('-inf')


	edges_to_color = []
	for node in nodess:
		if node.temporary_dis == float('-inf'):
			node.color = "red"
		else:
			node.color = "blue"
			for edge in edgess:
				if edge.begining_node == node.former and edge.end_node == node and edge.distance == node.former_link:
					edge.color = "blue"
					edges_to_color.append(edge)
				if graph_is_oriented == False:
					for edge2 in edge_list:
						if edge2.end_node == node.former and edge2.begining_node == node and edge2.distance == node.former_link:
							edges_to_color.append(edge2)
							edge2.color = "blue"

	for edge in edgess:
		if is_in_list(edges_to_color,edge) == False:
			edge.color = "black"

	for node in nodess:
		if node != None:
			print(node.text,node.temporary_dis,node.former_link ,node.color)
		if node.former != None:
			node.former.text
			print(node.former.text)


edgess = []
nodess = []



nodess.append(Node(100,50))
nodess.append(Node(600,82))
nodess.append(Node(0,56))
nodess.append(Node(555,1000))
nodess.append(Node(1000,26))
nodess.append(Node(53,66))
nodess.append(Node(55,656))
nodess.append(Node(513,636))
nodess.append(Node(513,600))
nodess.append(Node(0,600))
nodess.append(Node(0,600))

edgess.append(Edge(nodess[0],nodess[1],False,"5"))
#edgess.append(Edge(nodess[1],nodess[0],False,"-5"))
edgess.append(Edge(nodess[1],nodess[2],False,"20"))
edgess.append(Edge(nodess[1],nodess[6],False,"60"))
edgess.append(Edge(nodess[1],nodess[5],False,"30"))
edgess.append(Edge(nodess[2],nodess[3],False,"10"))
edgess.append(Edge(nodess[2],nodess[4],False,"75"))
#edgess.append(Edge(nodess[3],nodess[2],False,"-15"))
edgess.append(Edge(nodess[4],nodess[9],False,"100"))
edgess.append(Edge(nodess[5],nodess[6],False,"5"))
edgess.append(Edge(nodess[5],nodess[4],False,"25"))
edgess.append(Edge(nodess[5],nodess[8],False,"50"))
edgess.append(Edge(nodess[6],nodess[7],False,"-50"))
edgess.append(Edge(nodess[7],nodess[8],False,"-10"))
edgess.append(Edge(nodess[10],nodess[8],False,"-10"))
edgess.append(Edge(nodess[4],nodess[1],False,"10"))

bellman_ford_algo(nodess[4],nodess,edgess)



#print(ending_node.text,ending_node.former.text,ending_node.temporary_dis,ending_node.former_link)


#for edge in edgess:
#	print(edge.begining_node.text,edge.distance,edge.end_node.text,edge.color)


