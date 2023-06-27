import pygame
from pygame.locals import *
from node import*
from button import*
from screen import*
from main import*
from text_zone import*
from edge import*
pygame.init()
x = 10
y = 40
screen_width = 1350
screen_height = 650

#declaring our main screen
main = Screen('main',screen_width,screen_height,bg,x,y)
entry = Screen('entry',screen_width,screen_height,bg,x,y)
#declaring our second screen
second = Screen('second',700,300,bg,x,y)

third = Screen('third',700,300,bg,x,y)

#making main screen our current screen
screen = entry.make_current()


begin = None
end = None

edge_warnning = False

dijkstra_warning = False

warning_exists = True

algorithm = 'n'

negative_edge = False

notice = False

run = True

while run:
	#checking for screen updates
	main.screen_update()
	second.screen_update()
	third.screen_update()
	entry.screen_update()

	if entry.check_update():
		color,text_coll = draw_screen_entry(entry.return_title())
		if exit_app.Action():
			run = False	

		if entry_app.Action():
			screen = main.make_current()
			entry.end_current()

	#if the current screen is the main screen we work with the first function
	elif main.check_update():
		graph_is_oriented,notice = draw_screen1(main.return_title(),notice)
	 	#if the button pressed is add_edgs we make the current screen the second screen 
		if add_edge.Action():
			reset_colors(nodes,edge_list)
			if len(nodes)>= 2:
				screen = second.make_current()
				main.end_current()
			else:
				edge_warnning = True
		if len(nodes)>=2:
			edge_warnning = False
		if edge_warnning == True:
			warning1(main.return_title(),"Warning : can't do anything until there are at least 2 nodes in screen",text_coll,330)

		if dijkstra.Action():
			notice = False

			if len(edge_list)>= 1:
				for edge in edge_list:
					if edge.distance < 0:
						negative_edge = True

			if negative_edge == False:
				algorithm = "dijkstra"
			if negative_edge:
				Tk().wm_withdraw()
				messagebox.showwarning("Error", "there are edges with negative value in the graph can't execute dijkstra")
				negative_edge = False
	 		#warning1(main.return_title(),"Warning : there are edges with negative value in the graph can't execute dijkstra",text_coll,330)

	 			
		if bellman_ford.Action():
			algorithm = "bellman ford"

		if algorithm == "dijkstra" or algorithm == "bellman ford" :
			reset_colors(nodes,edge_list)
			if len(edge_list)>= 1:
				screen = third.make_current()
				main.end_current()
			else :
				if len(nodes)>=2:
					dijkstra_warning = True
				else:
					edge_warnning = True
				algorithm = ""

		if len(edge_list)>= 1:
			dijkstra_warning = False
		if dijkstra_warning == True:
			warning1(main.return_title(),"Warning : there is no edge on screen to calculate any distance",text_coll,330)

		if notice :
			warning1(main.return_title(),"Notice : the red nodes are indication that the nodes are involved in an absorbant circuit therefor the shortest way is -infinity ",text_coll,240)

		if return_button.Action():
			notice = False
			screen = entry.make_current()
			main.end_current()	 		




#222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
	 #if the current screen is the second screen we draw the second screen
	elif second.check_update():
		warning_exists = draw_screen2(second.return_title())
		#if the button pressed is the cancel button we go back to the main screen without doing nothing
		if cancel_text.Action():
			screen = main.make_current()
			second.end_current()
		#if the okey button is pressed:
		elif set_text.Action() and warning_exists == False:
			#we save what was written in the texts
			node1_text = input_box1.text.upper()
			node2_text = input_box3.text.upper()
			edge_dis = input_box2.text
			#we get the node that has the sam text as our text 
			for node in nodes:
				if node.text == node1_text:
					begin = node
				if node.text == node2_text:
					end = node
			#we add an edge to our edge list with the nodes and the distance we got from the text box
			edge_list.append(Edge(begin,end,False,edge_dis,color))
			actual_edge_list.append(Edge(begin,end,False,edge_dis,color))
			if graph_is_oriented == False:
				actual_edge_list.append(Edge(end,begin,False,edge_dis,color))
			for box in input_boxes_all:
				box.text = ""
            #and then we go back to our main screen
			screen = main.make_current()
			second.end_current()



#3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    #if the current screen is the third screen we draw the third screen
	elif third.check_update():
		warning_exists2 = draw_screen3(third.return_title())
		if cancel_text.Action():
			algorithm = ""
			screen = main.make_current()
			second.end_current()

		elif set_text.Action() and warning_exists2 == False:
			departure_text = input_box4.text.upper()
			end_text = input_box5.text.upper()
			for node in nodes:
				if node.text == departure_text:
					begin = node
				if node.text == end_text:
					end = node
				if input_box5.text == "":
					end = None
			if algorithm == "dijkstra":
				dijkstra_algo(begin,end,nodes,actual_edge_list)
				algorithm = ""
			if algorithm == "bellman ford":
				bellman_ford_algo(begin,end,nodes,actual_edge_list)
				notice = True
				algorithm = ""


			#bellmandFord (begin, end, nodes, actual_edge_list)

			#and then we go back to our main screen
			screen = main.make_current()
			third.end_current()




	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False	
		for box in input_boxes:
			box.handle_event(event)
		for box in input_boxes2:
			box.handle_event(event)

	



	pygame.display.update()

pygame.quit()
