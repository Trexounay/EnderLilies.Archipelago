from typing import Callable, Dict, Optional
from BaseClasses import CollectionState, MultiWorld
from worlds.generic.Rules import CollectionRule, ItemRule
from .Items import ItemGroup, items
from .Types import EnderMagnoliaItem


keys = {items[name].key.rsplit('.', 1)[-1] : name for name in items}

class macros:
    DJUMP = lambda s, p: True
    FLOWER = lambda s, p: True

def is_skill(player : int, item: EnderMagnoliaItem) -> bool:
    return item.player == player and item.group == ItemGroup.Skill

def get_entrances_rules(p: int) -> Dict[str, CollectionRule]:
    return {
        "Ruins10Right": lambda s: s.has("Subterranean Testing Site Key", p),
        "Ruins13Left": lambda s: False,
        "Ruins02LowerLeft": lambda s: s.has("Ruins 7 Lever", p),  # lever
        "Ruins07UpperRight": lambda s: s.has("Ruins 7 Lever", p),  # lever
        "Ruins04UpperLeft": lambda s: False,  # fall
        "Ruins08Left" : lambda s: s.has("Hati's Charge", p),
        
        "Crossroad02Right": lambda s: s.has_all([keys["double_jump"], keys["dodge"]], p) or s.has_any([keys["high_jump"], keys["s5051_snow"]], p),
        "Crossroad02Left": lambda s: s.has_any([keys["double_jump"], keys["high_jump"], keys["wall_grab"], keys["s5052_flower"]], p)

    }

def get_locations_rules(p: int) -> Dict[str, CollectionRule]:
    return {
        "Goal": lambda s: s.can_reach("Slum 1 - Tattered Letter", None, p),
        "Ruins 5 - Charmed Fragment": lambda s: s.has("Aerial Jump", p) and s.has("Hati's Charge", p),
        "Crossroad 2 - Charmed Fragment": lambda s: s.has("Aerial Jump", p) and s.has("Dodge", p),
    }

def get_items_rules(p: int) -> Dict[str, ItemRule]:
    return {
        "Starting Skill": lambda i : is_skill(p, i),
    }
