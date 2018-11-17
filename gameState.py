from enum import Enum


class GameState(Enum):
    STARTING = 1
    PLAYING = 2
    PAUSED = 3
    GAME_OVER = 4
