from typing import Literal, Optional
from random import randint, choice, uniform

from pydantic import BaseModel, Extra, constr, conint, confloat


class Character(BaseModel):
    name: constr(max_length=255)
    level: conint(ge=1, le=20)
    profession: Literal["Fighter", "Mage", "Cleric", "Rogue"]
    offence: confloat(ge=0, lt=1)
    defense: confloat(ge=0, lt=1)

    class Config:
        extra = Extra.forbid


class CharacterOptions(BaseModel):
    name: Optional[constr(max_length=255)]
    level: Optional[conint(ge=1, le=20)]
    profession: Optional[Literal["Fighter", "Mage", "Cleric", "Rogue"]]
    offence: Optional[confloat(ge=0, lt=1)]
    defense: Optional[confloat(ge=0, lt=1)]

    class Config:
        extra = Extra.forbid


class RandomCharacter:
    professions = ["Fighter", "Mage", "Cleric", "Rogue"]
    names = [
        "John", "Jane", "Adam", "Anne", "Fred", "Francis", "Tom", "Terry",
        "George", "Genni", "Craig", "Carrie", "Kyle", "Kim", "Rosalyn",
        "Gwen", "Persephone", "Milena", "Paul", "Robert", "Stephen",
    ]

    def __init__(self):
        self.name = choice(self.names)
        self.level = randint(1, 20)
        self.profession = choice(self.professions)
        self.offence = uniform(0, 1)
        self.defense = uniform(0, 1)
