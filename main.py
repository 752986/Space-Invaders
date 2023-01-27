import pygame
import keymap
import settings
from gameObject import GameObject, GameState
from player import Player
from cover import generate_cover
from level import Wave


def main():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    SCREEN_SIZE = pygame.display.get_surface().get_size()

    running = True

    clock = pygame.time.Clock()

    game_objects: list[GameObject] = []
    game_state = GameState(game_objects)

    game_objects.append(
        Player(game_state, pygame.Vector2(SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] - 50))
    )
    game_objects.extend(generate_cover(SCREEN_SIZE[0], 4, SCREEN_SIZE[1] - 250, None))
    game_objects.append(Wave(game_state))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

        keys = pygame.key.get_pressed()

        if keys[keymap.QUIT]:
            running = False

        delta = (
            clock.tick(settings.FRAMERATE) / 1000
        )  # get delta and convert from milliseconds to seconds

        for object in game_objects:
            object.update(game_state, delta)

        for object in game_objects:
            if object.should_delete:
                game_objects.remove(object)

        screen.fill((10, 10, 20))

        for object in game_objects:
            object.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
