import pygame,sys
from node import*


class Edge():
	up_position = 0
	def __init__(self,begining_node,end_node,more_than_edge,text):
		self.begining_node = begining_node
		self.end_node = end_node
		self.text = text
		self.distance = int(self.text)
		self.color = "black"
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
		text_img = self.font.render(' '+self.text, True, self.color)
		self.width = max(20, text_img.get_width()+5)
		edge_rect = Rect(self.x,self.y,self.width,20)
		#when we draw one line our adge becomes immovable,to solve this problem we draw 2 lines 
		#the first line ,the frst coordinate is the center of our begining node and the second cordinate is the center of our rect
		begining_line = pygame.draw.line(screen,self.color,(self.begining_node.x,self.begining_node.y),(edge_rect.center),2)
		#same like first line but we swith the first cordinate the center of our rect and the second is the center of our end node
		end_line = pygame.draw.line(screen,self.color,(edge_rect.center),(self.end_node.x,self.end_node.y),2)
		#in pygame we can't draw a rect that is filled and has borders at the same time so we draw 2 rects on is filled with white and the other got black borders
		pygame.draw.rect(screen, 'white', edge_rect)
		pygame.draw.rect(screen, self.color, edge_rect,1)
		screen.blit(text_img, edge_rect)

	def is_over(self,pos):
		#get edge rect
		edge_rect = Rect(self.x,self.y,20,20)
		#if mouse position collided with edge rect
		if edge_rect.collidepoint(pos):
			return True
		else:
			return False


	def move(self,pos):		
		self.x= pos[0]
		self.y= pos[1]

