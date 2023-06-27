import pygame,sys
from math import*
from node import*


class Edge():
	up_position = 0
	oriented = False
	def __init__(self,begining_node,end_node,more_than_edge,text,color):
		self.begining_node = begining_node
		self.end_node = end_node
		self.text = text
		self.distance = int(self.text)
		self.color = color
		#give x and y the middle of the distance of the two nodes as a start position (it changes later when we move the edge)
		self.x = (self.begining_node.x+self.end_node.x )/2-5
		self.y = (self.begining_node.y+self.end_node.y )/2-5
		self.width = 20
		self.rect = Rect(self.x,self.y,self.width,20)
		self.font = pygame.font.SysFont('Constantia', 15)
		self.is_clicked = False
		#when  we give parameteres if there is more than one edge we add a little bit to the position to not draw over our first edge
		self.more_than_edge = more_than_edge
		if self.more_than_edge:
			Edge.up_position += 50
			self.x = (self.begining_node.x+self.end_node.x +Edge.up_position )/2-5
			self.y = (self.begining_node.y+self.end_node.y +Edge.up_position)/2-5



	def draw(self,screen):
		text_img = self.font.render(' '+self.text, True, "white")
		self.width = max(20, text_img.get_width()+5)
		edge_rect = Rect(self.x,self.y,self.width,20)
		#when we draw one line our adge becomes immovable,to solve this problem we draw 2 lines 
		#the first line ,the frst coordinate is the center of our begining node and the second cordinate is the center of our rect
		begining_line = pygame.draw.line(screen,self.color,(self.begining_node.x,self.begining_node.y),(edge_rect.center),2)
		if Edge.oriented == True:
			self.draw_arrow(screen)
		else:
			#same like first line but we swith the first cordinate the center of our rect and the second is the center of our end node
			end_line = pygame.draw.line(screen,self.color,(edge_rect.center),(self.end_node.x,self.end_node.y),2)
		#in pygame we can't draw a rect that is filled and has borders at the same time so we draw 2 rects on is filled with white and the other got black borders

		pygame.draw.rect(screen, self.color, edge_rect,border_top_left_radius=6, border_top_right_radius=6, border_bottom_left_radius=6, border_bottom_right_radius=6)
		#pygame.draw.rect(screen, self.color, edge_rect,1)
		screen.blit(text_img, edge_rect)

	def is_over(self,pos):
		#get edge rect
		edge_rect = Rect(self.x,self.y,20,20)
		#if mouse position collided with edge rect
		if edge_rect.collidepoint(pos):
			return True
		else:
			return False

	def draw_arrow(self,screen):
		edge_rect = Rect(self.x,self.y,self.width,20)
		nx = edge_rect.center[0]
		ny = self.end_node.y
		a = sqrt(pow((edge_rect.center[0]-self.end_node.x),2)+pow((edge_rect.center[1]-self.end_node.y),2))
		b = sqrt(pow((edge_rect.center[1]-ny),2))
		c = sqrt(pow((self.end_node.x - nx),2))
		cos_2 = self.end_node.radius*(c/a)
		sin_2 = self.end_node.radius*(b/a)
		if edge_rect.center[0] < self.end_node.x:
			if edge_rect.center[1] < self.end_node.y :
				begx = self.end_node.x - cos_2
				begy = self.end_node.y - sin_2
				endx = begx - (cos_2/3)
				endy = begy - (sin_2/3)
				tuple_arrow_down = (endx - 3 * (sin_2/10), endy + 3 * (cos_2/10))
				tuple_arrow_up = (endx + 3 * (sin_2/10), endy -3 * (cos_2/10))
			if edge_rect.center[1] > self.end_node.y:
				begx = self.end_node.x - cos_2
				begy = self.end_node.y + sin_2
				endx = begx - (cos_2/3)
				endy = begy + (sin_2/3)
				tuple_arrow_down = (endx + 3 * (sin_2/10), endy + 3 * (cos_2/10))
				tuple_arrow_up = (endx - 3 * (sin_2/10), endy - 3 * (cos_2/10) )
			if  edge_rect.center[1] == self.end_node.y:
				begx = self.end_node.x - cos_2
				begy = self.end_node.y 
				endx = begx - (cos_2/3)
				endy = begy + (sin_2/3)
				tuple_arrow_down = (endx + 3 * (sin_2/10) , endy + 3 * (cos_2/10))
				tuple_arrow_up = (endx + 3 * (sin_2/10), endy - 3 * (cos_2/10) )
		elif edge_rect.center[0] >= self.end_node.x:
			if edge_rect.center[1] < self.end_node.y :
				begx = self.end_node.x + cos_2
				begy = self.end_node.y - sin_2
				endx = begx + (cos_2/3)
				endy = begy - (sin_2/3)
				tuple_arrow_down = (endx - 3 * (sin_2/10), endy - 3 * (cos_2/10))
				tuple_arrow_up = (endx + 3 * (sin_2/10), endy + 3 * (cos_2/10))
			if edge_rect.center[1] > self.end_node.y:
				begx = self.end_node.x + cos_2
				begy = self.end_node.y + sin_2
				endx = begx + (cos_2/3)
				endy = begy + (sin_2/3)
				tuple_arrow_down = (endx + 3 * (sin_2/10), endy - 3 * (cos_2/10))
				tuple_arrow_up = (endx - 3 * (sin_2/10), endy + 3 * (cos_2/10) )
			if  edge_rect.center[1] == self.end_node.y:
				begx = self.end_node.x + cos_2
				begy = self.end_node.y 
				endx = begx + (cos_2/3)
				endy = begy + (sin_2/3)
				tuple_arrow_up = (endx + 3 * (sin_2/10), endy - 3 * (cos_2/10) )
				tuple_arrow_down = (endx + 3 * (sin_2/10) , endy + 3 * (cos_2/10))
		tuple_end_arrow = (begx, begy)
		tuple_end_line_up = (endx, endy)
		tuple_end_line_down = (endx, endy)
		tuple_top_beg = edge_rect.center
		tuple_down_beg = edge_rect.center
		pygame.draw.line(screen,self.color,(edge_rect.center),tuple_end_line_down,2)
		pygame.draw.polygon(screen, self.color, (tuple_top_beg,tuple_down_beg , tuple_end_line_up,tuple_arrow_down, tuple_end_arrow, tuple_arrow_up,tuple_end_line_down ))



	def move(self,pos):
	    if pos[0] >= 225 and pos[0] <= 1295 and pos[1] >= 60 and pos[1] <= 575:	
	    	self.x= pos[0]
	    	self.y= pos[1]

