

from .env import BG_LEFT_WIDTH


def shift_left_with_bg_width(pos: tuple) -> tuple:
    return (pos[0] - BG_LEFT_WIDTH, pos[1])
