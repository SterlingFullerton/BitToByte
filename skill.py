import pygame
from consts import colors

class Skill:
    def __init__(self, name, prerequisites, x, y, completed=False, icon=False, icon_size=18, icon_color=(128, 128, 128)):
        self.name = name

        # List of prerequisites skill NAMES
        self.prerequisites = prerequisites

        self.x = x
        self.y = y
        self.icon = icon
        self.icon_size = icon_size
        self.icon_color = icon_color

        self.color = colors["grey_bg"]
        self.border_color = colors["grey_text"]
        self.radius = 20

        self.completed = completed
        self.locked = True

        self.font = pygame.font.Font(None, 24)
        self.text = self.font.render(self.name, True, (255, 255, 255))

    def __str__(self):
        return f'{self.name} - {self.locked}'
    
    def __repr__(self):
        return f'{self.name} - {self.locked}'
    
    def unlock(self):
        self.locked = False
    
    def draw(self, screen):
        # Background
        self.circle = pygame.draw.circle(
            surface=screen,
            color=self.color,
            center=(self.x, self.y),
            radius=self.radius
        )

        # Border
        self.circle = pygame.draw.circle(
            surface=screen,
            color=self.border_color,
            center=(self.x, self.y),
            radius=self.radius,
            width=2
        )

        if self.icon != False:
            # Icon (if any) is a loaded pygame image
            icon_rect = self.icon.get_rect()
            icon = pygame.transform.scale(self.icon, (icon_rect.width // 2, icon_rect.height // 2))
            screen.blit(icon, (
                self.x - icon.get_width() // 2,
                self.y - icon.get_height() // 2
            ))
            
    def check_hover(self, mouse_pos):
        return self.circle.collidepoint(mouse_pos)

    def display_name(self, screen):
        screen.blit(self.text, (
            self.x - self.text.get_width() // 2,
            self.y + self.radius + 5
        ))
    
    def check_prerequisites(self, skills):
        #TODO: Check if all prerequisites are unlocked
        for skill in skills:
            #Remains true unless any prerequisite is incomplete.
            tempStatusBool = True
            for prereq_name in skill.prerequisites:
                prereq_skill = skills.get(prereq_name)
                if prereq_skill.completed == False:
                    tempStatusBool = False
            if tempStatusBool:
                skill.unlock()
        pass