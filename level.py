import enemy
from pygame import Vector2, Rect
from gameObject import GameObject, GameState

# import random
# import pygame


class Wave(GameObject):
    def __init__(self) -> None:
        super().__init__(Rect(0, 0, 0, 0))
        self.wave_height = 0
        # fill_wave(0)

    def fill_wave(self, wave_height: int) -> None:
        self.enemies: list[enemy.Enemy] = []
        self.enemies.extend(
            enemy.Octo(Vector2(i * 100, wave_height)) for i in range(10)
        )
        self.enemies.extend(
            enemy.Crab(Vector2(i * 100, wave_height + 100)) for i in range(10)
        )
        self.enemies.extend(
            enemy.Crab(Vector2(i * 100, wave_height + 150)) for i in range(10)
        )
        self.enemies.extend(
            enemy.Skull(Vector2(i * 100, wave_height + 200)) for i in range(10)
        )
        self.enemies.extend(
            enemy.Skull(Vector2(i * 100, wave_height + 250)) for i in range(10)
        )
        for e in self.enemies:
            print(e.rect.topleft)

    def update(self, game_state: GameState, delta: float) -> None:
        pass

    def move(self, delta: float) -> None:
        flip = False
        for enemy in self.enemies:
            enemy.rect.move_ip(enemy.vel * delta)
            if enemy.rect.left < 0 or enemy.rect.right > 1920:
                flip = True
        if flip:
            self.change_direction()

    def change_direction(self) -> None:
        for enemy in self.enemies:
            enemy.vel.x *= -1
            enemy.rect.move_ip(0, 5)
