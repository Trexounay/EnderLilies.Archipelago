from typing import Callable, Dict, Optional
from BaseClasses import CollectionState, MultiWorld
from worlds.generic.Rules import CollectionRule

from .Items import ItemGroup


def get_entrances_rules(p: int) -> Dict[str, CollectionRule]:
    return {
        "Ruins 10 to Ruins 13": lambda s: s.has("Subterranean Testing Site Key", p),
        "Ruins 13 to Ruins 10": lambda s: False,
        "Ruins 2 to Ruins 7": lambda s: s.has("Ruins 7 Lever", p),  # lever
        "Ruins 7 to Ruins 2": lambda s: s.has("Ruins 7 Lever", p),  # lever
        "Ruins 4 to Ruins 3": lambda s: False,  # fall
        
        # New rules
        "Crossroad 2 to Slum 1": lambda s: s.has("Aerial Jump", p) and s.has("Dodge", p),

    }


def get_locations_rules(p: int) -> Dict[str, CollectionRule]:
    return {
        # Starting location
        "Ruins 14 - Worn Experiment Log": lambda s: True,
        "Goal": lambda s: s.can_reach_location(
            "Slum 1 - Tattered Letter", p
        ),
        "Ruins 5 - Charmed Fragment": lambda s: s.has("Aerial Jump", p) and s.has("Hati's Charge", p),
        "Crossroad 2 - Charmed Fragment": lambda s: s.has("Aerial Jump", p) and s.has("Dodge", p),
    }
