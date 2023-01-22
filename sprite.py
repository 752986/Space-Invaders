import pygame
from gameObject import (GameObject, GameState)


class Sprite(GameObject):
    def __init__(self, pos: pygame.Vector2, image: pygame.surface.Surface, image_size: pygame.Vector2 | None, alpha: bool = False):
        # resize the image if a size was provided
        if image_size == None:
            self.image = image
        else:
            self.image = pygame.transform.smoothscale(image, image_size)

        # convert the image into the correct format for the display surface
        if alpha:
            self.image = self.image.convert_alpha()
        else:
            self.image = self.image.convert()

        # calculate the bounding rect
        self.rect = self.image.get_rect()
        self.rect.center = (int(pos.x), int(pos.y))
        super().__init__(self.rect)

    def replace_image(self, new_image: pygame.surface.Surface, image_size: pygame.Vector2 | None, alpha: bool = False):
        '''Replaces the `Sprite`'s current image with a new one'''

        # resize the image if a size was provided
        if image_size == None:
            self.image = new_image
        else:
            self.image = pygame.transform.smoothscale(new_image, image_size)
        
        # convert the image into the correct format for the display surface
        if alpha:
            self.image = self.image.convert_alpha()
        else:
            self.image = self.image.convert()

        # calculate the new bounding rect
        old_pos = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_pos

    def update(self, game_state: GameState, delta: float):
        pass

    def draw(self, surface: pygame.surface.Surface):
        surface.blit(self.image, self.rect)
