import enemy
from pygame import Vector2, Rect, display
from gameObject import GameObject, GameState


ENEMY_SPACING = 64
ENEMY_PER_ROW = 11
STEP_SIZE = 1 / 6


class Wave(GameObject):
    def __init__(self, game_state: GameState) -> None:
        super().__init__(Rect(0, 0, 0, 0))
        self.wave_height = 32
        self.fill_wave(game_state)
        self.pause_time_counter = 0
        self.pause_time = 0.25  # time in seconds between steps

    def pos_from_col(self, i: int, layer_addition: int):
        return Vector2((i * ENEMY_SPACING) + 32, self.wave_height + layer_addition)

    def fill_wave(self, game_state: GameState) -> None:
        game_state.game_objects.extend(
            enemy.Octo(self.pos_from_col(i, 0)) for i in range(ENEMY_PER_ROW)
        )
        game_state.game_objects.extend(
            enemy.Crab(self.pos_from_col(i, 64)) for i in range(ENEMY_PER_ROW)
        )
        game_state.game_objects.extend(
            enemy.Crab(self.pos_from_col(i, 128)) for i in range(ENEMY_PER_ROW)
        )
        game_state.game_objects.extend(
            enemy.Skull(self.pos_from_col(i, 192)) for i in range(ENEMY_PER_ROW)
        )
        game_state.game_objects.extend(
            enemy.Skull(self.pos_from_col(i, 256)) for i in range(ENEMY_PER_ROW)
        )

    def update(self, game_state: GameState, delta: float) -> None:
        if self.get_enemies(game_state):
            self.move(game_state, delta)
        else:
            self.fill_wave(game_state)

    def move(self, game_state: GameState, delta: float) -> None:
        self.pause_time_counter += delta
        if self.pause_time_counter >= self.pause_time:
            self.pause_time_counter = 0
            flip = False
            for enemy in self.get_enemies(game_state):
                enemy.rect.move_ip(enemy.vel * ENEMY_SPACING * STEP_SIZE)
                if (
                    enemy.rect.left < 0
                    or enemy.rect.right > display.get_window_size()[0]
                ):
                    flip = True
            if flip:
                self.change_direction(game_state)

    def change_direction(self, game_state: GameState) -> None:
        height_change = 32
        for enemy in self.get_enemies(game_state):
            enemy.vel.x *= -1
            enemy.rect.move_ip(0, height_change)
            self.wave_height += height_change

    def get_enemies(self, game_state: GameState):
        enemies: list[enemy.Enemy] = []
        for object in game_state.game_objects:
            if isinstance(object, enemy.Enemy):
                enemies.append(object)
        return enemies
