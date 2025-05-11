from typing import Dict, List, Optional
import settings
from BaseClasses import Item, ItemClassification, Location, Region
from worlds.AutoWorld import World
from worlds.generic.Rules import add_item_rule, add_rule, set_rule

from .Locations import LocationData, LocationGroup, locations
from .Regions import regions
from .Items import ItemGroup, items
from .Rules import get_entrances_rules, get_locations_rules

ENDERMAGNOLIA = "Ender Magnolia"

class EnderMagnoliaItem(Item):
    game = ENDERMAGNOLIA

class EnderMagnoliaLocation(Location):
    game = ENDERMAGNOLIA
    data : LocationData

    def __init__(self, player: int, name: str = '', data: Optional[LocationData] = None, parent: Optional[Region] = None):
        address = None
        if data:
            address = data.address
        super().__init__(player, name, address, parent)
        self.data = data

    def key(self):
        if self.data:
            return self.data.key
        return self.name

class EnderMagnoliaWorld(World):
    """
    Ender Magnolia: BLOOM IN THE MIST
    """

    game = ENDERMAGNOLIA

    # items
    item_name_to_id = {name: data.code for name, data in items.items()}
    item_name_groups = {item_group.name : {name for name, data in items.items() if data.item_group == item_group} for item_group in ItemGroup}
    
    # locations
    location_name_to_id = {name: data.address for name, data in locations.items()}
    location_name_groups = {location_group.name : {name for name, data in locations.items() if data.location_group == location_group} for location_group in LocationGroup}

    def create_item(self, item: str) -> EnderMagnoliaItem:
        if item in items:
            return EnderMagnoliaItem(item, items[item].classification, items[item].code, self.player)
        # event
        return EnderMagnoliaItem(item, ItemClassification.progression, None, self.player)

    def create_items(self) -> None:
        items_pool : List[Item] = []
        for name, data in items.items():
            if not data.code:
                continue
            for i in range(data.count):
                items_pool.append(self.create_item(name))
        self.multiworld.itempool += items_pool

    def create_region(self, name: str, checks: Optional[List[LocationData]] = []) -> Region:
        region = Region(name, self.player, self.multiworld)
        self.multiworld.regions.append(region)
        for location in checks:
            self.create_location(location.name, region)
        return region

    def create_location(self, name: str, parent_region: Optional[Region] = None) -> EnderMagnoliaLocation:
        data = None
        if name in locations:
            data = locations[name]
        location = EnderMagnoliaLocation(self.player, name, data, parent_region)
        if not data.address and data.content:
            location.place_locked_item(self.create_item(data.content.name))
        if parent_region:
            parent_region.locations.append(location)
        return location

    def create_regions(self) -> None:
        rules = get_entrances_rules(self.player)

        # create regions
        for region_data in regions:
            self.create_region(region_data.name, checks=region_data.locations)

        # connect regions together (needs to happens after region creation)
        for region_data in regions:
            region = self.multiworld.get_region(region_data.name, self.player)
            for connection in region_data.connections:
                destination = self.multiworld.get_region(connection.destination, self.player)
                region.connect(destination, connection.name, rules.get(connection.name))

    def set_rules(self) -> None:
        rules = get_locations_rules(self.player)

        # set location rules
        for location_name, rule in rules.items():
            add_rule(self.multiworld.get_location(location_name, self.player), rule)

        # Goal is to get the "Victory" event
        self.multiworld.completion_condition[self.player] = lambda s: s.has("Victory", self.player)

    def get_filler_item_name(self) -> str:
        return "nothing"

