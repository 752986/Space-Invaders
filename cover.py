import pygame
from pygame.math import Vector2
from gameObject import GameObject
from sprite import Sprite
from utility import is_hit


# the 4 stages of damage for a tile of cover
COVER_IMAGES = [
    pygame.image.load("invaders_imgs/barrier_0.png").convert_alpha(),
    pygame.image.load("invaders_imgs/barrier_1.png").convert_alpha(),
    pygame.image.load("invaders_imgs/barrier_2.png").convert_alpha(),
    pygame.image.load("invaders_imgs/barrier_3.png").convert_alpha(),
]

# the layout of each barrier
BARRIER_SHAPE = [
    [False, True, True, False],
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

    def update(self, game_objects: list[GameObject], delta: float):
        # if a projectile is colliding with the tile, take damage
        if is_hit(self, game_objects):
            self.health -= 1

            # if the tile is dead, remove it; otherwise, progress its stage of damage
            if self.health <= 0:
                self.should_delete = True
            else:
                self.replace_image(
                    COVER_IMAGES[4 - self.health], Vector2(self.rect.size))


# create the CoverTiles that form a single barrier 
def generate_barrier(tile_size: float, position: Vector2) -> list[CoverTile]:
    tiles: list[CoverTile] = []

    for (y, row) in enumerate(BARRIER_SHAPE):
        for (x, val) in enumerate(row):
            if val:
                tiles.append(CoverTile(
                    position + Vector2(x * tile_size, -y * tile_size), Vector2(tile_size)))

    return tiles


# generate and fill in all of the needed barriers
def fill_cover(add_to: list[GameObject], tile_size: float, height: float, screen_width: float, n_barriers: int):
    barrier_width = tile_size * len(BARRIER_SHAPE[0]) # how wide should a barrier be
    barrier_spacing = (screen_width - (barrier_width * n_barriers)) / n_barriers # how much space should there be between barriers
    
    # create each barrier in the correct position and add it to the provided `add_to` array
    for i in range(n_barriers):
        add_to.extend(
            generate_barrier(
                tile_size,
                Vector2(
                    (barrier_spacing / 2) + (i * barrier_spacing),
                    height
                )
            )
        )
