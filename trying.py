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
bg = 'lightpink'
#declaring our main screen
main = Screen('main',screen_width,screen_height,bg,x,y)
#declaring our second screen
second = Screen('second',700,300,bg,x,y)

third = Screen('third',700,300,bg,x,y)

#making main screen our current screen
screen = main.make_current()


begin = None
end = None

edge_warnning = False

dijkstra_warning = False

warning_exists = True

run = True
while run:
	#checking for screen updates
	main.screen_update()
	second.screen_update()
	third.screen_update()




	#if the current screen is the main screen we work with the first function
	if main.check_update():
	 	draw_screen1(main.return_title())
	 	#if the button pressed is add_edgs we make the current screen the second screen 
	 	if add_edge.Action():
	 		if len(nodes)>= 2:
	 			screen = second.make_current()
	 			main.end_current()
	 		else:
	 			edge_warnning = True
	 	if len(nodes)>=2:
	 		edge_warnning = False
	 	if edge_warnning == True:
	 		warning1(main.return_title())

	 	if dijkstra.Action():
	 		if len(edge_list)>= 1:
	 			screen = third.make_current()
	 			main.end_current()
	 		else :
	 			if len(nodes)>=2:
	 				dijkstra_warning = True
	 			else:
	 				edge_warnning = True

	 	if len(edge_list)>= 1:
	 		dijkstra_warning = False
	 	if dijkstra_warning == True:
	 		warning4(main.return_title())





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
			edge_list.append(Edge(begin,end,False,edge_dis))
			for box in input_boxes:
				box.text = ""
            #and then we go back to our main screen
			screen = main.make_current()
			second.end_current()




    #if the current screen is the third screen we draw the third screen
	elif third.check_update():
		warning_exists2 = draw_screen3(third.return_title())
		if cancel_text.Action():
			screen = main.make_current()
			second.end_current()

		elif set_text.Action() and warning_exists == False:
			departure_text = input_box4.text.upper()
			end_text = input_box5.text.upper()
			for node in nodes:
				if node.text == departure_text:
					begin = node
				if node.text == end_text:
					end = node
			dijkstra_algo(begin,end,nodes,edge_list)

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
