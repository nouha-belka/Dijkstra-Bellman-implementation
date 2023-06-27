import pygame
from pygame.locals import *
from node import*
from main import*
from edge import*

def min_in_list(listt):
	min_node = listt[0]
	minimum = listt[0].temporary_dis
	for node in listt:
		if node.temporary_dis <= minimum:
			minimum = node.temporary_dis
			min_node = node
	return min_node

def is_in_list(listt,node_to_check):
	is_in = False
	for node in listt:
		if node == node_to_check:
			is_in = True
	return is_in

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

edgess.append(Edge(nodess[0],nodess[6],False,"51"))
edgess.append(Edge(nodess[0],nodess[1],False,"10"))
edgess.append(Edge(nodess[0],nodess[2],False,"50"))
edgess.append(Edge(nodess[1],nodess[5],False,"10"))
edgess.append(Edge(nodess[2],nodess[4],False,"50"))
edgess.append(Edge(nodess[4],nodess[7],False,"50"))
edgess.append(Edge(nodess[5],nodess[7],False,"10"))
edgess.append(Edge(nodess[6],nodess[7],False,"50"))

#initialising
infinity = 0
for edge in edgess:
	infinity = infinity + edge.distance
infinity *=2


departure_node = nodess[0]
ending_node = nodess[7]

known_nodes = [departure_node]
unknown_nodes = []

departure_node.temporary_dis = 0

for node in nodess:
	if node != departure_node:
		node.temporary_dis = infinity
		for edge in edgess:
			if edge.begining_node == departure_node and edge.end_node == node:
				node.temporary_dis = edge.distance
				node.former = departure_node
				node.former_link = edge.distance
		unknown_nodes.append(node)

#algorithme
while len(unknown_nodes)>0 and any(unknown_nodes[k].temporary_dis < infinity for k in range(len(unknown_nodes))):
	current_node = min_in_list(unknown_nodes)
	for edge in edgess:
		if edge.begining_node == current_node and is_in_list(known_nodes,edge.end_node) == False :
			next_node = edge.end_node
			if (current_node.temporary_dis + edge.distance) < next_node.temporary_dis:
				next_node.temporary_dis = current_node.temporary_dis + edge.distance
				next_node.former = current_node
				next_node.former_link = edge.distance
	known_nodes.append(current_node)
	unknown_nodes.remove(current_node)
for node in known_nodes:
	if node != None:
		print(node.text,node.temporary_dis,node.former_link)
	if node.former != None:
		node.former.text


#print(ending_node.text,ending_node.former.text,ending_node.temporary_dis,ending_node.former_link)



