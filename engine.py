import libtcodpy as libtcod
from input_handlers import handle_keys_keyboard, handle_keys_mouse, InputOption
from entity_files.entity import Entity, get_player_entity
from render_files.renderer import get_renderer
from map_files.world import Position, Floor
from typing import List  # , Dict
from render_files.render_data import Font
import random


GAME_INPUT_KEYBOARD: bool = True  # Keyboard only. If False, it will use keyboard+mouse  # TODO

ENTITIES: List[Entity] = []

# def window_test():
#   pass


def exit_game() -> bool:
    # TODO save etc
    libtcod.console_delete(0)
    return True


def main() -> bool:

    # TODO load from save
    renderer = get_renderer()

    key: libtcod.Key = libtcod.Key()
    mouse: libtcod.Mouse = libtcod.Mouse()

    get_player_entity().position = Position(x=20, y=15, floor=Floor())
    ENTITIES.append(get_player_entity())

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        renderer.clear_all()

        # DRAW map/windows/etc
        renderer.render_main(ENTITIES)
        renderer.blit_all()

        libtcod.console_flush()

        if GAME_INPUT_KEYBOARD:
            action = handle_keys_keyboard(key)
        else:
            action = handle_keys_mouse(key, mouse)

        if action:  # if dict not empty

            act_walk = action.get(InputOption.WALK)
            act_direction = action.get(InputOption.DIRECTION)
            act_camera = action.get(InputOption.CAMERA)
            act_close = action.get(InputOption.CLOSE)
            act_fullscreen = action.get(InputOption.FULLSCREEN)
            act_icon_display = action.get(InputOption.ICON_DISPLAY)
            act_window = action.get(InputOption.WINDOW)  # testing: opens a window
            act_zoom = action.get(InputOption.ZOOM)
            act_font = action.get(InputOption.FONT)

            if act_walk is not None:
                get_player_entity().walk(act_walk)
            elif act_direction is not None:
                get_player_entity().face_towards_direction(act_direction)
            elif act_fullscreen is not None:
                renderer.toggle_fullscreen()
            elif act_camera is not None:
                renderer.test_camera(act_camera)  # TODO testing
            elif act_window is not None:
                pass
                # renderer.window_test()  # TODO testing
            elif act_icon_display is not None:
                renderer.set_icon_display(act_icon_display)

            # Resets render
            elif act_zoom is not None:  # is None! act_zoom is False for zoom down
                renderer.change_game_zoom(act_zoom)
            elif act_font is not None:
                # TODO testing
                font = random.choice([Font.ARIAL, Font.CAELDERA, Font.CELTIC_GARAMOND, Font.CONSOLAS, Font.COURIER,
                                      Font.DEJAVU, Font.DEJAVU_WIDE, Font.DUNDALK, Font.LUCIDA, Font.PRESTIGE,
                                      Font.TERMINAL])
                renderer.change_game_font(font)
            elif act_close is not None:
                return exit_game()

    return True


if __name__ == '__main__':
    main()
