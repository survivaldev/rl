from enum import Enum


class EntityID(Enum):
    HUMAN = "Human", "H", True, True

    def __init__(self, entity_name: str, char: str, gendered: bool, has_face: bool):
        self.entity_name: str = entity_name
        self.char: str = char
        self.gendered: bool = gendered
        self.has_face: bool = has_face

    # def build_def_body()
        # self.has_face,self.weight etc
    # def build_def_fighter()
    # def build_def_mobile()
