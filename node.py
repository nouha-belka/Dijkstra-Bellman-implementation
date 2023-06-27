import pygame
from pygame.locals import *
import random


class Node():
	count = 0

	def __init__(self,x,y,color):
		self.x = x
		self.y = y
		self.radius = 25
		self.width = 2
		self.color = color
		self.count = Node.count
		Node.count = Node.count + 1
		self.text = "X"+str(self.count)
		self.is_clicked = False
		#draw rect around circle because in pygame rectangles have a wide range of manipulations like the colidepoint funtion that helps tell us if a rect is coliding with something
		#we can't do this with circles so it's better to draw a rect around it
		self.rect = Rect(self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)
		self.temporary_dis = 0
		self.former = None
		self.former_link = 0
		self.source = True

	def draw_node(self,screen):
		#draw circle with white background
		pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius,0)
		#draw cicle with border width 
		pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius,self.width)
		#text rendering
		font = pygame.font.SysFont('Constantia', 15)
		text_img = font.render(self.text, True, "white")
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x - int(text_len /2), self.y-8))

	def is_over(self,pos):
		#get rect around circle
		circle_rect =  Rect(self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)
		#if mouse position collided with circle rect
		if circle_rect.collidepoint(pos):
			return True
		else:
			return False

	def move(self,pos):
		#give node the mouse positions
		if pos[0] >= 250 and pos[0] <= 1290 and pos[1] >= 80 and pos[1] <= 570:
			self.x = pos[0]
			self.y = pos[1]





