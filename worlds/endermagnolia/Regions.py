from typing import List

from worlds.endermagnolia import event_locations
from .Locations import LocationData, locations


class ExitData:
    name: str
    destination: str

    def __init__(self, name, destination):
        self.name = name
        self.destination = destination


class RegionData:

    def __init__(self, name, content: List[LocationData | ExitData] = []):
        self.name = name
        self.locations = [
            location for location in content if isinstance(location ,LocationData)]
        self.connections = [
            connection for connection in content if isinstance(connection, ExitData)]
        assert len(content) == len(self.connections) + len(self.locations), f"Wrong element in region content ({name})"

ruins_regions: List[RegionData] = [
    RegionData(
        "Menu",
        [
            event_locations["Goal"],
            ExitData("Start", "Ruins 14"),
        ]
    ),
    RegionData(
        "Ruins 1",
        [
            ExitData("Ruins 1 to Ruins 2", "Ruins 2"),
            ExitData("Ruins 1 to Ruins 15", "Ruins 15"),
        ]
    ),
    RegionData(
        "Ruins 2",
        [
            ExitData("Ruins 2 to Ruins 1", "Ruins 1"),
            ExitData("Ruins 2 to Ruins 9", "Ruins 9"),
            ExitData("Ruins 2 to Ruins 7", "Ruins 7"),
            ExitData("Ruins 2 to Ruins 3", "Ruins 3"),
        ]
    ),
    RegionData(
        "Ruins 3",
        [
            ExitData("Ruins 3 to Ruins 2", "Ruins 2"),
            ExitData("Ruins 3 to Ruins 4", "Ruins 4"),
        ]
    ),
    RegionData(
        "Ruins 4",
        [
            locations["Ruins 4 - Nola"],
            ExitData("Ruins 4 to Ruins 5", "Ruins 5"),
        ]
    ),
    RegionData(
        "Ruins 5",
        [
            locations["Ruins 5 - Charmed Fragment"],
            ExitData("Ruins 5 to Ruins 4", "Ruins 4"),
            ExitData("Ruins 5 to Ruins 6", "Ruins 6"),
        ]
    ),
    RegionData(
        "Ruins 6",
        [
            ExitData("Ruins 6 to Ruins 5", "Ruins 5"),
            ExitData("Ruins 6 to Ruins 7", "Ruins 7"),
        ]
    ),
    RegionData(
        "Ruins 7",
        [
            event_locations["Ruins 7 - Lever"],
            ExitData("Ruins 7 to Ruins 6", "Ruins 6"),
            ExitData("Ruins 7 to Ruins 2", "Ruins 2"),
            ExitData("Ruins 7 to Ruins 8", "Ruins 8"),
        ]
    ),
    RegionData(
        "Ruins 8",
        [
            ExitData("Ruins 8 to Ruins 7", "Ruins 7"),
        ]
    ),
    RegionData(
        "Ruins 9",
        [
            ExitData("Ruins 9 to Ruins 2", "Ruins 2"),
            ExitData("Ruins 9 to Ruins 10", "Ruins 10"),
        ]
    ),
    RegionData(
        "Ruins 10",
        [
            ExitData("Ruins 10 to Ruins 9", "Ruins 9"),
            ExitData("Ruins 10 to Ruins 11", "Ruins 11"),
            ExitData("Ruins 10 to Ruins 13", "Ruins 13"),
        ]
    ),
    RegionData(
        "Ruins 11",
        [
            ExitData("Ruins 11 to Ruins 10", "Ruins 10"),
            ExitData("Ruins 11 to Ruins 12", "Ruins 12"),
        ]
    ),
    RegionData(
        "Ruins 12",
        [
            locations["Ruins 12 - Subterranean Testing Site Key"],
            locations["Ruins 12 - Lito"],
            ExitData("Ruins 12 to Ruins 11", "Ruins 11"),
        ]
    ),
    RegionData(
        "Ruins 13",
        [
            locations["Ruins 13 - Homunculus Research Log 1"],
            ExitData("Ruins 13 to Ruins 10", "Ruins 10"),
            ExitData("Ruins 13 to Crossroad 1", "Crossroad 1")
        ]
    ),
    RegionData(
        "Ruins 14",
        [
            locations["Ruins 14 - Worn Experiment Log"],
            ExitData("Ruins 14 to Ruins 16", "Ruins 16"),
        ]
    ),
    RegionData(
        "Ruins 15",
        [
            locations["Ruins 15 - Healing Ward"],
            ExitData("Ruins 15 to Ruins 16", "Ruins 16"),
            ExitData("Ruins 15 to Ruins 1", "Ruins 1"),
        ]
    ),
    RegionData(
        "Ruins 16",
        [
            ExitData("Ruins 16 to Ruins 15", "Ruins 15"),
            ExitData("Ruins 16 to Ruins 14", "Ruins 14"),
        ]
    ),
]

crossroad_regions: List[RegionData] = [
    RegionData(
        "Crossroad 1",
        [
            ExitData("Crossroad 1 to Crossroad 4", "Crossroad 4"),
            ExitData("Crossroad 1 to Ruins 13", "Ruins 13")
        ]
    ),
    RegionData(
        "Crossroad 2",
        [
            locations["Crossroad 2 - Charmed Fragment"],
            ExitData("Crossroad 2 to Crossroad 5", "Crossroad 5"),
            ExitData("Crossroad 2 to Slum 1", "Slum 1")
        ]
    ),
    RegionData(
        "Crossroad 3",
        [
            ExitData("Crossroad 3 to Crossroad 4", "Crossroad 4"),
        ]
    ),
    RegionData(
        "Crossroad 4",
        [
            ExitData("Crossroad 4 to Crossroad 1", "Crossroad 1"),
            ExitData("Crossroad 4 to Crossroad 3", "Crossroad 3"),
            ExitData("Crossroad 4 to Crossroad 5", "Crossroad 5"),
        ]
    ),
    RegionData(
        "Crossroad 5",
        [
            locations["Crossroad 5 - Aerial Jump"],
            locations["Crossroad 5 - Dodge"],
            ExitData("Crossroad 5 to Crossroad 4", "Crossroad 4"),
            ExitData("Crossroad 5 to Crossroad 2", "Crossroad 2"),
        ]
    ),
]

slum_regions: List[RegionData] = [
    RegionData(
        "Slum 1",
        [
            locations["Slum 1 - Tattered Letter"],
            ExitData("Slum 1 to Crossroad 2", "Crossroad 2")
        ]
    )
]

regions: List[RegionData] = [
    *ruins_regions,
    *crossroad_regions,
    *slum_regions
]
