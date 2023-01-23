import pygame
import keymap
from gameObject import GameState
from sprite import Sprite
import projectile
import utility
from event import Event


SPEED: float = 500  # pixels per second; if this is too low then it won't move at all


class Player(Sprite):
    can_shoot: bool

    def on_projectile_deleted(self, event: Event):
        assert (
            type(event) is projectile.ProjectileDeleted
        )  # this is needed to appease the type checker
        if event.projectile.owner is self:
            self.can_shoot = True

    def __init__(self, game_state: GameState, pos: pygame.Vector2):
        super().__init__(pos, pygame.image.load("invaders_imgs/player.png"), None, True)
        self.can_shoot = True
        game_state.event_handler.subscribe(
            self, projectile.ProjectileDeleted, self.on_projectile_deleted
        )

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

        # projectile collision
        if utility.is_hit(self, game_state.game_objects):
            pass  # code for damage here
