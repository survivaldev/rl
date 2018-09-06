from entity_files.gender import Gender
from game_functions import random_bool


def random_gender(gendered: bool) -> Gender:
    if not gendered:
        return Gender.GENDERLESS
    else:
        if random_bool():
            return Gender.MALE
        else:
            return Gender.FEMALE
