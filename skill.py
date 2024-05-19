import pygame
from consts import colors

class Skill:
    def __init__(self, name, prerequisites, x, y, completed=False, icon=False, icon_size=18, icon_color=colors["grey_text"], locked=True):
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
        self.radius = 30

        self.completed = completed
        self.locked = locked

        self.font = pygame.font.Font(None, 24)
        self.text = self.font.render(self.name, True, (255, 255, 255))

    def __str__(self):
        return f'{self.name} - {self.locked}'
    
    def __repr__(self):
        return f'{self.name} - {self.locked}'
    
    def unlock(self):
        self.locked = False
    
    def complete(self):
        self.completed = True
        self.border_color = colors["neon_green"]
    
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
        # Check if all prerequisites are completed to unlock this skill
        for skill_name in skills:
            prerequisite_completed = True
            for prerequisite in self.prerequisites:
                if not skills[prerequisite].completed:
                    prerequisite_completed = False
                    break
            if prerequisite_completed:
                self.locked = False
                return False
        return True