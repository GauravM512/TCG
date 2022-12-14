"""TCG effects."""
import typing

import pydantic
from typing_extensions import Self

from .enums import (
    CardPosition,
    EffectTrigger,
    EffectType,
    Element,
    EquipmentType,
    ReactionType,
    SidelineLocation,
    SidelineTarget,
    TalentType,
)


class DiceCost(pydantic.BaseModel):
    """TCG dice cost."""

    amount: int = 0
    element: Element | None = None


class Trigger(pydantic.BaseModel):
    """Effect trigger."""

    type: EffectTrigger | None = None
    talent: TalentType | None = None
    reaction: ReactionType | None = None


class Effect(pydantic.BaseModel):
    """TCG attack effect."""

    def __new__(cls, **kwargs: typing.Any) -> Self:
        return super().__new__(_EFFECT_CLASSES[EffectType(kwargs["type"])])

    trigger: Trigger = Trigger()

    type: EffectType


class CardEffect(Effect):
    """TCG card effect."""

    type: EffectType = EffectType.CARD

    id: str


class AttackEffect(Effect):
    """TCG attack effect."""

    type: EffectType = EffectType.ATTACK

    damage: int
    element: Element


class HealEffect(Effect):
    """TCG heal effect."""

    type: EffectType = EffectType.HEAL

    amount: int


class SummonEffect(Effect):
    """TCG summon effect."""

    type: EffectType = EffectType.SUMMON

    id: str


class EffectEffect(Effect):
    """TCG effect effect."""

    type: EffectType = EffectType.EFFECT

    id: str


class InfuseEffect(Effect):
    """TCG infuse effect."""

    type: EffectType = EffectType.INFUSE

    element: Element


class SwitchEffect(Effect):
    """TCG switch effect."""

    type: EffectType = EffectType.SWITCH

    instant: bool = False


class ForceSwitchEffect(Effect):
    """TCG force switch effect."""

    type: EffectType = EffectType.FORCESWITCH
    
    switch_pos: CardPosition


class BuffEffect(Effect):
    """TCG buff effect."""

    type: EffectType = EffectType.BUFF

    amount: int


class ClearEffect(Effect):
    """TCG clear effect."""

    type: EffectType = EffectType.CLEAR


class DiscountEffect(Effect):
    """TCG discount effect."""

    type: EffectType = EffectType.DISCOUNT

    dice: list[DiceCost]


class DecrementEffect(Effect):
    """TCG decrement effect."""

    type: EffectType = EffectType.DECREMENT

    amount: int = 1


class DrawEffect(Effect):
    """TCG draw effect."""

    type: EffectType = EffectType.DRAW

    amount: int


class AddDiceEffect(Effect):
    """TCG add dice effect."""

    type: EffectType = EffectType.ADDDICE

    dice: list[DiceCost]


class DestroyEffect(Effect):
    """TCG destroy effect."""

    type: EffectType = EffectType.DESTROY

    target: SidelineTarget
    location: SidelineLocation

    amount: int = 1


class ExtendEffect(Effect):
    """TCG extend effect."""

    type: EffectType = EffectType.EXTEND

    target: SidelineTarget
    location: SidelineLocation = SidelineLocation.FRIEND


class SwapEffect(Effect):
    """TCG swap effect."""

    type: EffectType = EffectType.SWAP

    slot: EquipmentType


class EnergyEffect(Effect):
    """TCG energy effect."""

    type: EffectType = EffectType.ENERGY

    amount: int
    target: SidelineTarget = SidelineTarget.ACTIVE_CHARACTER
    location: SidelineLocation = SidelineLocation.FRIEND


_EFFECT_CLASSES: dict[EffectType, type[Effect]] = {
    cls.__fields__["type"].default: cls
    for cls in Effect.__subclasses__()
    if "type" in cls.__fields__ and cls.__fields__["type"].default
}
