import pygame

class GameObject:
    should_delete: bool
    def __init__(self, rect: pygame.Rect):
        self.rect: pygame.Rect = rect
        self.should_delete = False

    def update(self, game_state: "GameState", delta: float):
        pass

    def draw(self, surface: pygame.surface.Surface):
        pass

class GameState:
    def __init__(self, game_objects: list[GameObject]):
        self.game_objects = game_objects
