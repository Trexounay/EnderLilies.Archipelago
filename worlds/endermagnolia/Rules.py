from typing import Callable, Dict, Optional
from BaseClasses import CollectionState, MultiWorld
from worlds.generic.Rules import CollectionRule

from .Items import ItemGroup


def get_entrances_rules(p: int) -> Dict[str, CollectionRule]:
    return {
        "Ruins10Right": lambda s: s.has("Subterranean Testing Site Key", p),
        "Ruins13Left": lambda s: False,
        "Ruins02LowerLeft": lambda s: s.has("Ruins 7 Lever", p),  # lever
        "Ruins07UpperRight": lambda s: s.has("Ruins 7 Lever", p),  # lever
        "Ruins04UpperLeft": lambda s: False,  # fall

        # test
        "Ruins08Left" : lambda s: False,

        # New rules
        "Crossroad02Right": lambda s: s.has("Aerial Jump", p) and s.has("Dodge", p),
    }

def get_locations_rules(p: int) -> Dict[str, CollectionRule]:
    return {
        "Goal": lambda s: s.can_reach("Slum 1 - Tattered Letter", p),

        "Ruins 14 - Worn Experiment Log": lambda s: True,
        "Ruins 5 - Charmed Fragment": lambda s: s.has("Aerial Jump", p) and s.has("Hati's Charge", p),
        "Crossroad 2 - Charmed Fragment": lambda s: s.has("Aerial Jump", p) and s.has("Dodge", p),
    }
