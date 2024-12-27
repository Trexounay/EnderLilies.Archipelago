from typing import List, Dict

class StartingLocationData():
    clientKey: str
    earlyManeuverItems: List[str]

    def __init__(self, clientKey: str, earlyManeuverItems: List[str]):
        self.clientKey = clientKey
        self.earlyManeuverItems = earlyManeuverItems
        if "LEDGE" in earlyManeuverItems:
            self.earlyManeuverItems.remove("LEDGE")
            self.earlyManeuverItems.extend(["djump", "silva", "champion"])
        # For random seed determinism
        self.earlyManeuverItems.sort()

startingLocationsData : Dict[int, StartingLocationData] = {
    0   : StartingLocationData("Start",              ["LEDGE", "claw"]),
    3   : StartingLocationData("Cellar",             ["LEDGE", "claw"]),
    5   : StartingLocationData("CathedralCloister",  ["LEDGE", "claw"]),
    9   : StartingLocationData("SaintsPassage",      ["LEDGE", "claw"]),
    12  : StartingLocationData("Crossroads",         ["LEDGE", "claw"]),
    19  : StartingLocationData("CollapsedShack",     ["LEDGE", "hook"]),
    23  : StartingLocationData("BridgeHead",         ["swim"]),
    35  : StartingLocationData("RuinedCastleCellar", ["LEDGE", "claw"]),
    38  : StartingLocationData("GuestChamber",       ["LEDGE", "claw"]),
    41  : StartingLocationData("MaelstromRemparts",  ["claw"]),
    55  : StartingLocationData("BastionGates",       ["LEDGE", "sinner"]),
    61  : StartingLocationData("Courtyard",          ["LEDGE"]),
    62  : StartingLocationData("SecondSpireChamber", ["LEDGE"]),
    68  : StartingLocationData("MonumentOfTheWindStart", ["LEDGE"]),
    72  : StartingLocationData("MourningHall",       ["claw"]),
    78  : StartingLocationData("DryadLake",          ["LEDGE", "claw"]),
    83  : StartingLocationData("WitchsHermitage",    ["LEDGE"]),
    87  : StartingLocationData("CovenHalls",         ["LEDGE"]),
    91  : StartingLocationData("BottomOfTheWell",    ["claw"]),
    93  : StartingLocationData("Charnel",            ["claw"]),
    103 : StartingLocationData("Ossuary",            ["LEDGE", "claw", "sinner"]),
    106 : StartingLocationData("GreatHall",          ["claw"]),
    115 : StartingLocationData("Aqueduct",           ["LEDGE", "claw", "swim"]),
    123 : StartingLocationData("Cells",              ["swim"]),
    132 : StartingLocationData("DarkChamber",        ["hook"]),
    138 : StartingLocationData("ExecutionGrounds",   ["hook"]),
    145 : StartingLocationData("Lab1",               ["swim"]),
    150 : StartingLocationData("Lab2",               ["LEDGE"]),
}
