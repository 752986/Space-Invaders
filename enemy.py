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

UFO_IMAGES = [
    pygame.image.load("invaders_imgs/UFO.png")
]
UFO_EXPLODE = pygame.image.load("invaders_imgs/red_expld.png")


class Enemy(AnimatedSprite, Hittable):
    death_timer: float

    def __init__(self, pos: Vector2, images: list[pygame.Surface], death: pygame.Surface):
        super().__init__(pos, images, None, True)
        self.death = death
        self.vel: Vector2 = Vector2(200, 0)
        self.points: int = 0

        self.death_timer = 0

    def update(self, game_state: GameState, delta: float):
        self.rect.move_ip(self.vel * delta)

        if self.death_timer > 0:
            self.death_timer -= delta
            if self.death_timer <= 0:
                self.should_delete = True

    def on_hit(self):
        self.image = self.death
        self.animation_speed = 0
        self.vel = Vector2(0, 0)
        self.death_timer = 1


class Octo(Enemy):
    def __init__(self, pos: Vector2):
        super().__init__(pos, OCTO_IMAGES, OCTO_EXPLODE)
        self.points = 40


class Crab(Enemy):
    def __init__(self, pos: Vector2):
        super().__init__(pos, CRAB_IMAGES, CRAB_EXPLODE)
        self.points = 20


class Skull(Enemy):
    def __init__(self, pos: Vector2):
        super().__init__(pos, SKULL_IMAGES, SKULL_EXPLODE)
        self.points = 10


class UFO(Enemy):
    def __init__(self, pos: Vector2):
        super().__init__(pos, UFO_IMAGES, UFO_EXPLODE)
        self.point_options: list[int] = [50, 250, 300]
        self.points = random.choice(self.point_options)
