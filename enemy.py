import pygame
from pygame import Vector2 as v2
from gameObject import GameObject, GameState
from utility import is_hit
import random


class Enemy(GameObject):
    def __init__(self, pos: v2) -> None:
        self.vel: v2 = v2(5, 0)
        self.points: int = 0
        self.rect: pygame.Rect = pygame.Rect(pos, v2(100, 50))

    def update(self, game_state: GameState, delta: float) -> None:
        if is_hit(self, game_state.game_objects):
            self.should_delete = True

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)


class Octo(Enemy):
    def __init__(self, pos: v2) -> None:
        super().__init__(pos)
        self.points = 40


class Crab(Enemy):
    def __init__(self, pos: v2) -> None:
        super().__init__(pos)
        self.points = 20


class Skull(Enemy):
    def __init__(self, pos: v2) -> None:
        super().__init__(pos)
        self.points = 10


class UFO(Enemy):
    def __init__(self, pos: v2) -> None:
        super().__init__(pos)
        self.point_options: list[int] = [50, 250, 300]
        self.points = random.choice(self.point_options)
