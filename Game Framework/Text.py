import pygame

class Text_Render:

    def __init__(self, font):
        self.font = font
        self.x = None
        self.y = None


    def draw_text(self,surf, str, x, y, color):
        self.x = x
        self.y = y
        text_to_render = self.font.render(str, 1, color )
        surf.blit(text_to_render, (self.x, self.y))