import pygame
vec = pygame.math.Vector2

class Button:
    def __init__(self, surface, x, y, width, height, state='', id='', function=0, color =(255,255,255), hover_color=(240,240,240), border=True, border_width=2, border_color = (255,255,255), text='BUTTON',font_name = "Arial",text_size=15,text_color=(0,0,0)):
        self.type = 'button'
        self.x = x
        self.y = y
        self.pos = vec(x,y)
        self.width = width
        self.height = height
        self.surface = surface
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.state = state
        self.id = id
        self.function = function
        self.color = color
        self.hover_color = hover_color
        self.border = border
        self.border_color = border_color
        self.border_width = 1
        self.text = text
        self.font_name = font_name
        self.text_size = text_size
        self.text_color = text_color
        self.hovered = False
    def update(self,pos):
        if self.mouse_hovering(pos):
            self.hovered = True
        else:
            self.hovered = False

    def draw(self):
        if self.border:
            self.image.fill(self.border_color)
            if self.hovered:
                pygame.draw.rect(self.image, self.hover_color, (self.border_width, self.border_width,
                                                                self.width-(self.border_width*2), self.height-(self.border_width*2)))
            else:
                pygame.draw.rect(self.image, self.color, (self.border_width, self.border_width,
                                                                self.width-(self.border_width*2), self.height-(self.border_width*2)))
        else:
            self.image.fill(self.color)
        if len(self.text) > 0:
            self.show_text()
        self.surface.blit(self.image, self.pos)

    def click(self):
        if self.function != 0 and self.hovered:
            self.function()

    def show_text(self):
        font = pygame.font.SysFont(self.font_name, self.text_size)
        text = font.render(self.text, False, self.text_color)
        size = text.get_size()
        x,y = self.width//2-(size[0]//2), self.height//2-(size[1]//2)
        pos = vec(x,y)
        self.image.blit(text, pos)

    def mouse_hovering(self, pos):
        if pos[0] > self.pos[0] and pos[0] < self.pos[0]+self.width:
            if pos[1] > self.pos[1] and pos[1] < self.pos[1]+self.height:
                return True
        else:
            return False

