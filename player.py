import pygame
import keymap
from gameObject import GameObject
from utility import is_hit


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
        if is_hit(self, game_objects):
            pass # code for damage here
