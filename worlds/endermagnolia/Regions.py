from dataclasses import dataclass
from typing import Dict, List

from worlds.endermagnolia import event_locations
from .Locations import LocationData, locations


class ExitData:
    name: str
    destination: str

    def __init__(self, name, destination):
        self.name = name
        self.destination = destination

@dataclass
class RegionData:
    name : str
    connections: List[ExitData]

room_connections = {
    "Center 1": [
        ("Center01LeftDoor", "Center05CenterDoor"),
        ("Center01Lower",    "Street11Upper"),
        ("Center01LowerLeft", "Center02LowerRight"),
        ("Center01RightDoor", "Center04RightDoor"),
        ("Center01UpperLeft", "Center02UpperRight"),
    ],
    "Center 2": [
        ("Center02LowerRight", "Center01LowerLeft"),
        ("Center02UpperRight", "Center01UpperLeft"),
    ],
    "Center 3": [
        ("Center03CenterLeftDoor", "Center05LeftDoor"),
        ("Center03CenterRightDoor", "Center05RightDoor"),
        ("Center03LeftDoor", "Garden12RightDoor"),
        ("Center03RightDoor", "Kowloon01LeftDoor"),
    ],
    "Center 4": [
        ("Center04Left", "Center05Right"),
        ("Center04RightDoor", "Center01RightDoor"),
    ],
    "Center 5": [
        ("Center05CenterDoor", "Center01LeftDoor"),
        ("Center05LeftDoor", "Center03CenterLeftDoor"),
        ("Center05Right", "Center04Left"),
        ("Center05RightDoor", "Center03CenterRightDoor"),
    ],
    "Center 19": [
        ("Center19Right", "Summit08Left"),
    ],
    "Crossroad 1": [
        ("Crossroad01Lower", "Ruins13Upper"),
        ("Crossroad01Right", "Crossroad04LowerLeft"),
    ],
    "Crossroad 2": [
        ("Crossroad02Left", "Crossroad05Right"),
        ("Crossroad02Right", "Slum01Left"),
    ],
    "Crossroad 3": [
        ("Crossroad03Left", "Mine01Right"),
        ("Crossroad03Right", "Crossroad04UpperLeft"),
    ],
    "Crossroad 4": [
        ("Crossroad04LowerLeft", "Crossroad01Right"),
        ("Crossroad04Right", "Crossroad05Left"),
        ("Crossroad04UpperLeft", "Crossroad03Right"),
    ],
    "Crossroad 5": [
        ("Crossroad05Left", "Crossroad04Right"),
        ("Crossroad05Right", "Crossroad02Left"),
    ],
    "Estate 1": [
        ("Estate01Left", "Estate07UpperRight"),
        ("Estate01Lower", "Estate08Upper"),
        ("Estate01Right", "Estate02Left"),
    ],
    "Estate 2": [
        ("Estate02Left", "Estate01Right"),
        ("Estate02LowerRight", "Estate03CenterLeft"),
        ("Estate02Upper", "Estate05Lower"),
        ("Estate02UpperRight", "Estate03UpperLeft"),
    ],
    "Estate 3": [
        ("Estate03CenterLeft", "Estate02LowerRight"),
        ("Estate03HiddenRight", "Estate04Left"),
        ("Estate03LowerLeft", "Estate06Right"),
        ("Estate03UpperLeft", "Estate02UpperRight"),
    ],
    "Estate 4": [
        ("Estate04Left", "Estate03HiddenRight"),
    ],
    "Estate 5": [
        ("Estate05Lower", "Estate02Upper"),
    ],
    "Estate 6": [
        ("Estate06Lower", "Estate09Upper"),
        ("Estate06Right", "Estate03LowerLeft"),
    ],
    "Estate 7": [
        ("Estate07Lower", "Estate12Upper"),
        ("Estate07LowerRight", "Estate08Left"),
        ("Estate07UpperRight", "Estate01Left"),
    ],
    "Estate 8": [
        ("Estate08Left", "Estate07LowerRight"),
        ("Estate08Right", "Estate09UpperLeft"),
        ("Estate08Upper", "Estate01Lower"),
    ],
    "Estate 9": [
        ("Estate09HiddenRight", "Estate10Left"),
        ("Estate09LowerLeft", "Estate11Right"),
        ("Estate09Upper", "Estate06Lower"),
        ("Estate09UpperLeft", "Estate08Right"),
    ],
    "Estate 10": [
        ("Estate10Left", "Estate09HiddenRight"),
    ],
    "Estate 11": [
        ("Estate11Left", "Estate12Right"),
        ("Estate11Right", "Estate09LowerLeft"),
    ],
    "Estate 12": [
        ("Estate12Left", "Forest09LowerRight"),
        ("Estate12Right", "Estate11Left"),
        ("Estate12Upper", "Estate07Lower"),
    ],
    "Factory 1": [
        ("Factory01Left", "Factory02UpperRight"),
    ],
    "Factory 2": [
        ("Factory02HiddenCenterRight", "Factory19UpperLeft"),
        ("Factory02LowerLeft", "Factory04Right"),
        ("Factory02LowerRight", "Factory19LowerLeft"),
        ("Factory02UpperCenterRight", "Factory03Left"),
        ("Factory02UpperLeft", "Factory05Right"),
        ("Factory02UpperRight", "Factory01Left"),
    ],
    "Factory 3": [
        ("Factory03Left", "Factory02UpperCenterRight"),
        ("Factory03Right", "Garden14Left"),
    ],
    "Factory 4": [
        ("Factory04Left", "Factory06Right"),
        ("Factory04Right", "Factory02LowerLeft"),
    ],
    "Factory 5": [
        ("Factory05Left", "Factory09Right"),
        ("Factory05Right", "Factory02UpperLeft"),
        ("Factory05Upper", "Factory12Lower"),
    ],
    "Factory 6": [
        ("Factory06LowerLeft", "Factory10Right"),
        ("Factory06Right", "Factory04Left"),
        ("Factory06Upper", "Factory09Lower"),
        ("Factory06UpperLeft", "Factory07Right"),
    ],
    "Factory 7": [
        ("Factory07Left", "Factory08UpperRight"),
        ("Factory07Right", "Factory06UpperLeft"),
    ],
    "Factory 8": [
        ("Factory08LowerRight", "Factory10Left"),
        ("Factory08UpperRight", "Factory07Left"),
    ],
    "Factory 9": [
        ("Factory09Lower", "Factory06Upper"),
        ("Factory09Right", "Factory05Left"),
        ("Factory09Upper", "Factory11Lower"),
    ],
    "Factory 10": [
        ("Factory10Left", "Factory08LowerRight"),
        ("Factory10Right", "Factory06LowerLeft"),
    ],
    "Factory 11": [
        ("Factory11Lower", "Factory09Upper"),
        ("Factory11Right", "Factory12Left"),
    ],
    "Factory 12": [
        ("Factory12Left", "Factory11Right"),
        ("Factory12Lower", "Factory05Upper"),
        ("Factory12Right", "Factory13LowerLeft"),
        ("Factory12Upper", "Factory15Lower"),
    ],
    "Factory 13": [
        ("Factory13LowerLeft", "Factory12Right"),
        ("Factory13Right", "Factory14Left"),
        ("Factory13UpperLeft", "Factory15Right"),
    ],
    "Factory 14": [
        ("Factory14Left", "Factory13Right"),
    ],
    "Factory 15": [
        ("Factory15Lower", "Factory12Upper"),
        ("Factory15LowerLeft", "Factory21Right"),
        ("Factory15Right", "Factory13UpperLeft"),
        ("Factory15UpperLeft", "Factory16Right"),
    ],
    "Factory 16": [
        ("Factory16Left", "Factory17Right"),
        ("Factory16Right", "Factory15UpperLeft"),
    ],
    "Factory 17": [
        ("Factory17LowerLeft", "Factory18UpperLeft"),
        ("Factory17LowerRight", "Factory18UpperRight"),
        ("Factory17Right", "Factory16Left"),
    ],
    "Factory 18": [
        ("Factory18UpperLeft", "Factory17LowerLeft"),
        ("Factory18UpperRight", "Factory17LowerRight"),
    ],
    "Factory 19": [
        ("Factory19LowerLeft", "Factory02LowerRight"),
        ("Factory19UpperLeft", "Factory02HiddenCenterRight"),
    ],
    "Factory 21": [
        ("Factory21Right", "Factory15LowerLeft"),
    ],
    "Forest 1": [
        ("Forest01Left", "Tower17Right"),
        ("Forest01RightDoor", "Forest02LowerLeftDoor"),
        ("Forest01UpperDoor", "Forest12LeftDoor"),
    ],
    "Forest 2": [
        ("Forest02LowerDoor", "Forest04UpperCenterDoor"),
        ("Forest02LowerLeftDoor", "Forest01RightDoor"),
        ("Forest02Right", "Forest03Left"),
        ("Forest02UpperLeftDoor", "Forest06CenterDoor"),
        ("Forest02UpperRightDoor", "Forest05CenterLowerDoor"),
    ],
    "Forest 3": [
        ("Forest03Left", "Forest02Right"),
        ("Forest03LowerRightDoor", "Forest09CenterRightDoor"),
        ("Forest03UpperDoor", "Forsest07LowerDoor"),
        ("Forest03UpperRightDoor", "Forest19LeftDoor"),
    ],
    "Forest 4": [
        ("Forest04LowerCenterLeftDoor", "Forest09CenterLeftDoor"),
        ("Forest04LowerCenterRightDoor", "Forest09CenterDoor"),
        ("Forest04LowerLeftDoor", "Forest09LeftDoor"),
        ("Forest04LowerRightDoor", "Forest18LowerLeftDoor"),
        ("Forest04UpperCenterDoor", "Forest02LowerDoor"),
        ("Forest04UpperLeftDoor", "Forest12LowerRightDoor"),
        ("Forest04UpperRightDoor", "Forest18CenterLeftDoor"),
    ],
    "Forest 5": [
        ("Forest05CenterLowerDoor", "Forest02UpperRightDoor"),
        ("Forest05CenterUpperDoor", "Forest06CenterDoor"),
        ("Forest05LeftDoor", "Forest12UpperRightDoor"),
        ("Forest05RightDoor", "Forest10LowerLeftDoor"),
    ],
    "Forest 6": [
        ("Forest06CenterDoor", "Forest02UpperLeftDoor"),
        ("Forest06HiddenRight", "Forest07Left"),
        ("Forest06Left", "Forest11Right"),
        ("Forest06LowerLeftDoor", "Forest12UpperDoor"),
        ("Forest06LowerRightDoor", "Forest05CenterUpperDoor"),
    ],
    "Forest 7": [
        ("Forest07CenterDoor", "Forest10UpperLeftDoor"),
        ("Forest07Left", "Forest06HiddenRight"),
        ("Forest07Right", "Forest08Left"),
    ],
    "Forest 8": [
        ("Forest08Left", "Forest07Right"),
        ("Forest08LowerDoor", "Forest10RightDoor"),
    ],
    "Forest 9": [
        ("Forest09CenterDoor", "Forest04LowerCenterRightDoor"),
        ("Forest09CenterLeftDoor", "Forest04LowerCenterLeftDoor"),
        ("Forest09CenterRightDoor", "Forest03LowerRightDoor"),
        ("Forest09LeftDoor", "Forest04LowerLeftDoor"),
        ("Forest09LowerRight", "Estate12Left"),
        ("Forest09UpperRightDoor", "Forest18LowerCenterDoor"),
    ],
    "Forest 10": [
        ("Forest10CenterDoor", "Forest18UpperLeftDoor"),
        ("Forest10LowerLeftDoor", "Forest05RightDoor"),
        ("Forest10RightDoor", "Forest08LowerDoor"),
        ("Forest10UpperLeftDoor", "Forest07CenterDoor"),
    ],
    "Forest 11": [
        ("Forest11Right", "Forest06Left"),
    ],
    "Forest 12": [
        ("Forest12LeftDoor", "Forest01UpperDoor"),
        ("Forest12LowerRightDoor", "Forest04UpperLeftDoor"),
        ("Forest12UpperDoor", "Forest06LowerLeftDoor"),
        ("Forest12UpperRightDoor", "Forest05LeftDoor"),
    ],
    "Forest 18": [
        ("Forest18CenterLeftDoor", "Forest04UpperRightDoor"),
        ("Forest18LowerCenterDoor", "Forest09UpperRightDoor"),
        ("Forest18LowerLeftDoor", "Forest04LowerRightDoor"),
        ("Forest18UpperLeftDoor", "Forest10CenterDoor"),
        ("Forest18UpperRightDoor", "Forest19LowerDoor"),
    ],
    "Forest 19": [
        ("Forest19LeftDoor", "Forest18UpperRightDoor"),
        ("Forest19LowerDoor", "Forest03UpperRightDoor"),
        ("Forest19Right", "Forest20Left"),
    ],
    "Forest 20": [
        ("Forest20Left", "Forest19Right"),
        ("Forest20Right", "Forest21Left"),
    ],
    "Forest 21": [
        ("Forest21Left", "Forest20Right"),
        ("Forest21Right", "Forest22Left"),
    ],
    "Forest 22": [
        ("Forest22Left", "Forest21Right"),
        ("Forest22Right", "Forest23Left"),
    ],
    "Forest 23": [
        ("Forest23Left", "Forest22Right"),
    ],
    "Forsest 7": [
        ("Forsest07LowerDoor", "Forest04UpperCenterDoor"),
    ],
    "Garden 1": [
        ("Garden01Left", "Garden09Right"),
        ("Garden01Right", "Garden12Left"),
    ],
    "Garden 2": [
        ("Garden02Left", "Garden04Right"),
        ("Garden02LowerLeft", "Garden03UpperLeft"),
        ("Garden02LowerRight", "Garden03UpperRight"),
        ("Garden02Right", "Garden09Left"),
    ],
    "Garden 3": [
        ("Garden03LeftLower", "Garden14Right"),
        ("Garden03LeftUpper", "Garden13Right"),
        ("Garden03UpperLeft", "Garden02LowerLeft"),
        ("Garden03UpperRight", "Garden02LowerRight"),
    ],
    "Garden 4": [
        ("Garden04Left", "Garden05Right"),
        ("Garden04Right", "Garden02Left"),
    ],
    "Garden 5": [
        ("Garden05Left", "Garden06Right"),
        ("Garden05Right", "Garden04Left"),
    ],
    "Garden 6": [
        ("Garden06Left", "Garden08Right"),
        ("Garden06Right", "Garden05Left"),
        ("Garden06UpperDoor", "Garden07LowerDoor"),
    ],
    "Garden 7": [
        ("Garden07LowerDoor", "Garden06UpperDoor"),
        ("Garden07Upper", "Garden10Lower"),
    ],
    "Garden 8": [
        ("Garden08Right", "Garden06Left"),
        ("Garden08Upper", "Labo06Lower"),
    ],
    "Garden 9": [
        ("Garden09Left", "Garden02Right"),
        ("Garden09Right", "Garden01Left"),
    ],
    "Garden 10": [
        ("Garden10Left", "Garden11Right"),
        ("Garden10Lower", "Garden07Upper"),
    ],
    "Garden 11": [
        ("Garden11Right", "Garden10Left"),
    ],
    "Garden 12": [
        ("Garden12Left", "Garden01Right"),
        ("Garden12RightDoor", "Center03LeftDoor"),
    ],
    "Garden 13": [
        ("Garden13Right", "Garden03LeftUpper"),
    ],
    "Garden 14": [
        ("Garden14Left", "Factory03Right"),
        ("Garden14Right", "Garden03LeftLower"),
    ],
    "Kowloon 1": [
        ("Kowloon01LeftDoor", "Center03RightDoor"),
        ("Kowloon01Right", "Kowloon02LowerLeft"),
    ],
    "Kowloon 2": [
        ("Kowloon02CenterRight", "Kowloon05LowerLeft"),
        ("Kowloon02LowerLeft", "Kowloon01Right"),
        ("Kowloon02LowerRight", "Kowloon03Left"),
        ("Kowloon02UpperLeft", "Kowloon39LowerRight"),
        ("Kowloon02UpperRight", "Kowloon05UpperLeft"),
    ],
    "Kowloon 3": [
        ("Kowloon03Left", "Kowloon02LowerRight"),
        ("Kowloon03Right", "Kowloon06LowerLeft"),
    ],
    "Kowloon 4": [
        ("Kowloon04LeftDoor", "Summit01RightDoor"),
        ("Kowloon04Right", "Kowloon43Left"),
    ],
    "Kowloon 5": [
        ("Kowloon05LowerLeft", "Kowloon02CenterRight"),
        ("Kowloon05Right", "Kowloon06UpperLeft"),
        ("Kowloon05UpperLeft", "Kowloon02UpperRight"),
    ],
    "Kowloon 6": [
        ("Kowloon06CenterRight", "Kowloon08Left"),
        ("Kowloon06LowerLeft", "Kowloon03Right"),
        ("Kowloon06LowerRight", "Kowloon07Left"),
        ("Kowloon06UpperLeft", "Kowloon05Right"),
        ("Kowloon06UpperRight", "Kowloon16Left"),
    ],
    "Kowloon 7": [
        ("Kowloon07Left", "Kowloon06LowerRight"),
        ("Kowloon07Lower", "Kowloon09Upper"),
        ("Kowloon07Right", "Kowloon10Left"),
    ],
    "Kowloon 8": [
        ("Kowloon08Left", "Kowloon06CenterRight"),
        ("Kowloon08Right", "Kowloon15CenterLeft"),
    ],
    "Kowloon 9": [
        ("Kowloon09HiddenRight", "Kowloon14Left"),
        ("Kowloon09Upper", "Kowloon07Lower"),
    ],
    "Kowloon 10": [
        ("Kowloon10Left", "Kowloon07Right"),
        ("Kowloon10Lower", "Kowloon13UpperLeft"),
        ("Kowloon10Right", "Kowloon15LowerLeft"),
    ],
    "Kowloon 13": [
        ("Kowloon13HiddenLower", "Kowloon14HiddenUpper"),
        ("Kowloon13UpperLeft", "Kowloon10Lower"),
        ("Kowloon13UpperRight", "Kowloon15Lower"),
    ],
    "Kowloon 14": [
        ("Kowloon14HiddenUpper", "Kowloon13HiddenLower"),
        ("Kowloon14Left", "Kowloon09HiddenRight"),
    ],
    "Kowloon 15": [
        ("Kowloon15CenterLeft", "Kowloon08Right"),
        ("Kowloon15Lower", "Kowloon13UpperRight"),
        ("Kowloon15LowerLeft", "Kowloon10Right"),
        ("Kowloon15LowerRight", "Kowloon18Left"),
        ("Kowloon15UpperLeft", "Kowloon16Right"),
        ("Kowloon15UpperRight", "Kowloon21LowerLeft"),
    ],
    "Kowloon 16": [
        ("Kowloon16Left", "Kowloon06UpperRight"),
        ("Kowloon16Right", "Kowloon15UpperLeft"),
        ("Kowloon16Upper", "Kowloon23Lower"),
    ],
    "Kowloon 18": [
        ("Kowloon18Left", "Kowloon15LowerRight"),
    ],
    "Kowloon 21": [
        ("Kowloon21LowerLeft", "Kowloon15UpperRight"),
        ("Kowloon21UpperLeft", "Kowloon24Right"),
    ],
    "Kowloon 23": [
        ("Kowloon23Lower", "Kowloon16Upper"),
        ("Kowloon23Upper", "Kowloon24Lower"),
    ],
    "Kowloon 24": [
        ("Kowloon24Left", "Kowloon25Right"),
        ("Kowloon24Lower", "Kowloon23Upper"),
        ("Kowloon24Right", "Kowloon21UpperLeft"),
        ("Kowloon24Upper", "Kowloon30Lower"),
    ],
    "Kowloon 25": [
        ("Kowloon25Left", "Kowloon26Right"),
        ("Kowloon25Right", "Kowloon24Left"),
    ],
    "Kowloon 26": [
        ("Kowloon26Left", "Kowloon38LowerRight"),
        ("Kowloon26Right", "Kowloon25Left"),
    ],
    "Kowloon 28": [
        ("Kowloon28Left", "Kowloon47Right"),
        ("Kowloon28Right", "Kowloon34UpperLeft"),
    ],
    "Kowloon 29": [
        ("Kowloon29Left", "Kowloon30LowerRight"),
    ],
    "Kowloon 30": [
        ("Kowloon30CenterLeft", "Kowloon41UpperRight"),
        ("Kowloon30CenterRight", "Kowloon33Left"),
        ("Kowloon30Lower", "Kowloon24Upper"),
        ("Kowloon30LowerLeft", "Kowloon41LowerRight"),
        ("Kowloon30LowerRight", "Kowloon29Left"),
        ("Kowloon30UpperLeft", "Kowloon31Right"),
        ("Kowloon30UpperRight", "Kowloon32Left"),
    ],
    "Kowloon 31": [
        ("Kowloon31Right", "Kowloon30UpperLeft"),
    ],
    "Kowloon 32": [
        ("Kowloon32Left", "Kowloon30UpperRight"),
    ],
    "Kowloon 33": [
        ("Kowloon33Left", "Kowloon30CenterRight"),
        ("Kowloon33Right", "Kowloon34LowerLeft"),
    ],
    "Kowloon 34": [
        ("Kowloon34CenterLeft", "Kowloon46Right"),
        ("Kowloon34LowerLeft", "Kowloon33Right"),
        ("Kowloon34Right", "Kowloon35Left"),
        ("Kowloon34UpperLeft", "Kowloon28Right"),
    ],
    "Kowloon 35": [
        ("Kowloon35CenterLowerRight", "Kowloon48Right"),
        ("Kowloon35CenterRight", "Kowloon49Left"),
        ("Kowloon35CenterUpperRight", "Kowloon50Left"),
        ("Kowloon35Left", "Kowloon34Right"),
        ("Kowloon35LowerRight", "Kowloon37Left"),
        ("Kowloon35UpperRight", "Kowloon51Left"),
    ],
    "Kowloon 36": [
        ("Kowloon36CenterLeft", "Kowloon49Right"),
        ("Kowloon36CenterLowerLeft", "Kowloon48Right"),
        ("Kowloon36CenterUpperLeft", "Kowloon50Right"),
        ("Kowloon36LowerLeft", "Kowloon37Right"),
        ("Kowloon36Right", "Paradise01Left"),
        ("Kowloon36UpperLeft", "Kowloon51Right"),
    ],
    "Kowloon 37": [
        ("Kowloon37Left", "Kowloon35LowerRight"),
        ("Kowloon37Right", "Kowloon36LowerLeft"),
    ],
    "Kowloon 38": [
        ("Kowloon38CenterRight", "Kowloon44Left"),
        ("Kowloon38Left", "Kowloon40Right"),
        ("Kowloon38LowerRight", "Kowloon26Left"),
        ("Kowloon38UpperRight", "Kowloon42Left"),
    ],
    "Kowloon 39": [
        ("Kowloon39LowerRight", "Kowloon02UpperLeft"),
        ("Kowloon39UpperRight", "Kowloon40Left"),
    ],
    "Kowloon 40": [
        ("Kowloon40Left", "Kowloon39UpperRight"),
        ("Kowloon40Right", "Kowloon38Left"),
    ],
    "Kowloon 41": [
        ("Kowloon41LowerRight", "Kowloon30LowerLeft"),
        ("Kowloon41UpperRight", "Kowloon30CenterLeft"),
    ],
    "Kowloon 42": [
        ("Kowloon42Left", "Kowloon38UpperRight"),
        ("Kowloon42Upper", "Kowloon43Lower"),
    ],
    "Kowloon 43": [
        ("Kowloon43Left", "Kowloon04Right"),
        ("Kowloon43Lower", "Kowloon42Upper"),
    ],
    "Kowloon 44": [
        ("Kowloon44Left", "Kowloon38CenterRight"),
        ("Kowloon44Right", "Kowloon45Left"),
    ],
    "Kowloon 45": [
        ("Kowloon45Left", "Kowloon44Right"),
        ("Kowloon45Right", "Kowloon46Left"),
        ("Kowloon45Upper", "Kowloon47Lower"),
    ],
    "Kowloon 46": [
        ("Kowloon46Left", "Kowloon45Right"),
        ("Kowloon46Right", "Kowloon34CenterLeft"),
    ],
    "Kowloon 47": [
        ("Kowloon47Lower", "Kowloon45Upper"),
        ("Kowloon47Right", "Kowloon28Left"),
    ],
    "Kowloon 48": [
        ("Kowloon48Left", "Kowloon35CenterLowerRight"),
        ("Kowloon48Right", "Kowloon36CenterLowerLeft"),
    ],
    "Kowloon 49": [
        ("Kowloon49Left", "Kowloon35CenterRight"),
        ("Kowloon49Right", "Kowloon36CenterLeft"),
    ],
    "Kowloon 50": [
        ("Kowloon50Left", "Kowloon35CenterUpperRight"),
        ("Kowloon50Right", "Kowloon36CenterUpperLeft"),
    ],
    "Kowloon 51": [
        ("Kowloon51Left", "Kowloon35UpperRight"),
        ("Kowloon51Right", "Kowloon36UpperLeft"),
    ],
    "Labo 1": [
        ("Labo01Left", "Labo02Right"),
        ("Labo01Right", "Labo03Left"),
        ("Labo01Upper", "Labo09Lower"),
    ],
    "Labo 2": [
        ("Labo02Right", "Labo01Left"),
    ],
    "Labo 3": [
        ("Labo03Left", "Labo01Right"),
        ("Labo03Right", "Labo14LowerLeft"),
    ],
    "Labo 4": [
        ("Labo04Right", "Labo14UpperLeft"),
        ("Labo04Upper", "Labo05Lower"),
    ],
    "Labo 5": [
        ("Labo05Lower", "Labo04Upper"),
        ("Labo05LowerLeft", "Labo09LowerRight"),
        ("Labo05LowerRight", "Labo08LowerLeft"),
        ("Labo05Upper", "Labo20Lower"),
        ("Labo05UpperLeft", "Labo09UpperRight"),
        ("Labo05UpperRight", "Labo08CenterLeft"),
    ],
    "Labo 6": [
        ("Labo06CenterLeft", "Labo15Right"),
        ("Labo06Lower", "Garden08Upper"),
        ("Labo06LowerLeft", "Labo07Right"),
        ("Labo06Upper", "Labo19LowerRight"),
        ("Labo06UpperLeft", "Labo24Right"),
    ],
    "Labo 7": [
        ("Labo07Left", "Labo08LowerRight"),
        ("Labo07Right", "Labo06LowerLeft"),
        ("Labo07Upper", "Labo16Lower"),
    ],
    "Labo 8": [
        ("Labo08CenterLeft", "Labo05UpperRight"),
        ("Labo08CenterRight", "Labo16Left"),
        ("Labo08Lower", "Labo14Upper"),
        ("Labo08LowerLeft", "Labo05LowerRight"),
        ("Labo08LowerRight", "Labo07Left"),
        ("Labo08Upper", "Labo19LowerLeft"),
        ("Labo08UpperLeft", "Labo26Right"),
        ("Labo08UpperRight", "Labo24Left"),
    ],
    "Labo 9": [
        ("Labo09Left", "Labo10LowerRight"),
        ("Labo09Lower", "Labo02Right"),
        ("Labo09LowerRight", "Labo05LowerLeft"),
        ("Labo09Upper", "Labo23Lower"),
        ("Labo09UpperRight", "Labo05UpperLeft"),
    ],
    "Labo 10": [
        ("Labo10Left", "Labo25Right"),
        ("Labo10LowerRight", "Labo09Left"),
        ("Labo10Right", "Labo23Left"),
        ("Labo10UpperRight", "Labo11Left"),
    ],
    "Labo 11": [
        ("Labo11Left", "Labo10UpperRight"),
        ("Labo11LowerRight", "Labo26Left"),
        ("Labo11UpperRight", "Labo12Left"),
    ],
    "Labo 12": [
        ("Labo12Left", "Labo11UpperRight"),
        ("Labo12Lower", "Labo26Upper"),
        ("Labo12Right", "Labo13Left"),
    ],
    "Labo 13": [
        ("Labo13Left", "Labo12Right"),
        ("Labo13Right", "Labo19Left"),
    ],
    "Labo 14": [
        ("Labo14LowerLeft", "Labo03Right"),
        ("Labo14Right", "Labo17Left"),
        ("Labo14Upper", "Labo08Lower"),
        ("Labo14UpperLeft", "Labo04Right"),
    ],
    "Labo 15": [
        ("Labo15Left", "Labo16Right"),
        ("Labo15Right", "Labo06CenterLeft"),
        ("Labo15Upper", "Labo24Lower"),
    ],
    "Labo 16": [
        ("Labo16Left", "Labo08CenterRight"),
        ("Labo16Lower", "Labo07Upper"),
        ("Labo16Right", "Labo15Left"),
    ],
    "Labo 17": [
        ("Labo17Left", "Labo14Right"),
    ],
    "Labo 18": [
        ("Labo18Left", "Labo19Right"),
        ("Labo18RightDoor", "Summit19CenterDoor"),
    ],
    "Labo 19": [
        ("Labo19Left", "Labo13Right"),
        ("Labo19LowerCenter", "Labo24Upper"),
        ("Labo19LowerLeft", "Labo08Upper"),
        ("Labo19LowerRight", "Labo06Upper"),
        ("Labo19Right", "Labo18Left"),
    ],
    "Labo 20": [
        ("Labo20Left", "Labo23Right"),
        ("Labo20Lower", "Labo05Upper"),
        ("Labo20LowerRight", "Labo21LowerLeft"),
        ("Labo20UpperRight", "Labo21UpperLeft"),
    ],
    "Labo 21": [
        ("Labo21LowerLeft", "Labo20LowerRight"),
        ("Labo21UpperLeft", "Labo20UpperRight"),
    ],
    "Labo 22": [
        ("Labo22LowerRight", "Labo25LowerLeft1"),
        ("Labo22UpperRight", "Labo25LowerLeft2"),
    ],
    "Labo 23": [
        ("Labo23Left", "Labo10Right"),
        ("Labo23Lower", "Labo09Upper"),
        ("Labo23Right", "Labo20Left"),
    ],
    "Labo 24": [
        ("Labo24Left", "Labo08UpperRight"),
        ("Labo24Lower", "Labo15Upper"),
        ("Labo24Right", "Labo06UpperLeft"),
        ("Labo24Upper", "Labo19LowerCenter"),
    ],
    "Labo 25": [
        ("Labo25LowerLeft1", "Labo22LowerRight"),
        ("Labo25LowerLeft2", "Labo22UpperRight"),
        ("Labo25UpperLeft1", "Labo27LowerRight"),
        ("Labo25UpperLeft2", "Labo27UpperRight"),
        ("Labo25Right", "Labo10Left"),
    ],
    "Labo 26": [
        ("Labo26Left", "Labo11LowerRight"),
        ("Labo26Right", "Labo08UpperLeft"),
        ("Labo26Upper", "Labo12Lower"),
    ],
    "Labo 27": [
        ("Labo27UpperRight", "Labo25UpperLeft2"),
        ("Labo27LowerRight", "Labo25UpperLeft1"),
    ],
    "Mine 1": [
        ("Mine01Left", "Mine13Right"),
        ("Mine01Lower", "Mine02UpperRight"),
        ("Mine01Right", "Crossroad03Left"),
    ],
    "Mine 2": [
        ("Mine02LowerLeft", "Mine04Upper"),
        ("Mine02LowerRight", "Mine03Upper"),
        ("Mine02UpperRight", "Mine01Lower"),
    ],
    "Mine 3": [
        ("Mine03Lower", "Mine05Upper"),
        ("Mine03Upper", "Mine02LowerRight"),
    ],
    "Mine 4": [
        ("Mine04Left", "Mine12Right"),
        ("Mine04Upper", "Mine02LowerLeft"),
    ],
    "Mine 5": [
        ("Mine05Left", "Mine06Right"),
        ("Mine05Upper", "Mine03Lower"),
    ],
    "Mine 6": [
        ("Mine06Left", "Mine07Right"),
        ("Mine06Lower", "Mine07HiddenRight"),
        ("Mine06Right", "Mine05Left"),
    ],
    "Mine 7": [
        ("Mine07HiddenRight", "Mine06Lower"),
        ("Mine07LowerLeft", "Mine11Right"),
        ("Mine07Right", "Mine06Left"),
        ("Mine07UpperLeft", "Mine09Right"),
    ],
    "Mine 8": [
        ("Mine08Right", "Mine10Left"),
        ("Mine08Upper", "Mine17Lower"),
    ],
    "Mine 9": [
        ("Mine09Right", "Mine07UpperLeft"),
        ("Mine09Upper", "Mine10Lower"),
    ],
    "Mine 10": [
        ("Mine10Left", "Mine08Right"),
        ("Mine10Lower", "Mine09Upper"),
        ("Mine10Right", "Mine12Left"),
    ],
    "Mine 11": [
        ("Mine11Right", "Mine07LowerLeft"),
    ],
    "Mine 12": [
        ("Mine12Left", "Mine10Right"),
        ("Mine12Right", "Mine04Left"),
        ("Mine12Upper", "Mine14Lower"),
    ],
    "Mine 13": [
        ("Mine13Left", "Mine14Right"),
        ("Mine13Right", "Mine01Left"),
    ],
    "Mine 14": [
        ("Mine14Left", "Mine15Right"),
        ("Mine14Lower", "Mine12Upper"),
        ("Mine14Right", "Mine13Left"),
    ],
    "Mine 15": [
        ("Mine15Left", "Mine16Right"),
        ("Mine15Right", "Mine14Left"),
    ],
    "Mine 16": [
        ("Mine16Left", "Mine17Right"),
        ("Mine16Right", "Mine15Left"),
    ],
    "Mine 17": [
        ("Mine17Lower", "Mine08Upper"),
        ("Mine17Right", "Mine16Left"),
    ],
    "Paradise 1": [
        ("Paradise01Left", "Kowloon36Right"),
        ("Paradise01LowerRight", "Paradise05Left"),
        ("Paradise01UpperRight", "Paradise02Left"),
    ],
    "Paradise 2": [
        ("Paradise02CenterRight", "Paradise04LowerLeft"),
        ("Paradise02Left", "Paradise01UpperRight"),
        ("Paradise02LowerRight", "Paradise19Left"),
        ("Paradise02UpperRight", "Paradise04UpperLeft"),
    ],
    "Paradise 3": [
        ("Paradise03Lower", "Paradise33Upper"),
        ("Paradise03LowerLeft", "Paradise08LowerRight"),
        ("Paradise03UpperLeft", "Paradise08UpperRight"),
    ],
    "Paradise 4": [
        ("Paradise04CenterRight", "Paradise10Left"),
        ("Paradise04Lower", "Paradise12Upper"),
        ("Paradise04LowerLeft", "Paradise02CenterRight"),
        ("Paradise04LowerRight", "Paradise07Left"),
        ("Paradise04UpperLeft", "Paradise02UpperRight"),
        ("Paradise04UpperRight", "Paradise09Left"),
    ],
    "Paradise 5": [
        ("Paradise05Left", "Paradise01LowerRight"),
        ("Paradise05Right", "Paradise20CenterLeft"),
        ("Paradise05UpperLeft", "Paradise06LowerLeft"),
        ("Paradise05UpperRight", "Paradise06LowerRight"),
    ],
    "Paradise 6": [
        ("Paradise06LowerLeft", "Paradise05UpperLeft"),
        ("Paradise06LowerRight", "Paradise05UpperRight"),
    ],
    "Paradise 7": [
        ("Paradise07Left", "Paradise04LowerRight"),
        ("Paradise07Lower", "Paradise18Upper"),
    ],
    "Paradise 8": [
        ("Paradise08Lower", "Paradise11Upper"),
        ("Paradise08LowerLeft", "Paradise09Right"),
        ("Paradise08LowerRight", "Paradise03LowerLeft"),
        ("Paradise08UpperLeft", "Paradise10Right"),
        ("Paradise08UpperRight", "Paradise03UpperLeft"),
    ],
    "Paradise 9": [
        ("Paradise09Left", "Paradise04UpperRight"),
        ("Paradise09Right", "Paradise08LowerLeft"),
    ],
    "Paradise 10": [
        ("Paradise10Left", "Paradise04CenterRight"),
        ("Paradise10Right", "Paradise08UpperLeft"),
    ],
    "Paradise 11": [
        ("Paradise11Upper", "Paradise08Lower"),
    ],
    "Paradise 12": [
        ("Paradise12Upper", "Paradise04Lower"),
    ],
    "Paradise 18": [
        ("Paradise18Lower", "Paradise19Upper"),
        ("Paradise18Upper", "Paradise07Lower"),
    ],
    "Paradise 19": [
        ("Paradise19Left", "Paradise02LowerRight"),
        ("Paradise19Lower", "Paradise32HiddenUpper"),
        ("Paradise19Upper", "Paradise18Lower"),
    ],
    "Paradise 20": [
        ("Paradise20CenterLeft", "Paradise05Right"),
        ("Paradise20CenterRight", "Paradise24Left"),
        ("Paradise20LowerLeft", "Paradise21Right"),
        ("Paradise20LowerRight", "Paradise23Left"),
        ("Paradise20UpperLeft", "Paradise22Right"),
        ("Paradise20UpperRight", "Paradise27Left"),
    ],
    "Paradise 21": [
        ("Paradise21Right", "Paradise20LowerLeft"),
    ],
    "Paradise 22": [
        ("Paradise22Right", "Paradise20UpperLeft"),
    ],
    "Paradise 23": [
        ("Paradise23Left", "Paradise20LowerRight"),
    ],
    "Paradise 24": [
        ("Paradise24Left", "Paradise20CenterRight"),
    ],
    "Paradise 25": [
        ("Paradise25HiddenLower", "Paradise26Upper"),
        ("Paradise25Right", "Paradise28CenterLeft"),
    ],
    "Paradise 26": [
        ("Paradise26Upper", "Paradise25HiddenLower"),
    ],
    "Paradise 27": [
        ("Paradise27Left", "Paradise20UpperRight"),
        ("Paradise27Right", "Paradise28UpperLeft"),
    ],
    "Paradise 28": [
        ("Paradise28CenterLeft", "Paradise25Right"),
        ("Paradise28CenterRight", "Paradise31Left"),
        ("Paradise28LowerRight", "Paradise30Left"),
        ("Paradise28UpperLeft", "Paradise27Right"),
        ("Paradise28UpperRight", "Paradise29Left"),
    ],
    "Paradise 29": [
        ("Paradise29Left", "Paradise28UpperRight"),
    ],
    "Paradise 30": [
        ("Paradise30Left", "Paradise28LowerRight"),
    ],
    "Paradise 31": [
        ("Paradise31Left", "Paradise28CenterRight"),
        ("Paradise31Right", "Paradise32Left"),
    ],
    "Paradise 32": [
        ("Paradise32HiddenUpper", "Paradise19Lower"),
        ("Paradise32Left", "Paradise31Right"),
        ("Paradise32Lower", "Paradise34Upper"),
        ("Paradise32Right", "Paradise33Left"),
    ],
    "Paradise 33": [
        ("Paradise33Left", "Paradise32Right"),
        ("Paradise33Upper", "Paradise03Lower"),
    ],
    "Paradise 34": [
        ("Paradise34Upper", "Paradise32Lower"),
    ],
    "Quarry 1": [
        ("Quarry01Left", "Quarry02Right"),
        ("Quarry01Right", "Ruins08Left"),
    ],
    "Quarry 2": [
        ("Quarry02LowerLeft", "Quarry03Upper"),
        ("Quarry02LowerRight", "Quarry04Upper"),
        ("Quarry02Right", "Quarry01Left"),
    ],
    "Quarry 3": [
        ("Quarry03Lower", "Quarry07Upper"),
        ("Quarry03Upper", "Quarry02LowerLeft"),
    ],
    "Quarry 4": [
        ("Quarry04Left", "Quarry07Right"),
        ("Quarry04Upper", "Quarry02LowerRight"),
    ],
    "Quarry 5": [
        ("Quarry05Lower", "Quarry13Upper"),
    ],
    "Quarry 7": [
        ("Quarry07Left", "Quarry13Right"),
        ("Quarry07Lower", "Quarry15Upper"),
        ("Quarry07Right", "Quarry04Left"),
        ("Quarry07Upper", "Quarry03Lower"),
    ],
    "Quarry 8": [
        ("Quarry08Left", "Quarry10UpperRight"),
        ("Quarry08Right", "Quarry13Left"),
    ],
    "Quarry 9": [
        ("Quarry09Left", "Quarry19LowerRight"),
        ("Quarry09Right", "Quarry18LowerLeft"),
    ],
    "Quarry 10": [
        ("Quarry10HiddenRight", "Quarry11Left"),
        ("Quarry10Lower", "Quarry12Upper"),
        ("Quarry10UpperRight", "Quarry08Left"),
    ],
    "Quarry 11": [
        ("Quarry11Left", "Quarry10HiddenRight"),
    ],
    "Quarry 12": [
        ("Quarry12Left", "Quarry21Right"),
        ("Quarry12Lower", "Quarry18Upper"),
        ("Quarry12Right", "Quarry20Left"),
        ("Quarry12Upper", "Quarry10Lower"),
    ],
    "Quarry 13": [
        ("Quarry13Left", "Quarry08Right"),
        ("Quarry13Right", "Quarry07Left"),
        ("Quarry13Upper", "Quarry05Lower"),
    ],
    "Quarry 14": [
        ("Quarry14Right", "Quarry23UpperLeft"),
        ("Quarry14Upper", "Quarry21Lower"),
    ],
    "Quarry 15": [
        ("Quarry15Left", "Quarry22Right"),
        ("Quarry15LowerLeft", "Quarry24Upper"),
        ("Quarry15LowerRight", "Quarry31Upper"),
        ("Quarry15Upper", "Quarry07Lower"),
    ],
    "Quarry 16": [
        ("Quarry16Right", "Quarry18HiddenLeft"),
    ],
    "Quarry 17": [
        ("Quarry17Right", "Quarry21HiddenLeft"),
    ],
    "Quarry 18": [
        ("Quarry18HiddenLeft", "Quarry16Right"),
        ("Quarry18LowerLeft", "Quarry09Right"),
        ("Quarry18Upper", "Quarry12Lower"),
    ],
    "Quarry 19": [
        ("Quarry19LowerRight", "Quarry09Left"),
        ("Quarry19UpperRight", "Quarry23LowerLeft"),
    ],
    "Quarry 20": [
        ("Quarry20Left", "Quarry12Right"),
        ("Quarry20Right", "Quarry22Left"),
    ],
    "Quarry 21": [
        ("Quarry21HiddenLeft", "Quarry17Right"),
        ("Quarry21Lower", "Quarry14Upper"),
        ("Quarry21Right", "Quarry12Left"),
    ],
    "Quarry 22": [
        ("Quarry22Left", "Quarry20Right"),
        ("Quarry22Right", "Quarry15Left"),
    ],
    "Quarry 23": [
        ("Quarry23LowerLeft", "Quarry19UpperRight"),
        ("Quarry23UpperLeft", "Quarry14Right"),
    ],
    "Quarry 24": [
        ("Quarry24Upper", "Quarry15LowerLeft"),
    ],
    "Quarry 31": [
        ("Quarry31Right", "Roots17Left"),
        ("Quarry31Upper", "Quarry15LowerRight"),
    ],
    "Roots 1": [
        ("Roots01Left", "Roots04Right"),
    ],
    "Roots 2": [
        ("Roots02Right", "Roots03Left"),
    ],
    "Roots 3": [
        ("Roots03Left", "Roots02Right"),
        ("Roots03Right", "Roots24Left"),
    ],
    "Roots 4": [
        ("Roots04Left", "Roots21Right"),
        ("Roots04Right", "Roots01Left"),
        ("Roots04Upper", "Roots20Lower"),
    ],
    "Roots 5": [
        ("Roots05Right", "Roots12LowerLeft"),
        ("Roots05Upper", "Roots09Lower"),
    ],
    "Roots 6": [
        ("Roots06Lower", "Roots07Upper"),
        ("Roots06Right", "Sewer09Left"),
    ],
    "Roots 7": [
        ("Roots07HiddenRight", "Roots08Left"),
        ("Roots07Left", "Roots11Right"),
        ("Roots07Upper", "Roots06Lower"),
    ],
    "Roots 8": [
        ("Roots08Left", "Roots07HiddenRight"),
    ],
    "Roots 9": [
        ("Roots09Lower", "Roots05Upper"),
        ("Roots09Right", "Roots12UppwrLeft"),
        ("Roots09Upper", "Roots10LowerLeft"),
    ],
    "Roots 10": [
        ("Roots10LowerLeft", "Roots09Upper"),
        ("Roots10LowerRight", "Roots11HiddenUpper"),
    ],
    "Roots 11": [
        ("Roots11HiddenUpper", "Roots10LowerRight"),
        ("Roots11Lower", "Roots12Upper"),
        ("Roots11Right", "Roots07Left"),
    ],
    "Roots 12": [
        ("Roots12LowerLeft", "Roots05Right"),
        ("Roots12Upper", "Roots11Lower"),
        ("Roots12UppwrLeft", "Roots09Right"),
    ],
    "Roots 13": [
        ("Roots13Lower", "Roots20Upper"),
        ("Roots13LowerLeft", "Roots14Right"),
        ("Roots13Right", "Roots23Left"),
        ("Roots13UpperLeft", "Roots16Right"),
    ],
    "Roots 14": [
        ("Roots14Left", "Roots15Right"),
        ("Roots14Right", "Roots13LowerLeft"),
    ],
    "Roots 15": [
        ("Roots15Left", "Roots18UpperRight"),
        ("Roots15Right", "Roots14Left"),
    ],
    "Roots 16": [
        ("Roots16Left", "Roots17Right"),
        ("Roots16Right", "Roots13UpperLeft"),
    ],
    "Roots 17": [
        ("Roots17Left", "Quarry31Right"),
        ("Roots17Right", "Roots16Left"),
    ],
    "Roots 18": [
        ("Roots18LowerRight", "Roots19Left"),
        ("Roots18UpperRight", "Roots15Left"),
    ],
    "Roots 19": [
        ("Roots19Left", "Roots18LowerRight"),
        ("Roots19Right", "Roots21Left"),
    ],
    "Roots 20": [
        ("Roots20Lower", "Roots04Upper"),
        ("Roots20Upper", "Roots13Lower"),
    ],
    "Roots 21": [
        ("Roots21Left", "Roots19Right"),
        ("Roots21Lower", "Roots22Upper"),
        ("Roots21Right", "Roots04Left"),
    ],
    "Roots 22": [
        ("Roots22Upper", "Roots21Lower"),
    ],
    "Roots 23": [
        ("Roots23Left", "Roots13Right"),
    ],
    "Roots 24": [
        ("Roots24HiddenLeft", "Roots30Right"),
        ("Roots24Left", "Roots03Right"),
        ("Roots24LowerLeft", "Roots29Upper"),
        ("Roots24LowerRight", "Roots26Upper"),
        ("Roots24Right", "Roots25Left"),
        ("Roots24UpperLeft", "Roots28Lower"),
        ("Roots24UpperRight", "Roots27Lower"),
    ],
    "Roots 25": [
        ("Roots25Left", "Roots24Right"),
        ("Roots25Right", "Swamp10Left"),
    ],
    "Roots 26": [
        ("Roots26Upper", "Roots24LowerRight"),
    ],
    "Roots 27": [
        ("Roots27Lower", "Roots24UpperRight"),
    ],
    "Roots 28": [
        ("Roots28Lower", "Roots24UpperLeft"),
    ],
    "Roots 29": [
        ("Roots29Upper", "Roots24LowerLeft"),
    ],
    "Roots 30": [
        ("Roots30Right", "Roots24HiddenLeft"),
    ],
    "Ruins 1": [
        ("Ruins01Left", "Ruins15Right"),
        ("Ruins01Right", "Ruins02UpperLeft"),
    ],
    "Ruins 2": [
        ("Ruins02LowerLeft", "Ruins07UpperRight"),
        ("Ruins02LowerRight", "Ruins03Left"),
        ("Ruins02UpperLeft", "Ruins01Right"),
        ("Ruins02UpperRight", "Ruins09Left"),
    ],
    "Ruins 3": [
        ("Ruins03Left", "Ruins02LowerRight"),
        ("Ruins03Right", "Ruins04UpperLeft"),
    ],
    "Ruins 4": [
        ("Ruins04LowerLeft", "Ruins05Right"),
        ("Ruins04UpperLeft", "Ruins03Right"),
    ],
    "Ruins 5": [
        ("Ruins05Left", "Ruins06Right"),
        ("Ruins05Right", "Ruins04LowerLeft"),
    ],
    "Ruins 6": [
        ("Ruins06Left", "Ruins07LowerRight"),
        ("Ruins06Right", "Ruins05Left"),
    ],
    "Ruins 7": [
        ("Ruins07LowerLeft", "Ruins08Right"),
        ("Ruins07LowerRight", "Ruins06Left"),
        ("Ruins07UpperRight", "Ruins02LowerLeft"),
    ],
    "Ruins 8": [
        ("Ruins08Left", "Quarry01Right"),
        ("Ruins08Right", "Ruins07LowerLeft"),
    ],
    "Ruins 9": [
        ("Ruins09Left", "Ruins02UpperRight"),
        ("Ruins09Right", "Ruins10LowerLeft"),
    ],
    "Ruins 10": [
        ("Ruins10LowerLeft", "Ruins09Right"),
        ("Ruins10Right", "Ruins13Left"),
        ("Ruins10UpperLeft", "Ruins11Right"),
    ],
    "Ruins 11": [
        ("Ruins11Left", "Ruins12Right"),
        ("Ruins11Right", "Ruins10UpperLeft"),
    ],
    "Ruins 12": [
        ("Ruins12Right", "Ruins11Left"),
    ],
    "Ruins 13": [
        ("Ruins13Left", "Ruins10Right"),
        ("Ruins13Upper", "Crossroad01Lower"),
    ],
    "Ruins 14": [
        ("Ruins14Right", "Ruins16Left"),
    ],
    "Ruins 15": [
        ("Ruins15Left", "Ruins16Right"),
        ("Ruins15Right", "Ruins01Left"),
    ],
    "Ruins 16": [
        ("Ruins16Left", "Ruins14Right"),
        ("Ruins16Right", "Ruins15Left"),
    ],
    "Sewer 1": [
        ("Sewer01Right", "Sewer03UpperLeft"),
        ("Sewer01Upper", "Slum02Lower"),
    ],
    "Sewer 2": [
        ("Sewer02Lower", "Sewer04Upper"),
        ("Sewer02LowerLeft", "Sewer03CenterRight"),
        ("Sewer02UpperLeft", "Sewer03UpperRight"),
    ],
    "Sewer 3": [
        ("Sewer03CenterRight", "Sewer02LowerLeft"),
        ("Sewer03HiddenLeft", "Sewer05Right"),
        ("Sewer03LowerCenter", "Sewer12Upper"),
        ("Sewer03LowerLeft", "Sewer06Right"),
        ("Sewer03LowerRight", "Sewer04Left"),
        ("Sewer03UpperLeft", "Sewer01Right"),
        ("Sewer03UpperRight", "Sewer02UpperLeft"),
    ],
    "Sewer 4": [
        ("Sewer04Left", "Sewer03LowerRight"),
        ("Sewer04Lower", "Sewer13Upper"),
        ("Sewer04Right", "Sewer14UpperLeft"),
        ("Sewer04Upper", "Sewer02Lower"),
    ],
    "Sewer 5": [
        ("Sewer05Right", "Sewer03HiddenLeft"),
    ],
    "Sewer 6": [
        ("Sewer06Left", "Sewer07UpperRight"),
        ("Sewer06Right", "Sewer03LowerLeft"),
    ],
    "Sewer 7": [
        ("Sewer07LowerRight", "Sewer08Left"),
        ("Sewer07UpperRight", "Sewer06Left"),
    ],
    "Sewer 8": [
        ("Sewer08Left", "Sewer07LowerRight"),
        ("Sewer08Lower", "Sewer09UpperLeft"),
    ],
    "Sewer 9": [
        ("Sewer09Left", "Roots06Right"),
        ("Sewer09Right", "Sewer10Left"),
        ("Sewer09UpperLeft", "Sewer08Lower"),
        ("Sewer09UpperRight", "Sewer12Lower"),
    ],
    "Sewer 10": [
        ("Sewer10Left", "Sewer09Right"),
        ("Sewer10Right", "Sewer11Left"),
    ],
    "Sewer 11": [
        ("Sewer11Left", "Sewer10Right"),
        ("Sewer11LowerRight", "Sewer15Left"),
        ("Sewer11UpperRight", "Sewer14LowerLeft"),
    ],
    "Sewer 12": [
        ("Sewer12Lower", "Sewer09UpperRight"),
        ("Sewer12Upper", "Sewer03LowerCenter"),
    ],
    "Sewer 13": [
        ("Sewer13Right", "Sewer14CenterLeft"),
        ("Sewer13Upper", "Sewer04Lower"),
    ],
    "Sewer 14": [
        ("Sewer14CenterLeft", "Sewer13Right"),
        ("Sewer14HiddenRight", "Sewer17Left"),
        ("Sewer14LowerLeft", "Sewer11UpperRight"),
        ("Sewer14UpperLeft", "Sewer04Right"),
    ],
    "Sewer 15": [
        ("Sewer15Left", "Sewer11LowerRight"),
        ("Sewer15Lower", "Swamp18Upper"),
    ],
    "Sewer 17": [
        ("Sewer17Left", "Sewer14HiddenRight"),
    ],
    "Slum 1": [
        ("Slum01Left", "Crossroad02Right"),
        ("Slum01Lower", "Slum02Upper"),
        ("Slum01Right", "Street01Left"),
    ],
    "Slum 2": [
        ("Slum02Lower", "Sewer01Upper"),
        ("Slum02Upper", "Slum01Lower"),
    ],
    "Street 1": [
        ("Street01Door", "Street18Door"),
        ("Street01Left", "Slum01Right"),
        ("Street01Right", "Street06Left"),
    ],
    "Street 2": [
        ("Street02Left", "Street18Right"),
        ("Street02Right", "Street04Left"),
    ],
    "Street 3": [
        ("Street03Door", "Street10Door"),
        ("Street03LowerLeft", "Street05LowerRight"),
        ("Street03Right", "Street11Left"),
        ("Street03UpperLeft", "Street05UpperRight"),
    ],
    "Street 4": [
        ("Street04Left", "Street02Right"),
        ("Street04Right", "Street05Left"),
    ],
    "Street 5": [
        ("Street05Left", "Street04Right"),
        ("Street05LowerRight", "Street03LowerLeft"),
        ("Street05UpperRight", "Street03UpperLeft"),
    ],
    "Street 6": [
        ("Street06Left", "Street01Right"),
        ("Street06Right", "Street07CenterLeft"),
    ],
    "Street 7": [
        ("Street07CenterLeft", "Street06Right"),
        ("Street07HiddenLeft", "Street21Right"),
        ("Street07LowerLeft", "Street20Right"),
        ("Street07LowerRight", "Street09Left"),
        ("Street07UpperRight", "Street08Left"),
    ],
    "Street 8": [
        ("Street08Left", "Street07UpperRight"),
        ("Street08Right", "Street10Left"),
    ],
    "Street 9": [
        ("Street09Left", "Street07LowerRight"),
        ("Street09Upper", "Street10Lower"),
    ],
    "Street 10": [
        ("Street10Door", "Street03Door"),
        ("Street10Left", "Street08Right"),
        ("Street10Lower", "Street09Upper"),
    ],
    "Street 11": [
        ("Street11Left", "Street03Right"),
        ("Street11Right", "Street12Left"),
        ("Street11Upper", "Center01Lower"),
    ],
    "Street 12": [
        ("Street12Door", "Street13Door"),
        ("Street12Left", "Street11Right"),
        ("Street12LowerRight", "Street19LowerLeft"),
        ("Street12UpperRight", "Street19UpperLeft"),
    ],
    "Street 13": [
        ("Street13Door", "Street12Door"),
        ("Street13Left", "Street17Right"),
        ("Street13LowerHidden", "Street14UpperHidden"),
        ("Street13LowerLeft", "Street14UpperLeft"),
        ("Street13LowerRight", "Street14UpperRight"),
    ],
    "Street 14": [
        ("Street14Right", "Street15Left"),
        ("Street14UpperHidden", "Street13LowerHidden"),
        ("Street14UpperLeft", "Street13LowerLeft"),
        ("Street14UpperRight", "Street13LowerRight"),
    ],
    "Street 15": [
        ("Street15Left", "Street14Right"),
        ("Street15Right", "Tower01Left"),
    ],
    "Street 17": [
        ("Street17Right", "Street13Left"),
    ],
    "Street 18": [
        ("Street18Door", "Street01Door"),
        ("Street18Right", "Street02Left"),
    ],
    "Street 19": [
        ("Street19LowerLeft", "Street12LowerRight"),
        ("Street19UpperLeft", "Street12UpperRight"),
    ],
    "Street 20": [
        ("Street20Right", "Street07LowerLeft"),
    ],
    "Street 21": [
        ("Street21Right", "Street07HiddenLeft"),
    ],
    "Summit 1": [
        ("Summit01LowerLeft", "Summit02LowerRight"),
        ("Summit01RightDoor", "Kowloon04LeftDoor"),
        ("Summit01UpperLeft", "Summit02UpperRight"),
    ],
    "Summit 2": [
        ("Summit02Left", "Summit03Right"),
        ("Summit02LowerRight", "Summit01LowerLeft"),
        ("Summit02UpperRight", "Summit01UpperLeft"),
    ],
    "Summit 3": [
        ("Summit03HiddenLeft", "Summit04Right"),
        ("Summit03Right", "Summit02Left"),
        ("Summit03UpperLeft", "Summit06Right"),
    ],
    "Summit 4": [
        ("Summit04Left", "Summit05HiddenRight"),
        ("Summit04Right", "Summit03HiddenLeft"),
    ],
    "Summit 5": [
        ("Summit05HiddenRight", "Summit04Left"),
        ("Summit05Left", "Summit07Right"),
        ("Summit05UpperRight", "Summit06Left"),
    ],
    "Summit 6": [
        ("Summit06CenterDoor", "Summit12LeftDoor"),
        ("Summit06Left", "Summit05UpperRight"),
        ("Summit06Right", "Summit03UpperLeft"),
    ],
    "Summit 7": [
        ("Summit07LowerLeft", "Summit08LowerRight"),
        ("Summit07Right", "Summit05Left"),
        ("Summit07UpperLeft", "Summit08UpperRighy"),
    ],
    "Summit 8": [
        ("Summit08Left", "Summit19CenterDoor"),
        ("Summit08LeftDoor", "Summit11CenterDoor"),
        ("Summit08LowerRight", "Summit07LowerLeft"),
        ("Summit08RightDoor", "Summit15CenterDoor"),
        ("Summit08UpperRighy", "Summit07UpperLeft"),
    ],
    "Summit 9": [
        ("Summit09LowerLeft", "Summit15HiddenRight"),
        ("Summit09Right", "Summit14Left"),
        ("Summit09UpperLeft", "Summit15Right"),
    ],
    "Summit 10": [
        ("Summit10Right", "Summit11Left"),
    ],
    "Summit 11": [
        ("Summit11CenterDoor", "Summit08LeftDoor"),
        ("Summit11Left", "Summit10Right"),
        ("Summit11Right", "Summit16Left"),
    ],
    "Summit 12": [
        ("Summit12LeftDoor", "Summit06CenterDoor"),
        ("Summit12LowerLeft", "Summit13LowerRight"),
        ("Summit12Right", "Summit18Left"),
        ("Summit12RightDoor", "Summit17CenterDoor"),
        ("Summit12UpperLeft", "Summit13UpperRight"),
    ],
    "Summit 13": [
        ("Summit13Left", "Summit14Right"),
        ("Summit13LowerRight", "Summit12LowerLeft"),
        ("Summit13UpperRight", "Summit12UpperLeft"),
    ],
    "Summit 14": [
        ("Summit14CenterDoor", "Summit20CenterDoor"),
        ("Summit14Left", "Summit09Right"),
        ("Summit14Right", "Summit13Left"),
    ],
    "Summit 15": [
        ("Summit15CenterDoor", "Summit08RightDoor"),
        ("Summit15HiddenRight", "Summit09LowerLeft"),
        ("Summit15Left", "Summit16Right"),
        ("Summit15Right", "Summit09UpperLeft"),
    ],
    "Summit 16": [
        ("Summit16CenterDoor", "Summit24CenterDoor"),
        ("Summit16Left", "Summit11Right"),
        ("Summit16Right", "Summit15Left"),
    ],
    "Summit 17": [
        ("Summit17CenterDoor", "Summit12RightDoor"),
        ("Summit17LowerLeft", "Summit23LowerRight"),
        ("Summit17UpperLeft", "Summit23UpperRight"),
    ],
    "Summit 18": [
        ("Summit18Left", "Summit12Right"),
    ],
    "Summit 19": [
        ("Summit19CenterDoor", "Labo18RightDoor"),
    ],
    "Summit 20": [
        ("Summit20CenterDoor", "Summit14CenterDoor"),
        ("Summit20Upper", "Summit21Lower"),
    ],
    "Summit 21": [
        ("Summit21Left", "Summit24LowerRight"),
        ("Summit21Lower", "Summit20Upper"),
        ("Summit21Right", "Summit22LowerLeft"),
    ],
    "Summit 22": [
        ("Summit22CenterLeft", "Summit25UpperRight"),
        ("Summit22CenterRight", "Summit23CenterLeft"),
        ("Summit22LowerLeft", "Summit21Right"),
        ("Summit22LowerRight", "Summit23LowerLeft"),
        ("Summit22UpperLeft", "Summit24UpperRight"),
        ("Summit22UpperRight", "Summit23UpperLeft"),
    ],
    "Summit 23": [
        ("Summit23CenterLeft", "Summit22CenterRight"),
        ("Summit23LowerLeft", "Summit22LowerRight"),
        ("Summit23LowerRight", "Summit17LowerLeft"),
        ("Summit23UpperLeft", "Summit22UpperRight"),
        ("Summit23UpperRight", "Summit17UpperLeft"),
    ],
    "Summit 24": [
        ("Summit24CenterDoor", "Summit16CenterDoor"),
        ("Summit24CenterLeft", "Summit27CenterRight"),
        ("Summit24CenterRight", "Summit25UpperLeft"),
        ("Summit24HiddenRight", "Summit25LowerLeft"),
        ("Summit24LowerLeft", "Summit27LowerRight"),
        ("Summit24LowerRight", "Summit21Left"),
        ("Summit24UpperLeft", "Summit27UpperRight"),
        ("Summit24UpperRight", "Summit26Left"),
    ],
    "Summit 25": [
        ("Summit25Lower", "Summit28Upper"),
        ("Summit25LowerLeft", "Summit24HiddenRight"),
        ("Summit25LowerRight", "Summit22CenterLeft"),
        ("Summit25UpperLeft", "Summit24CenterRight"),
        ("Summit25UpperRight", "Summit24CenterRight"),
    ],
    "Summit 26": [
        ("Summit26CenterDoor", "Summit30CenterDoor"),
        ("Summit26Left", "Summit24UpperRight"),
    ],
    "Summit 27": [
        ("Summit27CenterRight", "Summit24CenterLeft"),
        ("Summit27LowerRight", "Summit24LowerLeft"),
        ("Summit27UpperRight", "Summit24UpperLeft"),
    ],
    "Summit 28": [
        ("Summit28Upper", "Summit25Lower"),
    ],
    "Summit 30": [
        ("Summit30CenterDoor", "Summit26CenterDoor"),
    ],
    "Swamp 1": [
        ("Swamp01LowerLeft", "Swamp02Upper"),
        ("Swamp01LowerRight", "Swamp20Upper"),
        ("Swamp01Upper", "Tower18Lower"),
    ],
    "Swamp 2": [
        ("Swamp02Left", "Swamp03Right"),
        ("Swamp02Upper", "Swamp01LowerLeft"),
    ],
    "Swamp 3": [
        ("Swamp03Left", "Swamp04Right"),
        ("Swamp03Right", "Swamp02Left"),
    ],
    "Swamp 4": [
        ("Swamp04HiddenLeft", "Swamp19Right"),
        ("Swamp04Lower", "Swamp13Upper"),
        ("Swamp04Right", "Swamp03Left"),
        ("Swamp04Upper", "Swamp05Lower"),
    ],
    "Swamp 5": [
        ("Swamp05Left", "Swamp06Right"),
        ("Swamp05Lower", "Swamp04Upper"),
        ("Swamp05Right", "Swamp18Left"),
    ],
    "Swamp 6": [
        ("Swamp06Lower", "Swamp07Upper"),
        ("Swamp06Right", "Swamp05Left"),
    ],
    "Swamp 7": [
        ("Swamp07Lower", "Swamp08Upper"),
        ("Swamp07Upper", "Swamp06Lower"),
    ],
    "Swamp 8": [
        ("Swamp08Lower", "Swamp10UpperLeft"),
        ("Swamp08Right", "Swamp09Left"),
        ("Swamp08Upper", "Swamp07Lower"),
    ],
    "Swamp 9": [
        ("Swamp09Left", "Swamp08Right"),
        ("Swamp09Lower", "Swamp10UpperRight"),
        ("Swamp09Right", "Swamp11UpperLeft"),
    ],
    "Swamp 10": [
        ("Swamp10Left", "Roots25Right"),
        ("Swamp10Right", "Swamp11LowerLeft"),
        ("Swamp10UpperLeft", "Swamp08Lower"),
        ("Swamp10UpperRight", "Swamp09Lower"),
    ],
    "Swamp 11": [
        ("Swamp11Lower", "Swamp14Upper"),
        ("Swamp11LowerLeft", "Swamp10Right"),
        ("Swamp11LowerRight", "Swamp12LowerLeft"),
        ("Swamp11UpperLeft", "Swamp09Right"),
        ("Swamp11UpperRight", "Swamp12UpperLeft"),
    ],
    "Swamp 12": [
        ("Swamp12LowerLeft", "Swamp12LowerLeft"),
        ("Swamp12Upper", "Swamp13Lower"),
        ("Swamp12UpperLeft", "Swamp11UpperRight"),
    ],
    "Swamp 13": [
        ("Swamp13Lower", "Swamp12Upper"),
        ("Swamp13Upper", "Swamp04Lower"),
    ],
    "Swamp 14": [
        ("Swamp14Right", "Swamp15Left"),
        ("Swamp14Upper", "Swamp11Lower"),
    ],
    "Swamp 15": [
        ("Swamp15Left", "Swamp14Right"),
        ("Swamp15Right", "Swamp16Left"),
    ],
    "Swamp 16": [
        ("Swamp16Left", "Swamp15Right"),
        ("Swamp16Right", "Swamp17Left"),
    ],
    "Swamp 17": [
        ("Swamp17Left", "Swamp16Right"),
    ],
    "Swamp 18": [
        ("Swamp18Left", "Swamp05Right"),
        ("Swamp18Upper", "Sewer15Lower"),
    ],
    "Swamp 19": [
        ("Swamp19Right", "Swamp04HiddenLeft"),
    ],
    "Swamp 20": [
        ("Swamp20Upper", "Swamp01LowerRight"),
    ],
    "Tower 1": [
        ("Tower01CenterRight", "Tower02CenterLeft"),
        ("Tower01Left", "Street15Right"),
        ("Tower01LowerRight", "Tower02LowerLeft"),
        ("Tower01UpperRight", "Tower02UpperLeft"),
    ],
    "Tower 2": [
        ("Tower02CenterLeft", "Tower01CenterRight"),
        ("Tower02CenterRight", "Tower03CenterLeft"),
        ("Tower02Lower", "Tower07Upper"),
        ("Tower02LowerLeft", "Tower01LowerRight"),
        ("Tower02LowerRight", "Tower03LowerLeft"),
        ("Tower02UpperLeft", "Tower01UpperRight"),
        ("Tower02UpperRight", "Tower03UpperLeft"),
    ],
    "Tower 3": [
        ("Tower03CenterLeft", "Tower02CenterRight"),
        ("Tower03LowerLeft", "Tower02LowerRight"),
        ("Tower03UpperLeft", "Tower02UpperRight"),
    ],
    "Tower 4": [
        ("Tower04Lower", "Tower05Upper"),
        ("Tower04Upper", "Tower07Lower"),
    ],
    "Tower 5": [
        ("Tower05Lower", "Tower08Upper"),
        ("Tower05Upper", "Tower04Lower"),
    ],
    "Tower 6": [
        ("Tower06Right", "Tower18Left"),
    ],
    "Tower 7": [
        ("Tower07Lower", "Tower04Upper"),
        ("Tower07Upper", "Tower02Lower"),
    ],
    "Tower 8": [
        ("Tower08Lower", "Tower09Upper"),
        ("Tower08Right", "Tower10UpperLeft"),
        ("Tower08Upper", "Tower05Lower"),
    ],
    "Tower 9": [
        ("Tower09CenterRight", "Tower10CenterLowerLeft"),
        ("Tower09Lower", "Tower11Upper"),
        ("Tower09LowerRight", "Tower10LowerLeft"),
        ("Tower09Upper", "Tower08Lower"),
        ("Tower09UpperRight", "Tower10CenterUpperLeft"),
    ],
    "Tower 10": [
        ("Tower10CenterLowerLeft", "Tower09CenterRight"),
        ("Tower10CenterUpperLeft", "Tower09UpperRight"),
        ("Tower10LowerLeft", "Tower09LowerRight"),
        ("Tower10UpperLeft", "Tower08Right"),
    ],
    "Tower 11": [
        ("Tower11HiddenLeft", "Tower12Right"),
        ("Tower11Lower", "Tower13Upper"),
        ("Tower11Upper", "Tower09Lower"),
    ],
    "Tower 12": [
        ("Tower12Right", "Tower11HiddenLeft"),
    ],
    "Tower 13": [
        ("Tower13Lower", "Tower19Upper"),
        ("Tower13Upper", "Tower11Lower"),
    ],
    "Tower 14": [
        ("Tower14LowerLeft", "Tower19LowerRight"),
        ("Tower14Right", "Tower15Left"),
        ("Tower14UpperLeft", "Tower19UpperRight"),
    ],
    "Tower 15": [
        ("Tower15Left", "Tower14Right"),
        ("Tower15Right", "Tower16Left"),
    ],
    "Tower 16": [
        ("Tower16Left", "Tower15Right"),
        ("Tower16Right", "Tower17Left"),
    ],
    "Tower 17": [
        ("Tower17Left", "Tower16Right"),
        ("Tower17Right", "Forest01Left"),
    ],
    "Tower 18": [
        ("Tower18Left", "Tower06Right"),
        ("Tower18Lower", "Swamp01Upper"),
        ("Tower18LowerRight", "Tower19LowerLeft"),
        ("Tower18UpperRight", "Tower19UpperLeft"),
    ],
    "Tower 19": [
        ("Tower19LowerLeft", "Tower18LowerRight"),
        ("Tower19LowerRight", "Tower14LowerLeft"),
        ("Tower19Upper", "Tower13Lower"),
        ("Tower19UpperLeft", "Tower18UpperRight"),
        ("Tower19UpperRight", "Tower14UpperLeft"),
    ],
}

regions : Dict[str, RegionData]  = {
**{
    region : RegionData(region, [ExitData(src, src) for (src, dst) in connections])
    for region, connections in room_connections.items()
},
**{
    src : RegionData(src, [ExitData(f"{src} to {dst}", dst), ExitData(f"{src} to {region}", region)])
    for region, connections in room_connections.items()
    for (src, dst) in connections
}}

regions["Menu"] = RegionData("Menu", [ExitData("Start", "Ruins 14")])

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
            locations["Crossroad 3 - Subterranean Laborer's Code"],
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
