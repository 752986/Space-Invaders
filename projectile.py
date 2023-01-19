import pygame
from gameObject import GameObject

class Projectile(GameObject): 
    def __init__(self, rect: pygame.Rect, velocity: pygame.Vector2, owner: GameObject):
        self.rect = rect
        self.velocity = velocity
        self.owner = owner
        
    def update(self, game_objects: list[GameObject], delta: float):
        self.rect.move_ip(self.velocity * delta)

    def draw(self, surface: pygame.surface.Surface):
        pass