import pygame
import keymap
import settings
from gameObject import GameObject
from level import Wave


def main():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    running = True

    clock = pygame.time.Clock()

    game_objects: list[GameObject] = []
    game_objects.append(Wave())

    delta: float = 0
    while running:
        for event in pygame.event.get():
            # mouse = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

        keys = pygame.key.get_pressed()

        if keys[keymap.QUIT]:
            running = False

        delta = clock.tick(settings.FRAMERATE)

        for object in game_objects:
            object.update(game_objects, delta)

        screen.fill((0, 0, 0))

        for object in game_objects:
            object.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
