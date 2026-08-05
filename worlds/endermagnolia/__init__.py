import os
from typing import Any, List, Mapping, Optional, Tuple
from BaseClasses import Item, ItemClassification, Region, Tutorial
from rule_builder.rules import False_
from worlds.AutoWorld import WebWorld, World
from worlds.generic.Rules import add_item_rule

from .Locations import LocationData, LocationGroup, locations, event_locations
from .Options import CentralElevatorFix, EnderMagnoliaOptions, Goal, slot_data_options
from .Regions import room_connections
from .Items import (ItemData, ItemGroup, aptitudes, currencies, custom, items, passives, pool,
                    progressive_chains, quests, stats)
from .Rules import completion_rules, elevator_rules, items_rules, levy_rules, shop_rules, shop_item_rule
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
    #topology_present = True

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

    def generate_early(self) -> None:
        if (self.options.starting_respite.requires_elevator()
                and self.options.central_elevator_fix == CentralElevatorFix.option_vanilla):
            self.options.central_elevator_fix.value = CentralElevatorFix.option_free

    def create_item(self, item: str) -> EnderMagnoliaItem:
        return EnderMagnoliaItem.from_name(item, self.player)

    def create_items(self) -> None:
        removed: List[ItemData] = []
        added: List[ItemData] = []
        placed: List[Tuple[ItemData, str]] = []
        precollected: List[ItemData] = []
        
        starting_skill = self.options.starting_skill.get_skill_name()
        placed.append((items[starting_skill], "Starting Skill"))

        if self.options.goal == Goal.option_ending_b:
            placed.append((passives["ending_flag"], "Roots 2 - Lilia's Blighted Ring"))
            placed.append((quests["quest_amulet"], "Center 4 - Faintly Glowing Aegis Curio"))

        if self.options.start_with_fast_travel:
            precollected.append(aptitudes["fast_travel"])

        if self.options.start_with_heal:
            precollected.append(aptitudes["heal"])

        if self.options.central_elevator_fix == CentralElevatorFix.option_key:
            added.append(custom["Grand Lift Key"])

        if self.options.progressive_aptitudes:
            for name, chain in progressive_chains.items():
                removed.extend(items[aptitude] for aptitude in chain)
                added.extend(custom[name] * len(chain))

        for data, location in placed:
            item = EnderMagnoliaItem.from_data(data, self.player)
            item.classification = ItemClassification.progression
            self.get_location(location).place_locked_item(item)

        for data in precollected:
            self.multiworld.push_precollected(EnderMagnoliaItem.from_data(data, self.player))

        removed.extend(data for data, _ in placed)
        removed.extend(precollected)

        remaining = list(pool)
        for data in removed:
            remaining.remove(data)
        remaining.extend(added)

        items_pool = [EnderMagnoliaItem.from_data(data, self.player) for data in remaining]
        items_pool.extend(self.create_filler()
                          for _ in range(len(self.multiworld.get_unfilled_locations(self.player)) - len(items_pool)))
        self.multiworld.itempool.extend(items_pool)

    def collect_item(self, state, item: Item, remove: bool = False) -> Optional[str]:
        chain = progressive_chains.get(item.name)
        if chain is None:
            return super().collect_item(state, item, remove)
        if remove:
            chain = reversed(chain)
        for name in chain:
            if state.has(name, self.player) == remove:
                return name
        return None

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
        menu = self.create_region("Menu")
        for name in room_connections:
            self.create_region(name)

        # connect transitions together (room1 <-> room2)
        for name, region_data in room_connections.items():
            region = self.get_region(name)
            region.add_exits(region_data.get_exits())
 
        # connect the menu to the starting respite
        menu.add_exits({self.options.starting_respite.get_region(): "Start"})

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
            region = self.get_location("Street 11 - Street Elevator Fixed").parent_region
            for entrance in region.entrances:
                self.set_rule(entrance, False_())
            self.get_region("Menu").add_exits([region.name], {region.name: rule})

        # Goal
        self.set_completion_rule(completion_rules[self.options.goal.value])

    def get_filler_item_name(self) -> str:
        return currencies["Default"].name

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(*slot_data_options)

    def generate_output(self, output_directory):
        if not self.options.generate_seed_file:
            return

        out_path = os.path.join(output_directory, "seed.txt")
        output = f"seed:{self.multiworld.seed}\n"

        for name, value in self.options.as_dict(*slot_data_options).items():
            output += f"option.{name}:{int(value)}\n"

        locations : List[EnderMagnoliaLocation] = self.multiworld.get_filled_locations(self.player);
        for location in locations:
            if not isinstance(location, EnderMagnoliaLocation) or not location.item or not location.key():
                continue
            item = location.item
            if item.player == self.player:
                if item.name not in items:
                    continue
                value = items[item.name].key
            else:
                player_name = self.multiworld.get_player_name(item.player)
                value = f"{item.name}|{player_name}|{self.multiworld.worlds[item.player].game}"
            output += f"{location.key()}:{value}\n"

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(output)
