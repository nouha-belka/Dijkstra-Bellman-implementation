import pygame
import os


class Screen():
	def __init__(self,title,width,height,fill,x,y):
		self.title = title
		self.width = width
		self.height = height
		Screen.fill = fill
		self.current = False
		self.x = x
		self.y = y
		self.position = self.x, self.y
	def make_current(self):
		pygame.display.set_caption(self.title)
		self.current = True
		self.screen = pygame.display.set_mode((self.width,self.height))

	def end_current(self):
		self.current = False

	def check_update(self):
		return self.current

	def screen_update(self):
		if(self.current):
			self.screen.fill(self.fill)

	def return_title(self):
		return self.screen

