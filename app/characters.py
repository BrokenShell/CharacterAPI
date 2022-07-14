from pydantic import BaseModel, constr, conint, confloat, Extra
from pydantic.schema import Literal, Optional


class Character(BaseModel):
    name: constr(min_length=3, max_length=16)
    level: conint(ge=1, le=20)
    profession: Literal["Fighter", "Mage", "Cleric", "Rogue"]
    offence: confloat(ge=0, lt=1)
    defense: confloat(ge=0, lt=1)

    class Config:
        extra = Extra.forbid


class CharacterOptions(BaseModel):
    name: Optional[constr(min_length=3, max_length=16)]
    level: Optional[conint(ge=1, le=20)]
    profession: Optional[Literal["Fighter", "Mage", "Cleric", "Rogue"]]
    offence: Optional[confloat(ge=0, lt=1)]
    defense: Optional[confloat(ge=0, lt=1)]

    class Config:
        extra = Extra.forbid
