import os
from typing import Dict, List, Optional, TextIO
from Utils import output_path
import settings
from BaseClasses import Item, ItemClassification, Location, Region
from worlds.AutoWorld import World
from worlds.generic.Rules import add_item_rule, add_rule, set_rule

from .Locations import LocationData, LocationGroup, locations, event_locations
from .Regions import regions
from .Items import ItemData, ItemGroup, items, pool
from .Rules import get_entrances_rules, get_locations_rules

ENDERMAGNOLIA = "Ender Magnolia"

class EnderMagnoliaItem(Item):
    game = ENDERMAGNOLIA
    
    @classmethod
    def from_name(cls, name: str, player: int):
        if name in items:
            return cls.from_data(items[name], player)
        return cls(name, ItemClassification.progression, None, player)

    @classmethod
    def from_data(cls, data: ItemData, player: int):
        return cls(data.name, data.classification, data.code, player)

class EnderMagnoliaLocation(Location):
    game = ENDERMAGNOLIA
    data : LocationData

    def __init__(self, player: int, name: str, data: LocationData, parent: Optional[Region] = None):
        address = data.address
        super().__init__(player, name, address, parent)
        self.data = data

    def key(self):
        return self.data.key

class EnderMagnoliaEvent(Location):
    game = ENDERMAGNOLIA
    def __init__(self, player: int, name: str, parent: Optional[Region] = None):
        super().__init__(player, name, None, parent)

class EnderMagnoliaWorld(World):
    """
    Ender Magnolia: BLOOM IN THE MIST
    """

    game = ENDERMAGNOLIA

    # items
    item_name_to_id = {name: data.code for name, data in items.items()}
    item_name_groups = {group.name : {name for name, data in items.items() if data.group == group} for group in ItemGroup}
    
    # locations
    location_name_to_id = {name: data.address for name, data in locations.items()}
    location_name_groups = {group.name : {name for name, data in locations.items() if data.group == group} for group in LocationGroup}

    def create_item(self, item: str) -> EnderMagnoliaItem:
        return EnderMagnoliaItem.from_name(item, self.player)

    def create_items(self) -> None:
        items_pool : List[Item] = []
        print("Pool contains", len(pool));

        for data in pool:
            items_pool.append(EnderMagnoliaItem.from_data(data, self.player))
        self.multiworld.itempool.extend(items_pool)

    def create_region(self, name: str) -> Region:
        region = Region(name, self.player, self.multiworld)
        self.multiworld.regions.append(region)
        return region

    def create_location(self, name: str, parent_region: Optional[Region] = None) -> EnderMagnoliaLocation:
        if name in locations:
            location = EnderMagnoliaLocation(self.player, name, locations[name], parent_region)
        elif name in event_locations:
            location = EnderMagnoliaEvent(self.player, name, parent_region)
            location.place_locked_item(EnderMagnoliaItem.from_data(event_locations[name].content, self.player))
        else:
            raise Exception(f"Could not create location {name}")
        if parent_region:
            parent_region.locations.append(location)
        return location

    def create_regions(self) -> None:
        rules = get_entrances_rules(self.player)

        # create regions
        for region_data in regions:
            self.create_region(region_data.name)

        # connect regions together (needs to happens after region creation)
        for region_data in regions:
            region = self.multiworld.get_region(region_data.name, self.player)
            for connection in region_data.connections:
                destination = self.multiworld.get_region(connection.destination, self.player)
                region.connect(destination, connection.name, rules.get(connection.name))
            for location in region_data.locations:
                self.create_location(location.name, region)
        total = self.multiworld.get_locations(self.player)

        # TMP
        # create fake locations to fill pool
        address = 1000
        region = self.get_region("Menu")
        for _ in range(len(total), len(pool)):
            l = Location(self.player, str(address), address, region)
            self.location_name_to_id[str(address)] = address;
            add_rule(l, lambda s : s.has("Victory", self.player))
            region.locations.append(l)
            address += 1


    def set_rules(self) -> None:
        rules = get_locations_rules(self.player)
        rules = {}

        # set location rules
        for location_name, rule in rules.items():
            add_rule(self.multiworld.get_location(location_name, self.player), rule)

        # Goal is to get the "Victory" event
        self.multiworld.completion_condition[self.player] = lambda s: s.has("Victory", self.player)

    def get_filler_item_name(self) -> str:
        return "nothing"

    def generate_output(self, output_directory):
        out_path = os.path.join(output_directory, "EnderMagnolia.txt")
        output = ""
        locations : List[EnderMagnoliaLocation] = self.multiworld.get_filled_locations();
        for location in locations:
            if isinstance(location, EnderMagnoliaLocation) and location.item and location.key() and location.item.name and location.item.name in items:
                s = f"{location.key()}:{items[location.item.name].key}"
                print(s)
                output += f"{s}\n"

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(output)
