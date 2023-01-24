import enemy
from pygame import Vector2, Rect
from gameObject import GameObject, GameState


class Wave(GameObject):
    def __init__(self, game_state: GameState) -> None:
        super().__init__(Rect(0, 0, 0, 0))
        self.wave_height = 0
        self.fill_wave(game_state)

    def fill_wave(self, game_state: GameState) -> None:
        game_state.game_objects.extend(
            enemy.Octo(Vector2(i * 100, self.wave_height)) for i in range(10)
        )
        game_state.game_objects.extend(
            enemy.Crab(Vector2(i * 100, self.wave_height + 100)) for i in range(10)
        )
        game_state.game_objects.extend(
            enemy.Crab(Vector2(i * 100, self.wave_height + 150)) for i in range(10)
        )
        game_state.game_objects.extend(
            enemy.Skull(Vector2(i * 100, self.wave_height + 200)) for i in range(10)
        )
        game_state.game_objects.extend(
            enemy.Skull(Vector2(i * 100, self.wave_height + 250)) for i in range(10)
        )

    def update(self, game_state: GameState, delta: float) -> None:
        self.move(game_state, delta)

    def move(self, game_state: GameState, delta: float) -> None:
        flip = False
        for object in game_state.game_objects:
            if type(object) is enemy.Enemy:
                object.rect.move_ip(object.vel * delta)
                if object.rect.left < 0 or object.rect.right > 1920:
                    flip = True
        if flip:
            self.change_direction(game_state)

    def change_direction(self, game_state: GameState) -> None:
        for enemy in self.get_enemies(game_state):
            enemy.vel.x *= -1
            enemy.rect.move_ip(0, 5)

    def get_enemies(self, game_state: GameState):
        for object in game_state.game_objects:
            if type(object) is enemy.Enemy:
                yield object
