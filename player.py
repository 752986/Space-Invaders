import pygame
import keymap
from gameObject import GameObject
from projectile import Projectile


class Player(GameObject):
    SPEED: float = 10  # pixels per second

    def __init__(self, rect: pygame.Rect):
        self.rect = rect

    def update(self, game_objects: list[GameObject], delta: float):
        keys = pygame.key.get_pressed()
        if keys[keymap.LEFT]:
            self.rect.move_ip(-self.SPEED * delta, 0)
        if keys[keymap.RIGHT]:
            self.rect.move_ip(self.SPEED * delta, 0)

        # projectile collision
        for object in game_objects:
            if type(object) is Projectile:
                if self.rect.colliderect(object.rect):
                    if object.owner is not self:
                        game_objects.remove(object)
                        # code for damage here
