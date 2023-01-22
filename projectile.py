import pygame
from gameObject import (GameObject, GameState)
from sprite import Sprite
import player
import event


PLAYER_PROJECTILE = pygame.image.load("invaders_imgs/player_shot.png")
ENEMY_PROJECTILE = pygame.image.load("invaders_imgs/enemy_shot_1.png")


class ProjectileDeleted(event.Event):
    def __init__(self, projectile: "Projectile"):
        self.projectile = projectile


class Projectile(Sprite):
    def __init__(self, game_state: GameState, velocity: pygame.Vector2, owner: GameObject):
        image = PLAYER_PROJECTILE if type(owner) is player.Player else ENEMY_PROJECTILE
        super().__init__(pygame.Vector2(owner.rect.center), image, None, True)
        self.velocity = velocity
        self.owner = owner
        game_state.event_handler.register_event(ProjectileDeleted)


    def update(self, game_state: GameState, delta: float):
        self.rect.move_ip(self.velocity * delta)

        # delete the projectile if it goes off screen
        if not (pygame.display.get_surface().get_rect().contains(self.rect)):
            game_state.event_handler.emit_event(ProjectileDeleted(self))
            self.should_delete = True
