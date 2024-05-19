import pygame
from consts import colors

class Button:
    def __init__(self, x, y, text, text_size, \
            width=None, height=None,
            bg_color=colors["grey_bg"], text_color=colors["grey_text"], \
            rounded=False, radius=10, border=False, border_color=colors["grey_text"], \
            border_width=1, padding=30, immutable_size=False, icon=False, index=0):
        
        self.font = pygame.font.Font(None, text_size)
        self.text = self.font.render(text, True, text_color)
        self.icon = False
        self.index = index

        self.immutable_size = immutable_size

        self.x = x - (self.text.get_width() + padding) // 2
        self.y = y - (self.text.get_height() + padding) // 2
        self.width = width if width else self.text.get_width() + padding
        self.height = height if height else self.text.get_height() + padding
        self.str_text = text
        self.bg_color = bg_color
        self.text_size = text_size
        self.text_color = text_color
        self.rounded = rounded
        self.radius = radius
        self.border = border
        self.border_color = border_color
        self.border_width = border_width
        self.padding = padding

        self.attached_to_mouse = False

    def setup(self):
        self.font = pygame.font.Font(None, self.text_size)
        self.text = self.font.render(self.str_text, True, self.text_color)

        if self.immutable_size:
            self.width = self.width
            self.height = self.height
        else:
            self.width = self.text.get_width() + self.padding
            self.height = self.text.get_height() + self.padding

        self.x = self.x - self.width // 2
        self.y = self.y - self.height // 2

    def setNewText(self, text):
        self.str_text = text
        self.setup()

    def setNewPos(self, x, y):
        self.x = x
        self.y = y
        self.setup()
    
    def setSize(self, width, height):
        self.width = width
        self.height = height
        self.setup()

    def draw(self, screen):
        if self.attached_to_mouse:
            mouse = pygame.mouse.get_pos()
            self.x = mouse[0] - self.width // 2
            self.y = mouse[1] - self.height // 2

        if self.icon != False:
            # Icon (if any) is a loaded pygame image
            icon_rect = self.icon.get_rect()
            icon = pygame.transform.scale(self.icon, (icon_rect.width // 2, icon_rect.height // 2))
        

        # Rectangle
        self.rectangle = pygame.draw.rect(
            surface=screen,
            color=self.bg_color,
            rect=(self.x, self.y, self.width, self.height),
            border_radius=self.radius
        )

        # Border
        self.rectangle = pygame.draw.rect(
            surface=screen,
            color=self.border_color,
            rect=(self.x, self.y, self.width, self.height),
            width=self.border_width,
            border_radius=self.radius
        )

        
        #icon
        if self.icon != False:
            screen.blit(self.icon, (
                self.x - self.icon.get_width() // 2,
                self.y - self.icon.get_height() // 2
                ))

        # Text
        screen.blit(self.text, (
            self.x + self.width // 2 - self.text.get_width() // 2,
            self.y + self.height // 2 - self.text.get_height() // 2
        ))

    def attach(self):
        self.attached_to_mouse = True

    def detach(self):
        self.attached_to_mouse = False
    
    def attached(self):
        return self.attached_to_mouse