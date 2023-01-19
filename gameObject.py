import pygame

class GameObject:
    def __init__(self, rect: pygame.Rect):
        self.rect: pygame.Rect = rect

    def update(self, game_objects: list["GameObject"], delta: float):
        pass

    def draw(self, surface: pygame.surface.Surface):
        pass
