from os import name
from typing import List, Optional, Dict
from enum import Enum
from .Items import ItemData, items
from dataclasses import dataclass


class LocationGroup(Enum):
    """
    Used to group locations
    """

    Boss = 0
    Event = 1
    Interactable = 2


@dataclass
class LocationData:
    name: str
    address: Optional[int] = None
    key: Optional[str] = None
    content: Optional[ItemData] = None
    group: Optional[LocationGroup] = None


locations: Dict[str, LocationData] = {location.name: location for location in [
# checks
    LocationData("Ruins 4 - Nola",                           address=1, key="Ruins_001_Zone_004.BP_Trigger_Event_C_0",              group=LocationGroup.Event,        content=items["Nola"]),
    LocationData("Ruins 5 - Charmed Fragment",               address=2, key="Ruins_001_Zone_005.BP_Interactable_AddItem_C_1",       group=LocationGroup.Interactable, content=items["Charmed Fragment"]),
    LocationData("Ruins 12 - Subterranean Testing Site Key", address=3, key="Ruins_001_Zone_012.BP_Interactable_AddItem_Skill_C_0", group=LocationGroup.Interactable, content=items["Subterranean Testing Site Key"]),
    LocationData("Ruins 12 - Lito",                          address=4, key="Ruins_001_Zone_012.BP_BossSpawner_C_0",                group=LocationGroup.Boss,         content=items["Lito"]),
    LocationData("Ruins 13 - Homunculus Research Log 1",     address=5, key="Ruins_001_Zone_013.BP_Interactable_AddItem_C_1",       group=LocationGroup.Interactable, content=items["Homunculus Research Log 1"]),
    LocationData("Ruins 14 - Worn Experiment Log",           address=6, key="Ruins_001_Zone_014.BP_Interactable_AddItem_C_1",       group=LocationGroup.Interactable, content=items["Worn Experiment Log"]),
    LocationData("Ruins 15 - Healing Ward",                  address=7, key="Ruins_001_Zone_015.BP_Trigger_Event_C_0",              group=LocationGroup.Event,        content=items["Healing Ward"]),

# New checks
    LocationData("Crossroad 2 - Charmed Fragment",           address=8,key="Crossroad_001_Zone_002.BP_Interactable_AddItem_C_1",       group=LocationGroup.Interactable, content=items["Charmed Fragment"]),
    LocationData("Slum 1 - Tattered Letter",                 address=9,key="Slum_001_Zone_001.BP_Interactable_AddItem_C_1",       group=LocationGroup.Interactable, content=items["Tattered Letter"]),


# event locations
    LocationData("Goal", content=items["Victory"]),
    LocationData("Ruins 7 - Lever", content=items["Ruins 7 Lever"]),
]}
