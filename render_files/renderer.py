import libtcodpy as libtcod
from render_files.game_console import GameConsole
from render_files.render_data import IconDisplay, Font, GAME_FONTS
from rpg import GAME_NAME
from typing import List  # , Dict


class Renderer:
    def __init__(self, screen_width: int=80, screen_height: int=50, font_path: str="fonts/arial10x10.png",
                 game_fullscreen: bool=False):
        self.screen_width: int = screen_width
        self.screen_height: int = screen_height
        self.game_fullscreen: bool = game_fullscreen
        # other values are set to default
        self.game_size = 1
        self.game_font = Font.ARIAL
        self.display_icon: IconDisplay = IconDisplay.ICON
        # Creates libtcod root console
        libtcod.console_set_custom_font(fontFile=font_path,
                                        flags=libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
        libtcod.console_init_root(w=self.screen_width, h=self.screen_height, title=GAME_NAME,
                                  fullscreen=self.game_fullscreen)
        # Console game scene
        self.consoles_scene: List[GameConsole] = list()

        # Default console values
        self.console_main: GameConsole = self.add_game_console(x=1, y=1, width=int(80 / 2),
                                                               height=int(50 / 2), fore_fade=1, back_fade=1)

    def toggle_fullscreen(self):
        self.game_fullscreen = not self.game_fullscreen
        # libtcod.console_set_fullscreen(self.game_fullscreen)
        # libtcod.console_delete(0)
        libtcod.sys_shutdown()
        libtcod.console_init_root(w=self.screen_width, h=self.screen_height, title=GAME_NAME,
                                  fullscreen=self.game_fullscreen)

    def change_game_zoom(self, zoom: bool):  # bool (zoom+)True (zoom-)False
        if zoom:
            font_data = GAME_FONTS.get(self.game_font, [])
            if self.game_size + 1 < len(font_data):
                self.game_size += 1
        else:
            if self.game_size > 0:
                self.game_size -= 1
        self.update_root_console()

    def change_game_font(self, font: Font):
        self.game_font = font
        self.game_size = 0
        self.update_root_console()

    def update_root_console(self):
        # libtcod.console_delete(0)
        libtcod.sys_shutdown()
        font_path = "fonts/" + GAME_FONTS.get(self.game_font, [])[self.game_size]
        libtcod.console_set_custom_font(fontFile=font_path,
                                        flags=libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
        libtcod.console_init_root(w=self.screen_width, h=self.screen_height, title=GAME_NAME,
                                  fullscreen=self.game_fullscreen)

    def set_icon_display(self, new_display: IconDisplay):
        if self.display_icon == new_display:
            self.display_icon = IconDisplay.ICON
        else:
            self.display_icon = new_display

    def add_game_console(self, x: int, y: int, width: int, height: int, fore_fade: float, back_fade: float,
                         parent: GameConsole=None) -> GameConsole:
        new_console: GameConsole = GameConsole(x=x, y=y, width=width, height=height,
                                               fore_fade=fore_fade, back_fade=back_fade, parent=parent)
        self.consoles_scene.append(new_console)
        return new_console

    # def delete_console(self, del_con: GameConsole):

    def clear_all(self):
        """Prints frame in root, clears all (default clear=True)"""
        libtcod.console_print_frame(con=0, x=0, y=0, w=self.screen_width, h=self.screen_height, fmt=GAME_NAME)

    def blit_all(self):
        for console in reversed(self.consoles_scene):
            console.blit()

    def render_main_map(self):
        """Renders floor in main based on current map coordinates"""
        for tile_x in range(0, self.console_main.width):
            for tile_y in range(0, self.console_main.height):
                libtcod.console_put_char(self.console_main.con_id, tile_x, tile_y, ".", libtcod.BKGND_NONE)

    def render_main_entities(self, entities):  # : List[Entity]):
        """Renders all the entities in the Main console"""
        for entity in entities:
            self.console_main.draw_entity(entity, self.display_icon)

    def render_main(self, entities):  # : List[Entity]):
        self.render_main_map()  # send floor
        self.render_main_entities(entities)
        # libtcod.console_print_frame(con=window.con_id, x=0, y=0, w=window.width, h=window.height, clear=True,
        #                             flag=libtcod.BKGND_DEFAULT, fmt="WINDOW")

    # def window_test(self):
    #     pass

    def test_camera(self, camera: tuple):  # TODO testing
        dx, dy = camera
        self.console_main.x += dx
        self.console_main.y += dy


GAME_RENDERER: Renderer = Renderer()


def get_renderer() -> Renderer:
    return GAME_RENDERER


def set_renderer(renderer: Renderer):
    """For loading"""
    global GAME_RENDERER
    GAME_RENDERER = renderer
