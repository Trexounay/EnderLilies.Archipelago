import json
import os

from worlds.AutoWorld import World
from BaseClasses import ItemClassification, Region, Item, Location
from worlds.generic.Rules import set_rule, add_item_rule
from typing import Any, Dict

from .Items import items
from .Locations import locations
from .Rules import get_rules
from .Names import names as el

ENDERLILIES = "Ender Lilies"

class EnderLiliesItem(Item):
    game = ENDERLILIES

class EnderLiliesLocation(Location):
    game = ENDERLILIES

class EnderLiliesWorld(World):
    """
    Ender Lilies: QUIETUS OF THE KNIGHTS
    """
    game                = ENDERLILIES
    location_name_to_id = { name: data.address for name, data in locations.items() }
    item_name_to_id     = { name: data.code for name, data in items.items() }

    def create_item(self, item: str) -> EnderLiliesItem:
        if item in self.item_name_to_id:
            return EnderLiliesItem(item, items[item].classification, items[item].code, self.player)
        else:
            return EnderLiliesItem(item, ItemClassification.progression, None, self.player)

    def create_items(self) -> None:
        for item, data in items.items():
            for i in range(data.count):
                self.multiworld.itempool.append(self.create_item(item))

    def create_regions(self) -> None:
        regions = {
            'Menu' : Region('Menu', self.player, self.multiworld),
            'Game' : Region('Game', self.player, self.multiworld),
        }        
        self.multiworld.regions.extend(regions.values())
        regions["Menu"].connect(regions["Game"])
        for location, data in locations.items():
            check = EnderLiliesLocation(self.player, location, data.address, regions["Game"])
            if not data.address:
                check.place_locked_item(self.create_item(data.content))
                check.show_in_spoiler = False
            regions["Game"].locations.append(check)


    def set_rules(self) -> None:
        locations_rules, items_rules = get_rules(self.player)
        player = self.player        

        can_contain_map = lambda item : item.player == player and item.name.startswith('Map.')
        cannot_contain_map = lambda item : item.name.startswith('Map.') == False

        for name, rule in locations_rules.items():
            set_rule(self.multiworld.get_location(name, self.player), rule)
        for name, rule in items_rules.items():
            add_item_rule(self.multiworld.get_location(name, self.player), rule)

        set_rule(self.multiworld.get_location(el['Start'], self.player), lambda state : True)
        self.multiworld.completion_condition[self.player] = lambda state: state.has(el["Abyss03Left"], self.player)

    def generate_output(self, output_directory: str) -> None:
        filename = f"{self.multiworld.get_player_name(self.player)}.EnderLiliesSeed.txt"
        with open(os.path.join(output_directory, filename), 'w') as f:
            print(f"SEED:{self.multiworld.seed}", file=f)
            for location in self.multiworld.get_locations(self.player):
                if location.show_in_spoiler:
                    if location.item.player == self.player:
                        print(f"{location.name}:{location.item.name}", file=f)
                    else:
                        print(f"{location.name}:AP.{location.address}", file=f)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {}
        slot_data["SEED"] = str(self.multiworld.seed)
        for location in self.multiworld.get_locations(self.player):
            if location.show_in_spoiler:
                if location.item.player == self.player:
                    slot_data[location.name] = f"{location.item.name}"
                else:
                    slot_data[location.name] = f"AP.{location.address}"
        return slot_data
    
    def get_name_string_for_object(self, obj) -> str:
        name = obj.name
        if name in el:
            name = el[name]
        return name if self.players == 1 else f'{name} ({self.get_player_name(obj.player)})'
