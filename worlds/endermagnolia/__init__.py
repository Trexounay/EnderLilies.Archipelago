import os
from typing import Any, List, Mapping
from BaseClasses import Item, Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.generic.Rules import add_item_rule

from .Locations import LocationData, LocationGroup, locations, event_locations
from .Options import CentralElevatorFix, EnderMagnoliaOptions
from .Regions import room_connections
from .Items import ItemGroup, custom, items, pool, stats
from .Rules import completion_rule, elevator_rules, items_rules, levy_rules, shop_rules, shop_item_rule
from .Types import ENDERMAGNOLIA, EnderMagnoliaItem, EnderMagnoliaLocation, EnderMagnoliaEvent
from .gen.TransitionsRules import rules as transitions_rules
from .gen.LocationsRules import rules as locations_rules
from .gen.EventsRules import rules as events_rules


class EnderMagnoliaWebWorld(WebWorld):
    game = ENDERMAGNOLIA
    theme = "dirt"
    tutorials = [Tutorial(
        "Ender Magnolia Setup Guide",
        "TODO",
        "English",
        "setup_en.md",
        "",
        [],
    )]

class EnderMagnoliaWorld(World):
    """
    Ender Magnolia: BLOOM IN THE MIST
    """

    game = ENDERMAGNOLIA
    web = EnderMagnoliaWebWorld()

    # options
    options_dataclass = EnderMagnoliaOptions
    options: EnderMagnoliaOptions

    # items
    item_name_to_id = {name: data.code for name, data in items.items()}
    item_name_groups = {group.name: {name for name, data in items.items() if data.group == group}
                        for group in ItemGroup}
    item_name_groups = {group: names for group, names in item_name_groups.items() if names}
    
    # locations
    location_name_to_id = {name: data.address for name, data in locations.items()}
    location_name_groups = {group.name: {name for name, data in locations.items() if data.group == group}
                            for group in LocationGroup}
    location_name_groups = {group: names for group, names in location_name_groups.items() if names}

    def create_item(self, item: str) -> EnderMagnoliaItem:
        return EnderMagnoliaItem.from_name(item, self.player)

    def create_items(self) -> None:
        starting_skill = self.options.starting_skill.get_skill_name()
        self.get_location("Starting Skill").place_locked_item(self.create_item(starting_skill))

        items_pool : List[Item] = []
        remaining = list(pool)
        remaining.remove(items[starting_skill])

        if self.options.central_elevator_fix == CentralElevatorFix.option_key:
            remaining.remove(stats["hp_up_s"])
            remaining.append(custom["Central Stratum Elevator Key"])

        for data in remaining:
            items_pool.append(EnderMagnoliaItem.from_data(data, self.player))
        self.multiworld.itempool.extend(items_pool)

    def create_region(self, name: str) -> Region:
        region = Region(name, self.player, self.multiworld)
        self.multiworld.regions.append(region)
        return region

    def get_parent_region(self, data: LocationData) -> Region:
        if data.region:
            return self.get_region(data.region)
        return self.create_region(data.name)

    def create_location(self, name: str) -> EnderMagnoliaLocation:
        data = locations[name]
        parent_region = self.get_parent_region(data)
        location = EnderMagnoliaLocation(self.player, name, data, parent_region)
        parent_region.locations.append(location)
        return location

    def create_event_location(self, name: str) -> EnderMagnoliaLocation:
        data = event_locations[name]
        parent_region = self.get_parent_region(data)
        location = EnderMagnoliaEvent(self.player, name, parent_region)
        location.place_locked_item(EnderMagnoliaItem.from_data(data.content, self.player))
        parent_region.locations.append(location)
        return location

    def create_regions(self) -> None:
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

        # the shop and one region per shop level
        for name in {dst for _, dst in shop_rules}:
            self.create_region(name)

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

        # connect the shop and its levels
        for (src, dst), rule in shop_rules.items():
            region = self.get_region(src)
            region.add_exits([dst], {dst: rule});


        # connect levy progressive locations
        for (src, dst), rule in levy_rules.items():
            region = self.get_region(src)
            region.add_exits([dst], {dst: rule});

    def set_rules(self) -> None:
        # set items rules
        for location_name, rule in items_rules.items():
            add_item_rule(self.get_location(location_name), rule)

        for name in {dst for _, dst in shop_rules}:
            for slot in self.get_region(name).locations:
                add_item_rule(slot, shop_item_rule)

        # central elevator requirements
        rule = elevator_rules.get(self.options.central_elevator_fix.value)
        if rule is not None:
            location = self.get_location("Street 11 - Street Elevator Fixed")
            for entrance in location.parent_region.entrances:
                self.set_rule(entrance, rule)

        # Goal
        self.set_completion_rule(completion_rule)

    def get_filler_item_name(self) -> str:
        return stats["hp_up_s"].name

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict("central_elevator_fix")

    def generate_output(self, output_directory):
        return
        out_path = os.path.join(output_directory, "EnderMagnolia.Randomizer.Seed.txt")
        output = ""
        locations : List[EnderMagnoliaLocation] = self.multiworld.get_filled_locations();
        for location in locations:
            if isinstance(location, EnderMagnoliaLocation) and location.item and location.key() and location.item.name and location.item.name in items:
                s = f"{location.key()}:{items[location.item.name].key}"
                print(s)
                output += f"{s}\n"

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(output)
