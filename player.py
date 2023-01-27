import pygame
import keymap
from gameObject import GameState
from sprite import Sprite
import projectile
from hittable import Hittable

SPEED: float = 500  # pixels per second; if this is too low then it won't move at all


class Player(Sprite, Hittable):
    can_shoot: bool

    def __init__(self, game_state: GameState, pos: pygame.Vector2):
        super().__init__(pos, pygame.image.load("invaders_imgs/player.png"), None, True)
        self.can_shoot = True
        self.score = 0

    def update(self, game_state: GameState, delta: float):
        keys = pygame.key.get_pressed()
        if keys[keymap.LEFT[0]] or keys[keymap.LEFT[1]]:
            self.rect.move_ip(-SPEED * delta, 0)
        if keys[keymap.RIGHT[0]] or keys[keymap.RIGHT[1]]:
            self.rect.move_ip(SPEED * delta, 0)

        if keys[keymap.FIRE] and self.can_shoot:
            game_state.game_objects.append(
                projectile.Projectile(game_state, pygame.Vector2(0, -1000), self)
            )
            self.can_shoot = False

    def draw(self, surface: pygame.surface.Surface):
        surface.blit(self.image, self.rect)
