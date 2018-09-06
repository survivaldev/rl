import libtcodpy as libtcod
from render_files.render_data import IconDisplay
from entity_files.entity import Entity


class GameConsole:
    def __init__(self, x: int, y: int, width: int, height: int, fore_fade: float, back_fade: float, parent=None):
        self.con_id: int = libtcod.console_new(width, height)
        self.parent: GameConsole = parent  # If None, it prints to root
        self.x: int = x  # The console's starting top left coordinates on it's parent interface
        self.y: int = y
        self.width: int = width
        self.height: int = height
        self.fore_fade: float = fore_fade
        self.back_fade: float = back_fade

    @property
    def parent_id(self) -> int:
        if self.parent:
            return self.parent.con_id
        return 0  # Defaults to root

    def blit(self):
        """x=0, y=0 starts printing from the beginning"""
        libtcod.console_blit(src=self.con_id, x=0, y=0, w=self.width, h=self.height, dst=self.parent_id,
                             xdst=self.x, ydst=self.y, ffade=self.fore_fade, bfade=self.back_fade)

    def change_size(self, new_width, new_height):
        self.con_id = libtcod.console_new(new_width, new_height)

    def draw_entity(self, entity: Entity, display: IconDisplay=IconDisplay.ICON):
        # libtcod.console_put_char_ex(con=self.con_id, x=entity.x, y=entity.y, c=entity.char,
        #                             fore=libtcod.white, back=libtcod.black)  # TODO entity.fore entity.back

        if display == IconDisplay.DIRECTION:
            if entity.facing:
                libtcod.console_put_char(self.con_id, entity.x, entity.y, entity.facing.value, libtcod.BKGND_NONE)
                return
        elif display == IconDisplay.JOB:
            if entity.job:  # TODO rework when jobs are implemented. job.icon
                libtcod.console_put_char(self.con_id, entity.x, entity.y, entity.job.icon, libtcod.BKGND_NONE)
                return
        # after the other conditions failed, print the entity, only if it has a Position
        if entity.position:
            libtcod.console_put_char(self.con_id, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)
