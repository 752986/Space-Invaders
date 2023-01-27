import pygame
from pygame import Vector2
from gameObject import GameState
from animatedsprite import AnimatedSprite
from sprite import Sprite
from hittable import Hittable
import random

CRAB_IMAGES = [
    pygame.image.load("invaders_imgs/orange_1.png"),
    pygame.image.load("invaders_imgs/orange_2.png"),
]
CRAB_EXPLODE = pygame.image.load("invaders_imgs/orange_expld.png")

OCTO_IMAGES = [
    pygame.image.load("invaders_imgs/red_1.png"),
    pygame.image.load("invaders_imgs/red_2.png"),
]
OCTO_EXPLODE = pygame.image.load("invaders_imgs/red_expld.png")

SKULL_IMAGES = [
    pygame.image.load("invaders_imgs/yellow_1.png"),
    pygame.image.load("invaders_imgs/yellow_2.png"),
]
SKULL_EXPLODE = pygame.image.load("invaders_imgs/yellow_expld.png")

UFO_IMAGES = [pygame.image.load("invaders_imgs/UFO.png")]
UFO_EXPLODE = pygame.image.load("invaders_imgs/red_expld.png")


class Enemy(AnimatedSprite, Hittable):
    death_timer: float

    def __init__(
        self,
        pos: Vector2,
        images: list[pygame.Surface],
        death: pygame.Surface,
        game_state: GameState,
    ):
        super().__init__(pos, images, None, True)
        self.death = death
        self.vel: Vector2 = Vector2(1, 0)
        self.points: int = 0
        self.game_state = game_state
        self.death_timer = 0

    def update(self, game_state: GameState, delta: float):
        pass

    def on_hit(self):
        self.should_delete = True


class Explosion(Sprite):
    def __init__(
        self,
        pos: pygame.Vector2,
        image: pygame.surface.Surface,
        image_size: pygame.Vector2 | None,
    ):
        super().__init__(pos, image, image_size, True)
        self.death_timer = 0.1

    def update(self, game_state: GameState, delta: float):
        self.death_timer -= delta
        if self.death_timer <= 0:
            self.should_delete = True


class Octo(Enemy):
    def __init__(self, pos: Vector2, game_state: GameState):
        super().__init__(pos, OCTO_IMAGES, OCTO_EXPLODE, game_state)
        self.points = 40


class Crab(Enemy):
    def __init__(self, pos: Vector2, game_state: GameState):
        super().__init__(pos, CRAB_IMAGES, CRAB_EXPLODE, game_state)
        self.points = 20


class Skull(Enemy):
    def __init__(self, pos: Vector2, game_state: GameState):
        super().__init__(pos, SKULL_IMAGES, SKULL_EXPLODE, game_state)
        self.points = 10


class UFO(Enemy):
    def __init__(self, pos: Vector2, game_state: GameState):
        super().__init__(pos, UFO_IMAGES, UFO_EXPLODE, game_state)
        self.point_options: list[int] = [50, 250, 300]
        self.points = random.choice(self.point_options)
