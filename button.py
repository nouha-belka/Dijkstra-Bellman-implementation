import pygame
from pygame.locals import *

clicked = False
class button():	
	#colours for  text
	text_col = 'white'
	sound = True
	

	def __init__(self, x, y, text,text_size,width,height,top_left = 20,top_right = 0,bottom_left = 0,bottom_right = 20):
		self.x = x
		self.y = y
		self.text = text
		self.text_size = text_size
		self.ac_color = 'pink3'
		self.hover_col = 'pink2'
		self.button_col = 'pink3'
		self.width = width
		self.height = height
		self.top_left = top_left
		self.top_right = top_right
		self.bottom_left = bottom_left
		self.bottom_right = bottom_right

	def draw_button(self,screen):

		global clicked 


		#get mouse position
		pos = pygame.mouse.get_pos()

		#create pygame Rect object for the button
		button_rect = Rect(self.x, self.y, self.width, self.height)
		
		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				#drawing rect (the border_redius parameteres to draw a rect with rounded corners)
				#here we are drawing the rect with the normal color
				pygame.draw.rect(screen, self.button_col, button_rect,border_top_left_radius=self.top_left , border_top_right_radius=self.top_right, border_bottom_left_radius=self.bottom_left, border_bottom_right_radius=self.bottom_right)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == False:
				#here we draw it with hte hover color
				pygame.draw.rect(screen, self.hover_col, button_rect,border_top_left_radius=self.top_left , border_top_right_radius=self.top_right, border_bottom_left_radius=self.bottom_left, border_bottom_right_radius=self.bottom_right)
		else:
			#here again the normal color 
			pygame.draw.rect(screen, self.button_col, button_rect,border_top_left_radius=self.top_left , border_top_right_radius=self.top_right, border_bottom_left_radius=self.bottom_left, border_bottom_right_radius=self.bottom_right)
		#why do we draw three diffrent rects: this last condition draws the rect when no event is happening,the one above it we check if the mouse is collieded with button
		#if yes we draw the rect in a lighter color and the firs condition checks if the mouse is both colided and clicked in this case 
		#we draw the rect in its original color to give the effect that it's clicked


		#add shading to button
		#pygame.draw.line(screen, 'white', (self.x, self.y), (self.x + self.width, self.y), 2)
		#pygame.draw.line(screen, 'white', (self.x, self.y), (self.x, self.y + self.height), 2)
		#pygame.draw.line(screen, 'black', (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
		#pygame.draw.line(screen, 'black', (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

		#add text to button
		font = pygame.font.SysFont('Constantia', self.text_size)
		text_img = font.render(self.text, True, self.text_col)
		text_len = text_img.get_width()
		#these parameters help place the text in the middle of the button
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), (self.y + self.height/3)))

	def Action(self):#this funtion helps us know if the button is clicked or not
		global clicked
		action = False
		button_rect = Rect(self.x, self.y, self.width, self.height)
		pos = pygame.mouse.get_pos()
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
				if button.sound:
					score_sound = pygame.mixer.Sound('button-29.wav')
					score_sound.play()
		return action