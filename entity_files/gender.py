from enum import Enum


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"
    GENDERLESS = "None"

    @property
    def nominative(self) -> str:
        if self == Gender.MALE:
            return "He"  # "He talked"
        elif self == Gender.FEMALE:
            return "She"  # "She talked"
        elif self == Gender.OTHER:
            return "They"  # "They talked"
        else:
            return "It"  # "It moved"

    @property
    def objective(self) -> str:
        if self == Gender.MALE:
            return "Him"  # "I called him"
        elif self == Gender.FEMALE:
            return "Her"  # "I called her"
        elif self == Gender.OTHER:
            return "Them"  # "I called them"
        else:
            return "It"  # "I turned it on"

    @property
    def possessive(self) -> str:
        if self == Gender.MALE:
            return "His"  # "His heart stopped"
        elif self == Gender.FEMALE:
            return "Her"  # "Her heart stopped"
        elif self == Gender.OTHER:
            return "Their"  # "Their tentacles wriggled"
        else:
            return "Its"  # "Its engine exploded"

    @property
    def possessive_pronoun(self) -> str:
        if self == Gender.MALE:
            return "His"  # "That is his"
        elif self == Gender.FEMALE:
            return "Hers"  # "That is hers"
        elif self == Gender.OTHER:
            return "Theirs"  # "That is theirs"
        else:
            return "Its"  # "That is its"

    @property
    def reflexive(self) -> str:
        if self == Gender.MALE:
            return "Himself"  # "He did it himself"
        elif self == Gender.FEMALE:
            return "Herself"  # "She did it herself"
        elif self == Gender.OTHER:
            return "Themselves"  # "They did it themselves"
        else:
            return "Itself"  # "It did it itself"
