import pygame 
from button import*



#our color pallette:
#color of inacive text box's border
COLOR_INACTIVE = pygame.Color('lightpink3')
#color of acive text box's border
COLOR_ACTIVE = pygame.Color('dodgerblue2')
#color of inacive text box's border
FILL_COLOR_INACTIVE = pygame.Color('mistyrose')
#color of acive text box
FILL_COLOR_ACTIVE = pygame.Color('white')
font_size = 20





class InputBox:

    def __init__(self, x, y, width, height,zone_text='', text='',border_width = 0,text_zone_width = 170):
        #self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.fill_color = FILL_COLOR_INACTIVE
        self.text = text
        self.font = pygame.font.SysFont('Constantia', 20)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.border_width = border_width
        self.text_zone_width = text_zone_width
        self.rect_under = pygame.Rect(self.x-self.text_zone_width, self.y - self.border_width, self.width+self.text_zone_width+self.border_width , self.height + ( self.border_width*2))
        self.zone_text = zone_text


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect_under.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
            self.fill_color = FILL_COLOR_ACTIVE if self.active else FILL_COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active :
                if event.key == pygame.K_RETURN:
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:#delte by one characher everytime the backk space is pressed
                    self.text = self.text[:-1]
                if self.txt_surface.get_width()<self.width-20:
                    self.text += event.unicode#getting the chrachter pressed into the keyboard
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)
            

    def draw(self, screen):
        # Blit the text.
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.txt_zone_surface = self.font.render(self.zone_text, True, "white")
        self.text_zone_width = max(self.text_zone_width, self.txt_zone_surface.get_width()+20)
        self.rect_under = pygame.Rect(self.x-self.text_zone_width, self.y - self.border_width, self.width+self.text_zone_width+self.border_width , self.height + ( self.border_width*2))
        pygame.draw.rect(screen, self.color, self.rect_under, 0)
        pygame.draw.rect(screen, self.fill_color, self.rect, 0)
        screen.blit(self.txt_surface, (self.rect.x+(font_size/4), self.rect.y+(self.rect.height/4)))
        screen.blit(self.txt_zone_surface , (self.x-self.text_zone_width+(font_size/4), self.rect.y+(self.rect.height/4)))
        # Blit the rect.
        







	
