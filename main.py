#this file contains two functions each draws element on the screen

import pygame
from pygame.locals import *
from node import*
from button import*
from edge import*
from text_zone import*
from tkinter import *
from tkinter import messagebox
from screen import*
pygame.init()
width_button = 180
height_button = 65

#declaring the buttons:
#buttons of our main screen
y_button = 60
add_node = button(20, y_button, 'Add node',20,width_button,height_button)
delete = button(20,y_button+75 , 'Delete',20,width_button,height_button)
oriented = button(20, y_button+150, 'Oriented',20,width_button,height_button)
add_edge = button(20, y_button+225, 'Add edge',20,width_button,height_button)
dijkstra = button(20, y_button+375, 'Dijkstra Algorithme',15,width_button,height_button)
new_graph = button(20, y_button+300, 'New Graph',20,width_button,height_button)
bellman_ford = button(20, y_button+450, 'Bellman_ford Algorithme',15,width_button,height_button)
return_button = button(1200,605 , "return",15,100,40,20,20,20,20)
#buttons of entry screen
entry_app = button(550, 150, 'Enter',20,width_button,height_button)
exit_app = button(550, 405, 'Exit',20,width_button,height_button)
change_theme = button(550, 235, 'Change theme',20,width_button,height_button)
button_sound = button(550, 320, 'Sound : ON',20,width_button,height_button)
#buttons of the second screen
set_text = button(400, 50, 'Okey',20,width_button,height_button)
cancel_text = button(400,170 , 'Cancel',20,width_button,height_button)

button_list = [add_node,delete,oriented,add_edge,dijkstra,new_graph,bellman_ford,set_text,cancel_text,entry_app,exit_app,button_sound,change_theme,return_button]

entry_app.button_col = 'palevioletred4'
exit_app.button_col = 'palevioletred4'
change_theme.button_col = 'palevioletred4'
button_sound.button_col = 'palevioletred4'
#declaring the input boxes for second screen
input_box1 = InputBox(190, 50, 120, 40,zone_text ="Beginning node :" ,border_width = 2)
input_box2 = InputBox(190, 130, 120, 40,zone_text ="Edge distance :" ,border_width = 2)
input_box3 = InputBox(190, 210, 120, 40,zone_text ="End node :" ,border_width = 2)
input_boxes = [input_box1, input_box2,input_box3]

#declaring input boxes for thord screen
input_box4 = InputBox(190, 70, 120, 40,zone_text ="Departure Node :" ,border_width = 2)
input_box5 = InputBox(190, 180, 120, 40,zone_text ="End node :" ,border_width = 2)
input_boxes2 = [input_box4,input_box5]

input_boxes_all = [input_box1, input_box2,input_box3,input_box4,input_box5]

input_box6 = InputBox(190, 125, 120, 40,zone_text ="End node :" ,border_width = 2)

edge_list = []

nodes = []

actual_edge_list = []

clicked_global = False
item_clicked = None

graph_is_oriented = False

global_delete = False

short_color = "darkturquoise"
color = "palevioletred4"
text_col = 'palevioletred1'
color_list=['pink4','pink3','pink2','palevioletred4','darkturquoise','mistyrose','palevioletred1',pygame.image.load('edge_app.png')]



def warning1(screen,warning,text_col,x_blit):
	font = pygame.font.SysFont('Constantia', 20)
	txt_surface = font.render(warning, True, text_col)
	screen.blit(txt_surface, (x_blit,20))

def warning2(screen,text_col):
	font = pygame.font.SysFont('Constantia', 13)
	warning = "Warning : input isn't numeric value"
	txt_surface = font.render(warning, True, text_col)
	screen.blit(txt_surface, (input_box2.x-input_box2.text_zone_width,input_box2.y+input_box2.height+5))

def warning3(screen,x,y,text_col):
	font = pygame.font.SysFont('Constantia', 13)
	warning = "Warning : invalid node name (node doesn't exist in graph)"
	txt_surface = font.render(warning, True, text_col)
	screen.blit(txt_surface, (x,y+5))




def reset_colors(nodes,edge_list):
	for node in nodes:
		node.color = color
	for edge in edge_list:
		edge.color = color
def color_management(departure_node,ending_node,nodess,graph_is_oriented):
	global short_color
	global color
    #if the user typed the name of the ending node
	if ending_node != None:
		shortest_way = [ending_node]
		#we create a loop that goes to the end node's former we insert it at the begining of the list and look for it's former and do the same thing until we arrive to the departure node
		former_node = ending_node.former
		if former_node != None:
			while(former_node != departure_node):
				shortest_way.insert(0,former_node)
				former_node = former_node.former
			shortest_way.insert(0,former_node)
	#else we show the shortest way to all nodes
	else:
		shortest_way = nodess
	edges_to_color = []
	#we color the edges and nodes that represent the shortest way in blue
	for node in shortest_way:
		if node.temporary_dis == float('-inf'):
			node.color = "brown2"
		elif node.temporary_dis == float('inf'):
			node.color = color
		else:
			node.color = short_color
			for edge in edge_list:
				if edge.begining_node == node.former and edge.end_node == node and edge.distance == node.former_link:
					edge.color = short_color
					edges_to_color.append(edge)
				if graph_is_oriented == False:
					for edge2 in edge_list:
						if edge2.end_node == node.former and edge2.begining_node == node and edge2.distance == node.former_link:
							edges_to_color.append(edge2)
							edge2.color = short_color

    #we color the rest of edges incolor(the reason we do this is because if the way changer we have to uncolor our former edge)
	for node in nodes:
		if is_in_list(shortest_way,node) == False:
			node.color = color
	for edge in edge_list:
		if is_in_list(edges_to_color,edge) == False or edge.begining_node.temporary_dis == float('inf') or edge.end_node.temporary_dis == float('inf') or (edge.end_node == departure_node and graph_is_oriented == True):
			edge.color = color

#draw the main screen
def draw_screen1(screen,notice):
	global clicked_global
	global item_clicked
	global graph_is_oriented
	global global_delete
	global color
	#draw buttons
	add_node.draw_button(screen)
	delete.draw_button(screen)
	add_edge.draw_button(screen)
	oriented.draw_button(screen)
	dijkstra.draw_button(screen)
	new_graph.draw_button(screen)
	bellman_ford.draw_button(screen)
	return_button.draw_button(screen)
	pygame.draw.rect(screen, "white", pygame.Rect(220,50,1110,550,border_radius=5),border_top_left_radius=50, border_top_right_radius=50, border_bottom_left_radius=50, border_bottom_right_radius=50)

    #add node randomly on screen
	if add_node.Action():
		notice = False
		reset_colors(nodes,edge_list)
		x_circle =  random.randint(250,1275)
		y_circle =  random.randint(95,515)
		added_node = Node(x_circle,y_circle,color)
		nodes.append(added_node)

	#oriented button
	if oriented.Action():
		notice = False
		reset_colors(nodes,edge_list)
		#if edge list has at least one element then we should delete the graph 
		if len(edge_list)>0:
			#send a message to the user to make sur he wants to delete the graph
			Tk().wm_withdraw()
			answer = messagebox.askokcancel("Warning","if you change the orientation the current graph will be deleted ")
			if answer:
				#if the answer was yes  then we change the orientation
				#if it wasn't oriented 
				if graph_is_oriented == False:
					#we make it oriented
					oriented.button_col = oriented.hover_col
					Edge.oriented = True
					graph_is_oriented = True
				#the oposite 
				elif graph_is_oriented == True:
					oriented.button_col = oriented.ac_color
					Edge.oriented = False
					graph_is_oriented = False
				nodes.clear()
				actual_edge_list.clear()
				edge_list.clear()
				Node.count = 0
		#we do the same thing but this time without deleting because we still haven't drawn the edges yet
		else:
			if graph_is_oriented == False:
				oriented.button_col = oriented.hover_col
				Edge.oriented = True
				graph_is_oriented = True
			elif graph_is_oriented == True:
				oriented.button_col = oriented.ac_color
				Edge.oriented = False
				graph_is_oriented = False
    #new graph button
	if new_graph.Action():
		#send message 
		Tk().wm_withdraw()
		answer2 = messagebox.askokcancel("Warning","the current graph will be deleted ")
		#if yes we delete the graph
		if answer2:
			nodes.clear()
			actual_edge_list.clear()
			edge_list.clear()
			Node.count = 0
			notice = False
    #delete button 
	if delete.Action():
		notice = False
		reset_colors(nodes,edge_list)
		if global_delete == False:
			delete.button_col = delete.hover_col
			global_delete = True
		elif global_delete == True:
			delete.button_col = delete.ac_color
			global_delete = False

	#get mouse position
	pos = pygame.mouse.get_pos()
	#update the edges and draw them
	for edge in edge_list:
		edge.draw(screen)

		#if the delete button is pressed and we clicke on an edge it's gonna be deleted
		if global_delete and pygame.mouse.get_pressed()[0] == 1 and edge.is_over(pos):
			Tk().wm_withdraw()
			answer3 = messagebox.askyesno("Warning","do you want to delete the edge ? ")
			if answer3:
				edge_list.remove(edge)
				for edge2 in actual_edge_list:
					if edge.begining_node == edge2.begining_node and edge.end_node == edge2.end_node and edge.distance == edge2.distance:
						actual_edge_list.remove(edge2)
						if graph_is_oriented == False:
							if edge.begining_node == edge2.end_node and edge.end_node == edge2.begining_node and edge.distance == edge2.distance:
								actual_edge_list.remove(edge2)


	#update the nodes and draw them
	for node in nodes:
		node.draw_node(screen)
        #if the delete button is pressed and we clicke on a node it's gonna be deleted and we delete the edges that has this node 
        #on either begining or end
		if global_delete and pygame.mouse.get_pressed()[0] == 1 and node.is_over(pos):
			Tk().wm_withdraw()
			answer4 = messagebox.askyesno("Warning","do you want to delete the node ? \n all the edges that have this node will be deleted")
			if answer4:
				i = 0
				while i< len(edge_list):
					if edge_list[i].begining_node == node or edge_list[i].end_node == node:
						edge_list.remove(edge_list[i])
					else:
						i = i + 1
				i = 0
				while i< len(actual_edge_list):
					if actual_edge_list[i].begining_node == node or actual_edge_list[i].end_node == node:
						actual_edge_list.remove(actual_edge_list[i])
					else:
						i = i + 1
				nodes.remove(node)
    #concatinate the two list under a general list (to not do everuthing twice one for edges and one for nodes)
	item_list = nodes + edge_list

	#if the mouse is clicked and the mouse isn't already clicked on an item 
	#(might sound absurd but the second condition means that as long as the mouse is clicked on an item we won't go through this condition)
	#if we don't do all this condition moving the items is not gonna be perfect 
	if pygame.mouse.get_pressed()[0] == 1 and clicked_global == False:
		for item in item_list:
			#if the mouse is collided with the item
			if item.is_over(pos):
				item_clicked = item
				item_clicked.is_clicked = True
				clicked_global = True
			else:
				item.is_clicked = False

    #the first condition is so when we start the app with both lists void it won't raise an exception
    #the second condition to verify if the mouse isn't unclicked
	if item_clicked != None and pygame.mouse.get_pressed()[0] != 0 and item_clicked.is_clicked:
		item_clicked.move(pos)

	if pygame.mouse.get_pressed()[0] == 0:
		clicked_global = False

	#if len(nodes)>9:
		#bellman_ford_algo(nodes[0],nodes,actual_edge_list)






	return graph_is_oriented,notice







#draw the second screen
distance_warning = False
node1_warning = False
node2_warning = False
def draw_screen2(screen):
	#declaring warning variables
	global distance_warning
	global node1_warning
	global node2_warning
	global text_col
	
	#if input box 2 (contains the distance input) isn't a numiric value, it's gonna signal warnning
	if input_box2.text.isnumeric() == False and input_box2.active == True:
		distance_warning = True
	if input_box2.text.isnumeric():
		distance_warning = False
	else:
		if len(input_box2.text)>1 and input_box2.text[0] == '-' and input_box2.text[1:].isnumeric():
			distance_warning = False
    #initializing warnning when boxes are clicked 
	if input_box1.active:
		node1_warning = True
	if input_box3.active:
		node2_warning = True
	#testing if the  input in the rest of boxes(containing node input) is equal any node text form our node list if yes there is no warning
	for node in nodes:
		if node.text == input_box1.text.upper():
			node1_warning = False
		if node.text == input_box3.text.upper():
			node2_warning = False

     #drawing the buttons and boxes
	set_text.draw_button(screen)
	cancel_text.draw_button(screen)
	for box in input_boxes:
		box.draw(screen)
	#showing warnings in screen
	if distance_warning:
		warning2(screen,text_col)
	
	if node1_warning :
		warning3(screen,input_box1.x-input_box1.text_zone_width,input_box1.y+input_box1.height,text_col)

	if node2_warning :
		warning3(screen,input_box3.x-input_box3.text_zone_width,input_box3.y+input_box3.height,text_col)
    #returning the values of the three warning (gonna be used later in trying.py when the butoon "okey" is pressed so that if there was any warning we don't validate the input)
	return(distance_warning or node2_warning or node1_warning)






#dijkstra algorithme
#simple function that returns the node with the minimum temporary distance
def min_in_list(listt):
	min_node = listt[0]
	minimum = listt[0].temporary_dis
	for node in listt:
		if node.temporary_dis <= minimum:
			minimum = node.temporary_dis
			min_node = node
	return min_node
#simple funtion that checks if an item is in list and returns it
def is_in_list(listt,node_to_check):
	is_in = False
	for item in listt:
		if item == node_to_check:
			is_in = True
	return is_in

def dijkstra_algo(departure_node,ending_node,nodess,edgess):
	global graph_is_oriented
	#initialising
	infinity = 0
	#giving infinity the sum of all the edges and then multiplying it by 2 to make sur it's bigger than all distances
	for edge in edgess:
		infinity = infinity + edge.distance
	infinity *=2
	#list of known nodes basically the nodes that we know the minimal distance of, we initialize it with the departue node because we know the minimal distance to itself is 0
	known_nodes = [departure_node]
	#list of uknown nodes basically the oposite of known nodes
	unknown_nodes = []
    #explained in known nodes comment
	departure_node.temporary_dis = 0
    #initializing the  uknown_list
	for node in nodess:
		#we don't include the departure node because it's already known
		if node != departure_node:
			#we give all the other nodes infinity as a distance
			node.temporary_dis = infinity
			#and then we test the edges if there is any node that is linked with the departure node we give as distance the distance between the 2 nodes
			#and we give these nodes the departure node as a former node or 'precedent' 
			for edge in edgess:
				if edge.begining_node == departure_node and edge.end_node == node:
					node.temporary_dis = edge.distance
					node.former = departure_node
					node.former_link = edge.distance
			unknown_nodes.append(node)

	#algorithme
	#if uknown list isn't empty or there are still nodes inside that don't have infinity as distance we execute
	# (having a list with only infinity as distance means there is no way form our departure node to our end node )
	while len(unknown_nodes)>0 and any(unknown_nodes[k].temporary_dis < infinity for k in range(len(unknown_nodes))):
		#we look for the node with the minimum distance
		current_node = min_in_list(unknown_nodes)
		#if the node with the minimum distance is our end node we get out (no need to execute the algorithme until the end, we just need the way until the end node)
		for edge in edgess:
			#if current node is the edge's begining node and the end node of our edge isn't in known list (we havn't found the way to it yet) 
			#this means the successors of current node that aren't already known
			if edge.begining_node == current_node and is_in_list(known_nodes,edge.end_node) == False :
				next_node = edge.end_node
				#if current node minimal distance + the value of our edge is smaller than the minimal distance of our edge
				if (current_node.temporary_dis + edge.distance) < next_node.temporary_dis:
					#we update the minimal distance of the edge and set its former to the current node
					next_node.temporary_dis = current_node.temporary_dis + edge.distance
					next_node.former = current_node
					#we also save the distance between the former node and this nodes(helps in the drawing in cas there were many edges between two nodes)
					next_node.former_link = edge.distance
		#we put current node in the known list and delete it from the uknown list
		known_nodes.append(current_node)
		unknown_nodes.remove(current_node)
	color_management(departure_node,ending_node,nodess,graph_is_oriented)
#	for node in known_nodes:
#		if node != None:
#			print(node.text,node.temporary_dis,node.former_link)
#		if node.former != None:
#			print(node.former.text)
#	print(ending_node.text,ending_node.former.text,ending_node.temporary_dis,ending_node.former_link)
    #creating the lis of the shortest way 
    #we start it by our end node 




node4_warning = False
node3_warning = False
#drwing the screen of djikstra algorithme input 
def draw_screen3(screen):
	global node4_warning
	global node3_warning


	#initializing warnning when boxes are clicked 
	if input_box4.active:
		node4_warning = True
	if input_box5.active:
		node3_warning = True
	#testing if the  input in the rest of boxes(containing node input) is equal any node text form our node list if yes there is no warning
	for node in nodes:
		if node.text == input_box4.text.upper():
			node4_warning = False
		if node.text == input_box5.text.upper():
			node3_warning = False
	if input_box5.text == "":
		node3_warning = False

	if node4_warning :
		warning3(screen,input_box4.x-input_box4.text_zone_width,input_box4.y+input_box4.height,text_col)
	if node3_warning :
		warning3(screen,input_box5.x-input_box5.text_zone_width,input_box5.y+input_box5.height,text_col)
	
	set_text.draw_button(screen)
	cancel_text.draw_button(screen)

	for box in input_boxes2:
		box.draw(screen)
	return(node3_warning or node4_warning)




def bellman_ford_algo(departure_node,ending_node,nodess,edgess):
	global graph_is_oriented
	source_node = departure_node
	for node in nodess:
		node.temporary_dis = float('inf')
	source_node.temporary_dis = 0


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
	color_management(departure_node,ending_node,nodess,graph_is_oriented)
bg = 'pink4'
entry_surface = pygame.image.load('edge_app.png')
entry_surface_rect = entry_surface.get_rect(center=(675,325))


def draw_screen_entry(screen):
	global color
	global short_color
	global text_col,color_list
	global entry_surface,entry_surface_rect,bg
	



	if button_sound.Action():
		if button.sound :
			button.sound = False
			button_sound.text = "Sound : OFF"
		else :
			button.sound = True
			button_sound.text = "Sound : ON"

	if change_theme.Action():
		if bg == 'pink4':
			color_list =['darkslategrey','darkslategray4','darkslategray3','darkcyan','greenyellow','aliceblue','darkslategray1',pygame.image.load('edge_app2.png')]

	
		elif bg == 'darkslategrey':
			color_list=['pink4','pink3','pink2','palevioletred4','darkturquoise','mistyrose','palevioletred1',pygame.image.load('edge_app.png')]

		bg = color_list[0]
		Screen.fill = bg
		for buttonn in button_list:
			buttonn.ac_color = color_list[1]
			buttonn.button_col = color_list[1]
			buttonn.hover_col  = color_list[2]
			color = color_list[3]
			short_color = color_list[4]
		for node in nodes : 
			node.color = color
		for edge in edge_list:
			edge.color = color
		InputBox.COLOR_INACTIVE  = color_list[1]
		InputBox.FILL_COLOR_INACTIVE = color_list[5]
		text_col = color_list[6]
		entry_surface = color_list[7]
		entry_surface_rect = entry_surface.get_rect(center=(675,325))
		entry_app.button_col = color_list[3]
		exit_app.button_col = color_list[3]
		change_theme.button_col = color_list[3]
		button_sound.button_col = color_list[3]

	



	screen.blit(entry_surface,entry_surface_rect)
	entry_app.draw_button(screen)
	exit_app.draw_button(screen)
	change_theme.draw_button(screen)
	button_sound.draw_button(screen)

	return color,text_col


