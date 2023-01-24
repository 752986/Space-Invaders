import pygame
from gameObject import GameState
from sprite import Sprite


class AnimatedSprite(Sprite):
	animation_speed: float

	def __init__(self, pos: pygame.Vector2, images: list[pygame.surface.Surface], image_size: pygame.Vector2 | None, alpha: bool = False):
		super().__init__(pos, images[0], image_size, alpha)
		self.animation_speed = 1

	def update(self, game_state: GameState, delta: float):
		pass

	def draw(self, surface: pygame.surface.Surface):
		return super().draw(surface)