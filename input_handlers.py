import libtcodpy as libtcod
from render_files.game_console import IconDisplay
from enum import Enum, auto
from typing import Dict, Any


class InputOption(Enum):
    FULLSCREEN = auto()
    DIRECTION = auto()
    CLOSE = auto()
    WALK = auto()
    CAMERA = auto()
    ICON_DISPLAY = auto()
    LANGUAGE = auto()
    ZOOM = auto()
    FONT = auto()
    WINDOW = auto()


def handle_keys_keyboard(key: libtcod.Key) -> Dict[InputOption, Any]:
    if key.lalt:
        # System display keys
        if key.vk == libtcod.KEY_ENTER:
            return {InputOption.FULLSCREEN: True}
    elif key.lctrl:
        # Player direction keys
        if key.vk == libtcod.KEY_KP8:
            return {InputOption.DIRECTION: (0, -1)}
        elif key.vk == libtcod.KEY_KP2:
            return {InputOption.DIRECTION: (0, 1)}
        elif key.vk == libtcod.KEY_KP4:
            return {InputOption.DIRECTION: (-1, 0)}
        elif key.vk == libtcod.KEY_KP6:
            return {InputOption.DIRECTION: (1, 0)}
        elif key.vk == libtcod.KEY_KP7:
            return {InputOption.DIRECTION: (-1, -1)}
        elif key.vk == libtcod.KEY_KP1:
            return {InputOption.DIRECTION: (-1, 1)}
        elif key.vk == libtcod.KEY_KP9:
            return {InputOption.DIRECTION: (1, -1)}
        elif key.vk == libtcod.KEY_KP3:
            return {InputOption.DIRECTION: (1, 1)}
        # Changes renderer values
        elif key.vk == libtcod.KEY_KPADD:
            return {InputOption.ZOOM: True}
        elif key.vk == libtcod.KEY_KPSUB:
            return {InputOption.ZOOM: False}
        else:
            key_char = chr(key.c)
            # Game display keys
            if key_char == 'j':
                return {InputOption.ICON_DISPLAY: IconDisplay.JOB}
            elif key_char == 'd':
                return {InputOption.ICON_DISPLAY: IconDisplay.DIRECTION}
            # Rework/remove the following
            elif key_char == "f":  # move to settings menu?
                return {InputOption.FONT: True}
            elif key_char == "l":  # move to settings menu?
                return {InputOption.LANGUAGE: True}
            elif key_char == "w":
                return {InputOption.WINDOW: True}


    else:
        # System keys
        if key.vk == libtcod.KEY_ESCAPE:
            return {InputOption.CLOSE: True}
        # Movement keys
        elif key.vk == libtcod.KEY_KP8:
            return {InputOption.WALK: (0, -1)}
        elif key.vk == libtcod.KEY_KP2:
            return {InputOption.WALK: (0, 1)}
        elif key.vk == libtcod.KEY_KP4:
            return {InputOption.WALK: (-1, 0)}
        elif key.vk == libtcod.KEY_KP6:
            return {InputOption.WALK: (1, 0)}
        elif key.vk == libtcod.KEY_KP7:
            return {InputOption.WALK: (-1, -1)}
        elif key.vk == libtcod.KEY_KP1:
            return {InputOption.WALK: (-1, 1)}
        elif key.vk == libtcod.KEY_KP9:
            return {InputOption.WALK: (1, -1)}
        elif key.vk == libtcod.KEY_KP3:
            return {InputOption.WALK: (1, 1)}
        # Camera keys
        elif key.vk == libtcod.KEY_UP:
            return {InputOption.CAMERA: (0, -1)}
        elif key.vk == libtcod.KEY_DOWN:
            return {InputOption.CAMERA: (0, 1)}
        elif key.vk == libtcod.KEY_LEFT:
            return {InputOption.CAMERA: (-1, 0)}
        elif key.vk == libtcod.KEY_RIGHT:
            return {InputOption.CAMERA: (1, 0)}

    return {}


def handle_keys_mouse(key: libtcod.Key, mouse: libtcod.Mouse) -> Dict[InputOption, Any]:

    # if user_input.char == "w":
    #     return {"walk": (0, -1)}
    # elif user_input.char == "x":
    #     return {"walk": (0, 1)}
    # elif user_input.char == "a":
    #     return {"walk": (-1, 0)}
    # elif user_input.char == "d":
    #     return {"walk": (1, 0)}

    return {}
