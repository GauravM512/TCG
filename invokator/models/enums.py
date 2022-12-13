"""TCG enums."""
import enum


class Element(str, enum.Enum):
    """Elemental type of a character."""

    ANEMO = "Anemo"
    CRYO = "Cryo"
    DENDRO = "Dendro"
    ELECTRO = "Electro"
    GEO = "Geo"
    HYDRO = "Hydro"
    PYRO = "Pyro"

    OMNI = "omni"
    PHYSICAL = "physical"

    INFUSED = "infused"


class CardType(str, enum.Enum):
    """Type of a card."""

    EQUIPMENT = "equipment"
    EVENT = "event"


class EquipmentType(str, enum.Enum):
    """Type of an equipment card."""

    ARTIFACT = "artifact"
    WEAPON = "weapon"


class TalentType(str, enum.Enum):
    """Type of a character's talent."""

    NORMAL = A = "normal"
    SKILL = E = "skill"
    BURST = Q = "burst"
    PASSIVE = "passive"


class EffectType(str, enum.Enum):
    """Effect type of a character's talent."""

    ATTACK = "attack"
    HEAL = "heal"
    SUMMON = "summon"
    EFFECT = "effect"
    INFUSE = "infuse"
    SWITCH = "switch"
    FORCESWITCH = "forceswitch"

    BUFF = "buff"
    CLEAR = "clear"
    DISCOUNT = "discount"
    DECREMENT = "decrement"
    DRAW = "draw"
    ADDDICE = "adddice"
    DESTROY = "destroy"
    EXTEND = "extend"
    SWAP = "swap"
    ENERGY = "energy"


class EffectTrigger(str, enum.Enum):
    """Trigger of an effect."""

    USED = "used"
    ATTACK = "attack"
    NORMAL = "normal"
    SKILL = "skill"
    BURST = "burst"
    DEPLETED = "depleted"
    START = "start"
    END = "end"
    SWITCH = "switch"

    SWIRL = "swirl"

    DEPLOY = "deploy"


class CardEffectAttachType(str, enum.Enum):
    """Type of card effect attachment."""

    STATIC = "static"
    DYNAMIC = "dynamic"


class SidelineTarget(str, enum.Enum):
    """Target of a destroy card."""

    SUMMON = "summon"
    FRIEND_SUMMON = "friend_summon"
    ENEMY_SUMMON = "enemy_summon"
    CHARACTER = "character"
    ACTIVE_CHARACTER = "active_character"