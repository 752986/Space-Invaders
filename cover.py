import pygame
from pygame.math import Vector2
from gameObject import (GameObject, GameState)
from sprite import Sprite
from utility import is_hit
from random import random


# the 4 stages of damage for a tile of cover
COVER_IMAGES = [
    pygame.image.load("invaders_imgs/barrier_0.png"),
    pygame.image.load("invaders_imgs/barrier_1.png"),
    pygame.image.load("invaders_imgs/barrier_2.png"),
    pygame.image.load("invaders_imgs/barrier_3.png"),
]

# the layout of each barrier
BARRIER_SHAPE = [
    [True, True, True, True],
    [True, True, True, True],
    [True, True, True, True],
    [True, False, False, True],
]

# an individual tile of a barrier
class CoverTile(Sprite):
    health: int

    def __init__(self, pos: Vector2, size: Vector2 | None):
        super().__init__(pos, COVER_IMAGES[0], size)
        self.health = 4

    def update(self, game_state: GameState, delta: float):
        # if a projectile is colliding with the tile, take damage
        if is_hit(self, game_state.game_objects):
            self.health -= 1

            # if the tile is dead, remove it; otherwise, progress its stage of damage
            if self.health <= 0:
                self.should_delete = True
            else:
                self.replace_image(
                    # randomly flip the image so it doesn't look too repetitive
                    pygame.transform.flip(COVER_IMAGES[4 - self.health], random() > 0.5, random() > 0.5), 
                    Vector2(self.rect.size)
                )


# create the CoverTiles that form a single barrier 
def generate_barrier(tile_size: float, position: Vector2) -> list[CoverTile]:
    tiles: list[CoverTile] = []

    for (y, row) in enumerate(BARRIER_SHAPE):
        for (x, val) in enumerate(row):
            if val:
                tiles.append(CoverTile(position + Vector2(x * tile_size, y * tile_size), Vector2(tile_size)))

    return tiles


# generate and fill in all of the needed barriers
def generate_cover(screen_width: float, n_barriers: int, height: float, tile_size: float | None) -> list[GameObject]:
    '''Generates a set of barriers spaced on the screen. `height` is the y-coordinate of the bottom row of tiles.'''
    
    result: list[GameObject] = []

    if tile_size == None:
        tile_size = COVER_IMAGES[0].get_size()[0]

    barrier_width = tile_size * len(BARRIER_SHAPE[0]) # how wide should a barrier be
    barrier_spacing = (screen_width - (barrier_width * n_barriers)) / n_barriers # how much space should there be between barriers
    
    # create each barrier in the correct position and add it to the `result`
    for i in range(n_barriers):
        result.extend(
            generate_barrier(
                tile_size,
                Vector2(
                    (barrier_spacing / 2) + (tile_size / 2) + (i * (screen_width / n_barriers)),
                    height
                )
            )
        )
    
    return result
