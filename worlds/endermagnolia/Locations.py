from os import name
from typing import List, Optional, Dict
from enum import Enum
from .Items import ItemData, items


class LocationGroup(Enum):
    """
    Used to group locations
    """

    Boss = 0
    Event = 1
    Interactable = 2


class LocationData:
    name: str
    address: Optional[int]
    key: Optional[str]
    content: Optional[ItemData]
    location_group: Optional[LocationGroup]

    def __init__(self, name, address: Optional[int] = None, key: Optional[str] = None,
                 content: Optional[ItemData] = None,
                 group: Optional[LocationGroup] = None):
        self.name = name
        self.address = address
        self.key = key
        self.content = content
        self.location_group = group

locations: Dict[str, LocationData] = {location.name: location for location in [
# checks
    LocationData("Ruins 4 - Nola",                           address=0x1, key="Ruins_001_Zone_004.BP_Trigger_Event_C_0",              group=LocationGroup.Event,        content=items["Nola"]),
    LocationData("Ruins 5 - Charmed Fragment",               address=0x2, key="Ruins_001_Zone_005.BP_Interactable_AddItem_C_1",       group=LocationGroup.Interactable, content=items["Charmed Fragment"]),
    LocationData("Ruins 12 - Subterranean Testing Site Key", address=0x3, key="Ruins_001_Zone_012.BP_Interactable_AddItem_Skill_C_0", group=LocationGroup.Interactable, content=items["Subterranean Testing Site Key"]),
    LocationData("Ruins 12 - Lito",                          address=0x4, key="Ruins_001_Zone_012.BP_BossSpawner_C_0",                group=LocationGroup.Boss,         content=items["Lito"]),
    LocationData("Ruins 13 - Homunculus Research Log 1",     address=0x5, key="Ruins_001_Zone_013.BP_Interactable_AddItem_C_1",       group=LocationGroup.Interactable, content=items["Homunculus Research Log 1"]),
    LocationData("Ruins 14 - Worn Experiment Log",           address=0x6, key="Ruins_001_Zone_014.BP_Interactable_AddItem_C_1",       group=LocationGroup.Interactable, content=items["Worn Experiment Log"]),
    LocationData("Ruins 15 - Healing Ward",                  address=0x7, key="Ruins_001_Zone_015.BP_Trigger_Event_C_0",              group=LocationGroup.Event,        content=items["Healing Ward"]),

# event locations
    LocationData("Goal", content=items["Victory"]),
    LocationData("Ruins 7 - Lever", content=items["Ruins 7 Lever"]),
]}
