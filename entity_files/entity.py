# import libtcodpy as libtcod
from entity_files.entity_data import EntityID
from entity_files.entity_functions import random_gender
from entity_files.gender import Gender
from entity_files.job import Job
from map_files.world import Position, Floor
from game_data import Direction
from game_functions import direction_to_str
from typing import Optional


class Entity:
    def __init__(self, entity_id: EntityID, nickname: Optional[str]=None, gender: Optional[Gender]=None):
        # The following Entity variables can't be None
        self.entity_id: EntityID = entity_id
        if gender is None:
            self._gender: Gender = random_gender(self.entity_id.gendered)
        else:
            self._gender: Gender = gender
        self._body = None  # !#!#!#!# TODO MUST EXIST

        # The following Entity variables can be None
        self.nickname: Optional[str] = nickname
        self.position: Optional[Position] = None
        self.facing: Optional[Direction] = None  # Some objects don't have a face (body property)

        # TODO
        self._mobile = None  # If None it can't move or be moved
        self._fighter = None  # If None it can't fight
        self._job = None
        self._item = None  # If not None it can be placed in an inventory
        # ...

    # Entity has two types of variables:
    # public(ex: .facing) Can be changed by others using set_
    # protected(ex: ._gender) Can only return fake values modified by others from @property, uses assign_

    @property
    def name(self) -> str:
        if self.nickname:
            return self.nickname
        return self.entity_id.entity_name

    @property
    def char(self) -> str:
        if self == PLAYER_ENTITY:
            return "@"
        return self.entity_id.char

    @property  # depends on health or faction
    def char_fore_color(self) -> tuple:  # TODO tuple or libtcod.Color?
        # calculate
        return 150, 255, 150

    @property  # background color depends on action charge or cooldown
    def char_back_color(self) -> tuple:  # TODO tuple or libtcod.Color?
        # calculate
        return 0, 0, 0

    @property
    def x(self) -> int:
        if self.item:
            return self.item.x
            # if self.item.proprietary: return self.item.proprietary.x #TODO ITEM pos
        if self.position:
            return self.position.x
        return 0

    @property
    def y(self) -> int:
        if self.item:
            return self.item.y
        if self.position:
            return self.position.y
        return 0

    @property
    def floor(self) -> Optional[Floor]:
        if self.item:
            return self.item.floor
        if self.position:
            return self.position.floor
        return None

    # @property
    # def facing(self) -> Direction:
    #     return self._facing

    @property
    def gender(self) -> Gender:
        return self._gender

    @property
    def item(self):  # TODO -> :
        return self._item

    @property
    def fighter(self):  # TODO ->:
        return self._fighter

    @property
    def job(self):  # TODO -> :
        return self._job

    def assign_gender(self, gender: Gender):
        self._gender = gender

    def assign_job(self, job: Job):
        self._job = job
        job.owner = self  # TODO remember to add .owner reference to all the modules that need it

    ###

    def set_facing(self, direction: Direction):
        self.facing = direction

    def face_towards_direction(self, direction: tuple) -> bool:
        self.set_facing(direction_to_str(direction))
        return True

    def face_towards_position(self, position: Position) -> bool:
        return self.face_towards_direction((position.x - self.x, position.y - self.y))

    def walk(self, direction: tuple) -> bool:
        """When walking, the object turns towards that direction (tuple)"""
        self.face_towards_direction(direction)
        dx, dy = direction
        self.position.update(self.x+dx, self.y+dy, self.floor)
        return True


PLAYER_ENTITY: Entity = Entity(EntityID.HUMAN)


def get_player_entity() -> Entity:
    return PLAYER_ENTITY


def set_player_entity(entity: Entity):
    """When loading a game"""
    global PLAYER_ENTITY
    PLAYER_ENTITY = entity
