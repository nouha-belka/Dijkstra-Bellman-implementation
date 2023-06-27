import pygame
from math import*
from pygame.locals import*
from edge import*
from node import*
pygame.init()

node2_x = 500
node2_y = 200
screen = pygame.display.set_mode((800,800))
node1 = Node(400,400)
node2 = Node(node2_x,node2_y)
edge = Edge(node1,node2,False,"222")

#x = radar[0] + math.cos(math.radians(300))*radar_len
#y = radar[1] + math.sin(math.radians(300))*radar_len



run = True
while run: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False	

	screen.fill('pink')
	edge.draw(screen)	
	node1.draw_node(screen)
	node2.draw_node(screen)
	pos = pygame.mouse.get_pos()
	node2.move(pos)



	edge_rect = Rect(edge.x,edge.y,edge.width,20)
	nx = edge_rect.center[0]
	ny = node2.y
	a = sqrt(pow((edge_rect.center[0]-node2.x),2)+pow((edge_rect.center[1]-node2.y),2))
	b = sqrt(pow((edge_rect.center[1]-ny),2))
	c = sqrt(pow((node2.x - nx),2))
	cos_2 = node2.radius*(c/a)
	sin_2 = node2.radius*(b/a)

	if edge_rect.center[0] < node2.x:
		if edge_rect.center[1] < node2.y :
			begx = node2.x - cos_2
			begy = node2.y - sin_2
			endx = begx - (cos_2/3)
			endy = begy - (sin_2/3)
			tuple_arrow_down = (endx - 3 * (sin_2/10), endy + 3 * (cos_2/10))
			tuple_arrow_up = (endx + 3 * (sin_2/10), endy -3 * (cos_2/10))
		if edge_rect.center[1] > node2.y:
			begx = node2.x - cos_2
			begy = node2.y + sin_2
			endx = begx - (cos_2/3)
			endy = begy + (sin_2/3)
			tuple_arrow_down = (endx + 3 * (sin_2/10), endy + 3 * (cos_2/10))
			tuple_arrow_up = (endx - 3 * (sin_2/10), endy - 3 * (cos_2/10) )
		if  edge_rect.center[1] == node2.y:
			begx = node2.x - cos_2
			begy = node2.y 
			endx = begx - (cos_2/3)
			endy = begy + (sin_2/3)
			tuple_arrow_down = (endx + 3 * (sin_2/10) , endy + 3 * (cos_2/10))
			tuple_arrow_up = (endx + 3 * (sin_2/10), endy - 3 * (cos_2/10) )



	elif edge_rect.center[0] >= node2.x:
		if edge_rect.center[1] < node2.y :
			begx = node2.x + cos_2
			begy = node2.y - sin_2
			endx = begx + (cos_2/3)
			endy = begy - (sin_2/3)
			tuple_arrow_down = (endx - 3 * (sin_2/10), endy - 3 * (cos_2/10))
			tuple_arrow_up = (endx + 3 * (sin_2/10), endy + 3 * (cos_2/10))
		if edge_rect.center[1] > node2.y:
			begx = node2.x + cos_2
			begy = node2.y + sin_2
			endx = begx + (cos_2/3)
			endy = begy + (sin_2/3)
			tuple_arrow_down = (endx + 3 * (sin_2/10), endy - 3 * (cos_2/10))
			tuple_arrow_up = (endx - 3 * (sin_2/10), endy + 3 * (cos_2/10) )
		if  edge_rect.center[1] == node2.y:
			begx = node2.x + cos_2
			begy = node2.y 
			endx = begx + (cos_2/3)
			endy = begy + (sin_2/3)
			tuple_arrow_down = (endx + 3 * (sin_2/10) , endy + 3 * (cos_2/10))
			tuple_arrow_up = (endx + 3 * (sin_2/10), endy - 3 * (cos_2/10) )





	tuple_end_arrow = (begx, begy)
	tuple_end_line_up = (endx, endy)
	tuple_end_line_down = (endx, endy)
	tuple_top_beg = edge_rect.center
	tuple_down_beg = edge_rect.center
	pygame.draw.line(screen,'black',(edge_rect.center),tuple_end_line_down,2)
	pygame.draw.polygon(screen, 'black', (tuple_top_beg,tuple_down_beg , tuple_end_line_up,tuple_arrow_down, tuple_end_arrow, tuple_arrow_up,tuple_end_line_down ))


	pygame.display.update()