import pygame
from gameObject import GameObject


class Sprite(GameObject):
    def __init__(
        self,
        pos: pygame.Vector2,
        image: pygame.surface.Surface,
        image_size: pygame.Vector2 | None,
    ):
        self.image = pygame.transform.smoothscale(
            image, image_size if image_size != None else (1, 1)
        )
        self.rect = image.get_rect()
        self.rect.center = (int(pos.x), int(pos.y))
        super().__init__(self.rect)

    def draw(self, surface: pygame.surface.Surface):
        self.image.blit(surface, self.rect)
