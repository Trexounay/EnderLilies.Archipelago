from worlds.AutoWorld import World, WebWorld
from BaseClasses import ItemClassification, Region, Item, Location, Type, Tutorial
from worlds.generic.Rules import set_rule, add_item_rule
from typing import Any, Dict, List, Optional, TextIO, Union
from Options import Option
from Fill import swap_location_item

from .Items import ItemData, items
from .Locations import LocationData, locations
from .Rules import get_rules
from .Options import *
from .Regions import regions as regions_list, entrances, indirect_connections

from .EntranceRandomizer import EntranceRandomizer

ENDERLILIES = "Ender Lilies"

class EnderLiliesWeb(WebWorld):
    setup_en = Tutorial(
        "Multiworld Setup Tutorial",
        "A guide to setting up the Ender Lilies randomizer connected to an Archipelago Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Neocerber", "Trex", "Lurch9229"]
    )

    theme = "partyTime"

    tutorials = [setup_en]


class EnderLiliesEvent(Item):
    game = ENDERLILIES

    def key(self):
        return self.name

class EnderLiliesItem(Item):
    game = ENDERLILIES
    data : ItemData

    def __init__(self, name: str, data : ItemData, player: int):
        super().__init__(name, data.classification, data.code, player)
        self.data = data

    def key(self):
        return self.data.key

class EnderLiliesLocation(Location):
    game = ENDERLILIES
    data : LocationData

    def __init__(self, player: int, name: str, data : LocationData, parent: Optional[Region] = None):
        super().__init__(player, name, data.address, parent)
        self.data = data

    def key(self):
        return self.data.key


class EnderLiliesWorld(World):
    """
    Ender Lilies: QUIETUS OF THE KNIGHTS
    """

    game = ENDERLILIES
    web = EnderLiliesWeb()
    # option_definitions = options
    options_dataclass = EnderLiliesGameOptions
    options: EnderLiliesGameOptions
    location_name_to_id = {name: data.address for name, data in locations.items()}
    item_name_to_id = {name: data.code for name, data in items.items()}
    
    randomized_entrances : Dict[str, str] = {}

    def generate_early(self):
        early_maneuver_opt = self.get_option(EarlyManeuver)
        if early_maneuver_opt.value != 0:
            # Maneuver items of interest depends on starting location
            maneuver_items = early_maneuver_opt.get_early_maneuver(
                                                      self.get_option(StartingLocation))
            if early_maneuver_opt.value == 1:
                non_local_items = self.options.non_local_items.value
                avail_local_maneuver = [item for item in maneuver_items 
                                          if item not in non_local_items]
                item_name = self.random.choice(avail_local_maneuver)
                self.multiworld.local_early_items[self.player][item_name] = 1
            elif early_maneuver_opt.value == 2:
                item_name = self.random.choice(maneuver_items)
                self.multiworld.early_items[self.player][item_name] = 1

    def create_item(self, item: str) -> EnderLiliesItem:
        if item in self.item_name_to_id:
            item_object = EnderLiliesItem(item, items[item], self.player)
        else:
            item_object = EnderLiliesEvent(item, ItemClassification.progression, None, self.player)
        return item_object

    def create_items(self) -> None:
        starting_items = self.assign_starting_items()

        pool = []
        for item, data in items.items():
            if item in starting_items or data.unused and not self.get_option(AddUnusedItems):
                continue
            for i in range(data.count):
                pool.append(self.create_item(item))
        unfilled_location = self.multiworld.get_unfilled_locations(self.player)
        self.random.shuffle(pool)
        pool : List[EnderLiliesItem] = self.get_option(ItemPoolPriority).sort_items_list(pool, len(unfilled_location))

        if self.get_option(StoneTabletsPlacement).value == StoneTabletsPlacement.option_region:
            self.multiworld.local_items[self.player].value.add("Stone Tablet Fragment")
            for item in pool:
                if item.name == 'Stone Tablet Fragment':
                    item.classification = ItemClassification.progression_skip_balancing

        self.multiworld.itempool.extend(pool)

    def create_regions(self) -> None:
        victory_locations = self.get_option(Goal).get_victory_locations()
        starting_location = self.get_option(StartingLocation).get_starting_location()
        
        self.randomized_entrances = {}
        if self.get_option(RandomizeEntrances):
            er = EntranceRandomizer(starting_location)
            portals = er.get_portals()
            self.random.shuffle(portals)
            self.randomized_entrances = er.Randomize(portals)
        connections : List[Tuple[Region, str, str]] = []

        regions : Dict[str, Region]= {
            "Menu" : Region("Menu", self.player, self.multiworld),
        }
        starting_spirit = EnderLiliesLocation(self.player, "Starting Spirit", locations["Starting Spirit"], regions["Menu"])
        regions["Menu"].locations.append(starting_spirit)

        # 1 region per room
        for region_name, region_locations in regions_list.items():
            regions[region_name] = Region(region_name, self.player, self.multiworld)

        # 1 region per room entrance
        for entrance, region_name in entrances.items():
           regions[entrance] = Region(entrance, self.player, self.multiworld)
           regions[entrance].connect(regions[region_name])

        rules, _ = get_rules(self.player)
        for region_name, region_locations in regions_list.items():
            for location in region_locations:
                if location == starting_location:
                    regions["Menu"].connect(regions[region_name])
                if locations[location].content and locations[location].content in entrances:
                    if location in self.randomized_entrances:
                        destination_name = self.randomized_entrances[location]
                    else:
                        destination_name = locations[location].content
                    region_exit = regions[region_name].connect(regions[destination_name], location, rules[location])
                    if location in indirect_connections:
                        for indirect_regions in indirect_connections[location]:
                            self.multiworld.register_indirect_condition(regions[indirect_regions], region_exit)
                else:
                    check = EnderLiliesLocation(self.player, location, locations[location], regions[region_name])
                    regions[region_name].locations.append(check)
                    if check.data.address:
                        continue
                    check.show_in_spoiler = False
                    if location in victory_locations:
                        check.place_locked_item(self.create_item("Victory"))
                    else:
                        check.place_locked_item(self.create_item(check.data.content))

        self.multiworld.regions.extend([region for name, region in regions.items()])

    def post_fill(self) -> None:
        if self.get_option(StoneTabletsPlacement) == StoneTabletsPlacement.option_region:
            tablets_locations : List[Location]  = self.multiworld.find_item_locations(el["tablet"], self.player)
            tablet : EnderLiliesItem = tablets_locations[0].item
            valid_locations : List[Location]  = [location for location in self.multiworld.get_locations(self.player) if not location.locked and location.can_fill(self.multiworld.state, tablet) and location.item == None or not location.item.advancement]
            self.random.shuffle(valid_locations)
            swaps : List[Tuple[Location, Location]] = StoneTabletsPlacement.place_tablets_in_regions(tablets_locations, valid_locations)
            for swap in swaps:
                swap_location_item(swap[0], swap[1], True)
        return super().post_fill()

    def set_rules(self) -> None:
        locations_rules, items_rules = get_rules(self.player)

        for name, rule in locations_rules.items():
            if locations[name].content in entrances:
                continue
                location = self.multiworld.get_entrance(name, self.player)
            else:
                location = self.multiworld.get_location(name, self.player)
            set_rule(location, rule)
        for name, rule in items_rules.items():
            add_item_rule(self.multiworld.get_location(name, self.player), rule)

        starting_location = self.get_option(StartingLocation).get_starting_location()
        set_rule(self.multiworld.get_location(starting_location, self.player), lambda s : True)

        self.multiworld.completion_condition[self.player] = lambda state: state.has(
            "Victory", self.player
        )

#    def generate_basic(self) -> None:
#        from Utils import visualize_regions
#        visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")
#        return super().generate_basic()

    def fill_slot_data(self) -> Dict[str, Any]:
        # Content that will be send to the game
        slot_data: Dict[str, Any] = {}

        # Data for LiveSplit
        slot_data['AP.victory'] = self.get_option(Goal).get_victory_locations()
        slot_data['AP.key_to_address'] = {data.key: data.address  for _, data in locations.items() if data.address and data.key}
        slot_data['AP.key_to_code'] = {data.key: data.code for _, data in items.items() if data.code and data.key}

        # Data that will be in the seed file
        slot_data["SEED"] = str(self.multiworld.seed)
        if self.get_option(ShuffleRelicsCosts):
            slot_data[f'SETTINGS:{ShuffleRelicsCosts.name}'] = None
        if self.get_option(SubSpiritsIncreaseChapter):
            slot_data[f'SETTINGS:{SubSpiritsIncreaseChapter.name}'] = None
        if self.get_option(NewGamePlusAI):
            slot_data[f'SETTINGS:NG+'] = None
        if self.get_option(ShuffleSpiritsUpgrades):
            slot_data[f'SETTINGS:{ShuffleSpiritsUpgrades.name}'] = None
        if self.get_option(StartingWeaponUsesAncientSouls):
            slot_data[f'SETTINGS:{StartingWeaponUsesAncientSouls.name}'] = None
        if self.get_option(ShuffleBGM):
            slot_data[f'SETTINGS:{ShuffleBGM.name}'] = None
        if self.get_option(ChapterMin).value != ChapterMin.default:
            slot_data[f'SETTINGS:{ChapterMin.name}'] = str(self.get_option(ChapterMin).value)
        if self.get_option(ChapterMax).value != ChapterMax.default:
            slot_data[f'SETTINGS:{ChapterMax.name}'] = str(self.get_option(ChapterMax).value)
        slot_data["SETTINGS:starting_room"] = str(self.get_option(StartingLocation).value)
        for location in self.multiworld.get_locations(self.player):
            if location.show_in_spoiler:
                if location.item.player == self.player:
                    slot_data[location.key()] = f"{location.item.key()}"
                else:
                    slot_data[location.key()] = f"AP.{self.multiworld.player_name[location.item.player]}|{location.item.game}|{location.item.name}"
        for location_name, entrance in self.randomized_entrances.items():
            slot_data[locations[location_name].key] = entrance
        return slot_data

    def get_option(self, option: Union[str, Type[Option]]) -> Option:
        # if self.multiworld is None:
        #     return option.default
        if isinstance(option, str):
            return self.options.__getattribute__(option)
        return self.options.__getattribute__(option.name)

    def get_filler_item_name(self) -> str:
        return "nothing"

    def assign_starting_items(self) -> List[str]:
        weapon_name = self.get_option(StartingSpirit).get_starting_weapon_pool()
        if isinstance(weapon_name, list):
            weapon_name = self.random.choice(weapon_name)
        starting_weapon = self.create_item(weapon_name)
        self.multiworld.get_location("Starting Spirit", self.player).place_locked_item(starting_weapon)
        return [weapon_name]

    def write_spoiler(self, spoiler_handle: TextIO) -> None:
        super().write_spoiler(spoiler_handle)
        if len(self.randomized_entrances):
            key_to_names = {key : name for name, key in el.items()}
            spoiler_handle.write(f"\n\nEntrance Randomizer ({self.multiworld.player_name[self.player]}):\n\n")
            spoiler_handle.writelines([f"{location_name}: {key_to_names[entrance]}\n" for location_name, entrance in self.randomized_entrances.items()])
