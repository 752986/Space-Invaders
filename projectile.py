import pygame
from gameObject import (GameObject, GameState)
from sprite import Sprite
import player
from hittable import Hittable


PLAYER_PROJECTILE = pygame.image.load("invaders_imgs/player_shot.png")
ENEMY_PROJECTILE = pygame.image.load("invaders_imgs/enemy_shot_1.png")


class Projectile(Sprite):
    def __init__(self, game_state: GameState, velocity: pygame.Vector2, owner: GameObject):
        image = PLAYER_PROJECTILE if type(owner) is player.Player else ENEMY_PROJECTILE
        super().__init__(pygame.Vector2(owner.rect.center), image, None, True)
        self.velocity = velocity
        self.owner = owner


    def update(self, game_state: GameState, delta: float):
        self.rect.move_ip(self.velocity * delta)

        # check for collision with objects that care about it
        for object in game_state.game_objects:
            if (
                object is not self
                and object is not self.owner
                and isinstance(object, Hittable)
                and self.rect.colliderect(object.rect)
            ):
                object.on_hit()
                self.should_delete = True
                break # only collide with one object

        # delete the projectile if it goes off screen
        if not (pygame.display.get_surface().get_rect().contains(self.rect)):
            self.should_delete = True

        if self.should_delete:
            if type(self.owner) is player.Player:
                self.owner.can_shoot = True