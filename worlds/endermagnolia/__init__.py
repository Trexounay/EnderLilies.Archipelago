import os
from typing import List
from Utils import output_path
import settings
from BaseClasses import Item, Region
from worlds.AutoWorld import World
from worlds.generic.Rules import add_item_rule, add_rule, set_rule
from rule_builder.rules import True_

from .Locations import LocationGroup, locations, event_locations
from .Options import EnderMagnoliaOptions
from .Regions import room_connections
from .Items import ItemGroup, items, pool
from .Rules import get_entrances_rules, get_items_rules, get_locations_rules
from .Types import ENDERMAGNOLIA, EnderMagnoliaItem, EnderMagnoliaLocation, EnderMagnoliaEvent
from .gen.TransitionsRules import rules as transitions_rules
from .gen.LocationsRules import rules as locations_rules
from .gen.EventsRules import rules as events_rules


class EnderMagnoliaWorld(World):
    """
    Ender Magnolia: BLOOM IN THE MIST
    """

    game = ENDERMAGNOLIA

    # options
    options_dataclass = EnderMagnoliaOptions
    options: EnderMagnoliaOptions

    # items
    item_name_to_id = {name: data.code for name, data in items.items()}
    item_name_groups = {group.name : {name for name, data in items.items() if data.group == group} for group in ItemGroup}
    
    # locations
    location_name_to_id = {name: data.address for name, data in locations.items()}
    location_name_groups = {group.name : {name for name, data in locations.items() if data.group == group} for group in LocationGroup}

    def create_item(self, item: str) -> EnderMagnoliaItem:
        return EnderMagnoliaItem.from_name(item, self.player)

    def create_items(self) -> None:
        starting_skill = self.options.starting_skill.get_skill_name()
        self.get_location("Starting Skill").place_locked_item(self.create_item(starting_skill))

        items_pool : List[Item] = []
        remaining = list(pool)
        remaining.remove(items[starting_skill])
        for data in remaining:
            items_pool.append(EnderMagnoliaItem.from_data(data, self.player))
        self.multiworld.itempool.extend(items_pool)

    def create_region(self, name: str) -> Region:
        region = Region(name, self.player, self.multiworld)
        self.multiworld.regions.append(region)
        return region

    def create_location(self, name: str) -> EnderMagnoliaLocation:
        data = locations[name]
        parent_region = self.create_region(name)
        location = EnderMagnoliaLocation(self.player, name, data, parent_region)
        parent_region.locations.append(location)
        if data.event:
            event_location = EnderMagnoliaEvent(self.player, f"{data.region} - {data.event.name}", parent_region)
            event_location.place_locked_item(EnderMagnoliaItem.from_data(data.event, self.player))
            parent_region.locations.append(event_location)
        return location

    def create_event_location(self, name: str) -> EnderMagnoliaLocation:
        data = event_locations[name]
        parent_region = self.create_region(name)
        location = EnderMagnoliaEvent(self.player, name, parent_region)
        location.place_locked_item(EnderMagnoliaItem.from_data(data.content, self.player))
        parent_region.locations.append(location)
        return location

    def create_regions(self) -> None:
        rules = get_entrances_rules(self.player)

        # For each room entrances we create a region (need to happen first)
        for name in room_connections:
            self.create_region(name)

        # connect transitions together (room1 <-> room2)
        for name, region_data in room_connections.items():
            region = self.get_region(name)
            region.add_exits(region_data.get_exits())

        # connect rooms entrances (room1left <-> room1right)
        for (src, dst), rule in transitions_rules.items():
            region = self.get_region(src)
            region.add_exits([dst], {dst: rule});

        # add locations
        for name in locations:
            location = self.create_location(name)

        # add events
        for name in event_locations:
            location = self.create_event_location(name)
        
        # connect locations to rooms entrances
        for (src, dst), rule in locations_rules.items():
            region = self.get_region(src)
            region.add_exits([dst], {dst: rule});

        # connect events to rooms entrances
        for (src, dst), rule in events_rules.items():
            region = self.get_region(src)
            region.add_exits([dst], {dst: rule});

        # Starting weapon
        self.get_region("Menu").add_exits(["Starting Skill"])

    def set_rules(self) -> None:
        player = self.player
        items_rules = get_items_rules(player)

        # set items rules
        for location_name, rule in items_rules.items():
            add_item_rule(self.multiworld.get_location(location_name, player), rule)

        # Goal
        self.multiworld.completion_condition[player] = lambda state: state.has("Ending", player)

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
