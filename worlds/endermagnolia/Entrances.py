from dataclasses import dataclass, field
from typing import Dict, Iterator, Tuple, TYPE_CHECKING

from BaseClasses import EntranceType
from entrance_rando import (ERPlacementState, disconnect_entrance_for_randomization,
                            randomize_entrances)

from .Options import ShuffleTransitions

if TYPE_CHECKING:
    from . import EnderMagnoliaWorld


@dataclass
class TransitionSide:
    spawn: str
    region: str


@dataclass
class TransitionData:
    name: str
    sides: Tuple[TransitionSide, TransitionSide]


@dataclass
class TransitionTable:
    rows: Dict[str, tuple]
    transitions: Dict[str, TransitionData] = field(init=False)
    region_spawn: Dict[str, str] = field(init=False)
    vanilla_connections: Dict[str, str] = field(init=False)

    def __post_init__(self):
        self.transitions = {}
        self.region_spawn = {}
        self.vanilla_connections = {}
        for name, row in self.rows.items():
            sides = tuple(TransitionSide(*side) for side in row)
            if bool(sides[0].region) != bool(sides[1].region):
                raise ValueError(f"transition with a single mapped region: {name}")
            self.transitions[name] = TransitionData(name, sides)
            for index, side in enumerate(sides):
                if side.region:
                    self.region_spawn[side.region] = side.spawn
                    self.vanilla_connections[side.region] = sides[1 - index].region

    def vanilla_spawn(self, region: str) -> str:
        return self.region_spawn[self.vanilla_connections[region]]

    def __getitem__(self, name: str) -> TransitionData:
        return self.transitions[name]

    def __len__(self) -> int:
        return len(self.transitions)

    def __iter__(self) -> Iterator[TransitionData]:
        return iter(self.transitions.values())

transitions = TransitionTable({
    "center_garden_001":    (("Center_001.garden001",       "Center03LeftDoor"),        ("Garden_001.center001",       "Garden12RightDoor")),
    "center_kowloon_001":   (("Center_001.kowloon001",      "Center03RightDoor"),       ("Kowloon_001.center001",      "Kowloon01LeftDoor")),
    "crossroad_mine_001":   (("Crossroad_001.mine001",      "Crossroad03Left"),         ("Mine_001.crossroad001",      "Mine01Right")),
    "crossroad_slum_001":   (("Slum_001.crossroad001",      "Slum01Left"),              ("Crossroad_001.slum001",      "Crossroad02Right")),
    "factory_garden_001":   (("Factory_001.garden001",      "Factory03Right"),          ("Garden_001.factory001",      "Garden14Left")),
    "forest_estate_001":    (("Forest_001.estate001",       "Forest09LowerRight"),      ("Estate_001.forest001",       "Estate12Left")),
    "garden_labo_001":      (("Garden_001.labo001",         "Garden08Upper"),           ("Labo_001.garden001",         "Labo06Lower")),
    "inner_center_001":     (("Center_001.playerstart001a", "Center05CenterDoor"),      ("Center_001.playerstart001b", "Center01LeftDoor")),
    "inner_center_002":     (("Center_001.playerstart002a", "Center03CenterRightDoor"), ("Center_001.playerstart002b", "Center05RightDoor")),
    "inner_center_003":     (("Center_001.playerstart003a", "Center01RightDoor"),       ("Center_001.playerstart003b", "Center04RightDoor")),
    "inner_center_004":     (("Center_001.playerstart004a", "Center03CenterLeftDoor"),  ("Center_001.playerstart004b", "Center05LeftDoor")),
    "inner_forest_001":     (("Forest_001.playerstart001a", "Forest04UpperCenterDoor"), ("Forest_001.playerstart001b", "Forest02LowerDoor")),
    "inner_forest_002":     (("Forest_001.playerstart002a", "Forest06CenterDoor"),      ("Forest_001.playerstart002b", "Forest02UpperLeftDoor")),
    "inner_forest_003":     (("Forest_001.playerstart003a", "Forest05CenterLowerDoor"), ("Forest_001.playerstart003b", "Forest02UpperRightDoor")),
    "inner_forest_004":     (("Forest_001.playerstart004a", "Forest09CenterRightDoor"), ("Forest_001.playerstart004b", "Forest03LowerRightDoor")),
    "inner_forest_005":     (("Forest_001.playerstart005a", "Forest09CenterDoor"),      ("Forest_001.playerstart005b", "Forest04LowerCenterRightDoor")),
    "inner_forest_006":     (("Forest_001.playerstart006a", "Forest07LeftDoor"),        ("Forest_001.playerstart006b", "Forest03UpperDoor")),
    "inner_forest_007":     (("Forest_001.playerstart007a", "Forest06LowerRightDoor"),  ("Forest_001.playerstart007b", "Forest05CenterUpperDoor")),
    "inner_forest_008":     (("Forest_001.playerstart008a", "Forest12UpperDoor"),       ("Forest_001.playerstart008b", "Forest06LowerLeftDoor")),
    "inner_forest_009":     (("Forest_001.playerstart009a", "Forest08LowerDoor"),       ("Forest_001.playerstart009b", "Forest10RightDoor")),
    "inner_forest_010":     (("Forest_001.playerstart010a", "Forest10CenterDoor"),      ("Forest_001.playerstart010b", "Forest18UpperLeftDoor")),
    "inner_forest_011":     (("Forest_001.playerstart011a", "Forest19LowerDoor"),       ("Forest_001.playerstart011b", "Forest18UpperRightDoor")),
    "inner_forest_012":     (("Forest_001.playerstart012a", "Forest07CenterDoor"),      ("Forest_001.playerstart012b", "Forest10UpperLeftDoor")),
    "inner_forest_014":     (("Forest_001.playerstart014a", "Forest09UpperRightDoor"),  ("Forest_001.playerstart014b", "Forest18LowerCenterDoor")),
    "inner_forest_015":     (("Forest_001.playerstart015a", "Forest01UpperDoor"),       ("Forest_001.playerstart015b", "Forest12LeftDoor")),
    "inner_forest_016":     (("Forest_001.playerstart016a", "Forest09LeftDoor"),        ("Forest_001.playerstart016b", "Forest04LowerLeftDoor")),
    "inner_forest_017":     (("Forest_001.playerstart017a", "Forest09CenterLeftDoor"),  ("Forest_001.playerstart017b", "Forest04LowerCenterLeftDoor")),
    "inner_forest_018":     (("Forest_001.playerstart018a", "Forest04UpperLeftDoor"),   ("Forest_001.playerstart018b", "Forest12LowerRightDoor")),
    "inner_forest_019":     (("Forest_001.playerstart019a", "Forest02LowerLeftDoor"),   ("Forest_001.playerstart019b", "Forest01RightDoor")),
    "inner_forest_020":     (("Forest_001.playerstart020a", "Forest05LeftDoor"),        ("Forest_001.playerstart020b", "Forest12UpperRightDoor")),
    "inner_forest_021":     (("Forest_001.playerstart021a", "Forest10LowerLeftDoor"),   ("Forest_001.playerstart021b", "Forest05RightDoor")),
    "inner_forest_022":     (("Forest_001.playerstart022a", "Forest19LeftDoor"),        ("Forest_001.playerstart022b", "Forest03UpperRightDoor")),
    "inner_forest_023":     (("Forest_001.playerstart023a", "Forest18CenterLeftDoor"),  ("Forest_001.playerstart023b", "Forest04UpperRightDoor")),
    "inner_forest_024":     (("Forest_001.playerstart024a", "Forest18LowerLeftDoor"),   ("Forest_001.playerstart024b", "Forest04LowerRightDoor")),
    "inner_garden_001":     (("Garden_001.playerstart001a", "Garden06UpperDoor"),       ("Garden_001.playerstart001b", "Garden07LowerDoor")),
    "inner_steet_001":      (("Street_001.playerstart001a", "Street03Door"),            ("Street_001.playerstart001b", "Street10Door")),
    "inner_steet_002":      (("Street_001.playerstart002a", "Street13Door"),            ("Street_001.playerstart002b", "Street12Door")),
    "inner_steet_003":      (("Street_001.playerstart003a", "Street01Door"),            ("Street_001.playerstart003b", "Street18Door")),
    "inner_summit_001":     (("Summit_001.playerstart001a", "Summit16CenterDoor"),      ("Summit_001.playerstart001b", "Summit24CenterDoor")),
    "inner_summit_002":     (("Summit_001.playerstart002a", "Summit08LeftDoor"),        ("Summit_001.playerstart002b", "Summit11CenterDoor")),
    "inner_summit_003":     (("Summit_001.playerstart003a", "Summit15CenterDoor"),      ("Summit_001.playerstart003b", "Summit08RightDoor")),
    "inner_summit_004":     (("Summit_001.playerstart004a", "Summit14CenterDoor"),      ("Summit_001.playerstart004b", "Summit20CenterDoor")),
    "inner_summit_005":     (("Summit_001.playerstart005a", "Summit06CenterDoor"),      ("Summit_001.playerstart005b", "Summit12LeftDoor")),
    "inner_summit_006":     (("Summit_001.playerstart006a", "Summit26CenterDoor"),      ("Summit_001.playerstart006b", "Summit30CenterDoor")),
    "inner_summit_007":     (("Summit_001.playerstart007a", "Summit12RightDoor"),       ("Summit_001.playerstart007b", "Summit17CenterDoor")),
    "kowloon_paradise_001": (("Kowloon_001.paradise001",    "Kowloon36Right"),          ("Paradise_001.kowloon001",    "Paradise01Left")),
    "kowloon_summit_001":   (("Kowloon_001.summit001",      "Kowloon04LeftDoor"),       ("Summit_001.kowloon001",      "Summit01RightDoor")),
    "labo_summit_001":      (("Labo_001.summit001",         "Labo18RightDoor"),         ("Summit_001.labo001",         "Summit19CenterDoor")),
    "quarry_roots_001":     (("Quarry_001.roots001",        "Quarry31Right"),           ("Roots_001.quarry001",        "Roots17Left")),
    "ruins_crossroad_001":  (("Crossroad_001.ruins001",     "Crossroad01Lower"),        ("Ruins_001.crossroad001",     "Ruins13Upper")),
    "ruins_quarry_001":     (("Ruins_001.quarry001",        "Ruins08Left"),             ("Quarry_001.ruins001",        "Quarry01Right")),
    "sewer_roots_001":      (("Sewer_001.roots001",         "Sewer09Left"),             ("Roots_001.sewer001",         "Roots06Right")),
    "sewer_swamp_001":      (("Sewer_001.swamp001",         "Sewer15Lower"),            ("Swamp_001.sewer001",         "Swamp18Upper")),
    "slum_sewer_001":       (("Sewer_001.slum001",          "Sewer01Upper"),            ("Slum_001.sewer001",          "Slum02Lower")),
    "slum_street_001":      (("Street_001.slum001",         "Street01Left"),            ("Slum_001.street001",         "Slum01Right")),
    "street_center_001":    (("Street_001.center001",       "Street11Upper"),           ("Center_001.street001",       "Center01Lower")),
    "street_tower_001":     (("Street_001.tower001",        "Street15Right"),           ("Tower_001.street001",        "Tower01Left")),
    "swamp_roots_001":      (("Swamp_001.roots001",         "Swamp10Left"),             ("Roots_001.swamp001",         "Roots25Right")),
    "swamp_tower_001":      (("Tower_001.swamp001",         "Tower18Lower"),            ("Swamp_001.tower001",         "Swamp01Upper")),
    "tower_forest_001":     (("Forest_001.tower001",        "Forest01Left"),            ("Tower_001.forest001",        "Tower17Right")),

# wrong in the game
#   "inner_kowloon_001":    (("Kowloon_001.playerstart001a", ""),                    ("Kowloon_001.playerstart001a", "")),
#   "tower_kowloon_001":    (("Tower_001.kowloon001",        ""),                    ("Kowloon_001.tower001",        "")),
#   "mine_factory_001":     (("Mine_001.factory001",         ""),                    ("Factory_001.mine001",         "")),
#   "inner_kowloon_002":    (("Kowloon_001.playerstart002a", ""),                        ("Kowloon_001.playerstart002b", "")),
#   "inner_kowloon_003":    (("Kowloon_001.playerstart003a", ""),                        ("Kowloon_001.playerstart003b", "")),
#   "inner_kowloon_004":    (("Kowloon_001.playerstart004a", ""),                        ("Kowloon_001.playerstart004b", "")),
#   "inner_kowloon_005":    (("Kowloon_001.playerstart005a", ""),                        ("Kowloon_001.playerstart005b", "")),
#   "inner_kowloon_007":    (("Kowloon_001.playerstart007a", ""),                        ("Kowloon_001.playerstart007b", "")),
})


def disconnect_entrances(world: "EnderMagnoliaWorld") -> None:
    for region in transitions.region_spawn:
        entrance = world.get_entrance(region)
        entrance.randomization_type = EntranceType.TWO_WAY
        disconnect_entrance_for_randomization(entrance)


def shuffle_transitions(world: "EnderMagnoliaWorld") -> ERPlacementState:
    coupled = world.options.shuffle_transitions == ShuffleTransitions.option_coupled
    return randomize_entrances(world, coupled, {0: [0]})


def spawn_redirects(world: "EnderMagnoliaWorld") -> Dict[str, str]:
    return {transitions.vanilla_spawn(region):
            transitions.region_spawn[world.get_entrance(region).connected_region.name]
            for region in transitions.region_spawn}
