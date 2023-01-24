import enemy
from pygame import Vector2, Rect
from gameObject import GameObject, GameState


class Wave(GameObject):
    def __init__(self, game_state: GameState) -> None:
        super().__init__(Rect(0, 0, 0, 0))
        self.wave_height = 32
        self.fill_wave(game_state)

    def pos(self, i: int, layer_addition: int):
        return Vector2((i * 100) + 32, self.wave_height + layer_addition)

    def fill_wave(self, game_state: GameState) -> None:
        game_state.game_objects.extend(enemy.Octo(self.pos(i, 0)) for i in range(10))
        game_state.game_objects.extend(enemy.Crab(self.pos(i, 64)) for i in range(10))
        game_state.game_objects.extend(enemy.Crab(self.pos(i, 128)) for i in range(10))
        game_state.game_objects.extend(enemy.Skull(self.pos(i, 192)) for i in range(10))
        game_state.game_objects.extend(enemy.Skull(self.pos(i, 256)) for i in range(10))

    def update(self, game_state: GameState, delta: float) -> None:
        self.move(game_state, delta)

    def move(self, game_state: GameState, delta: float) -> None:
        flip = False
        for enemy in self.get_enemies(game_state):
            enemy.rect.move_ip(enemy.vel * delta)
            if enemy.rect.left < 0 or enemy.rect.right > 1920:
                flip = True
        if flip:
            print("Flipping")
            self.change_direction(game_state)

    def change_direction(self, game_state: GameState) -> None:
        for enemy in self.get_enemies(game_state):
            enemy.vel.x *= -1
            enemy.rect.move_ip(0, 5)

    def get_enemies(self, game_state: GameState):
        for object in game_state.game_objects:
            if isinstance(object, enemy.Enemy):
                yield object
