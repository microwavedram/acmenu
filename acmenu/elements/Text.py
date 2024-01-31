import pygame

from elements.Instance import *

class Text(Instance):
    def __init__(self, pos, text="", font=None, fontSize=25, color=(255, 255, 255)):
        super(Text, self).__init__(pos)

        self.font = pygame.font.Font(font, fontSize)
        self.color = color
        self.content = text

        self._last_content = ""

    def __repr__(self):
        return f"Text({self.id} text={self.content})"
    
    def render(self, screen):
        print("his")
        if self.content != self._last_content:
            self.rendered = self.font.render(self.content, True, self.color)

        print(self.rendered, self.pos.tuple())

        screen.blit(self.rendered, self.pos.tuple())
