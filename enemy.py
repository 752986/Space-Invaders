import pygame
from pygame import Vector2
from gameObject import GameState
from animatedsprite import AnimatedSprite
from hittable import Hittable
import random

CRAB_IMAGES = [
    pygame.image.load("invaders_imgs/orange_1.png"),
    pygame.image.load("invaders_imgs/orange_2.png"),
]

OCTO_IMAGES = [
    pygame.image.load("invaders_imgs/red_1.png"),
    pygame.image.load("invaders_imgs/red_2.png"),
]

SKULL_IMAGES = [
    pygame.image.load("invaders_imgs/yellow_1.png"),
    pygame.image.load("invaders_imgs/yellow_2.png"),
]

UFO_IMAGES = [pygame.image.load("invaders_imgs/UFO.png")]


class Enemy(AnimatedSprite, Hittable):
    def __init__(self, pos: Vector2, images: list[pygame.Surface]):
        super().__init__(pos, images, None, True)
        self.vel: Vector2 = Vector2(150, 0)
        self.points: int = 0

    def update(self, game_state: GameState, delta: float):
        pass

    def on_hit(self):
        self.should_delete = True


class Octo(Enemy):
    def __init__(self, pos: Vector2):
        super().__init__(pos, OCTO_IMAGES)
        self.points = 40


class Crab(Enemy):
    def __init__(self, pos: Vector2):
        super().__init__(pos, CRAB_IMAGES)
        self.points = 20


class Skull(Enemy):
    def __init__(self, pos: Vector2):
        super().__init__(pos, SKULL_IMAGES)
        self.points = 10


class UFO(Enemy):
    def __init__(self, pos: Vector2):
        super().__init__(pos, UFO_IMAGES)
        self.point_options: list[int] = [50, 250, 300]
        self.points = random.choice(self.point_options)
