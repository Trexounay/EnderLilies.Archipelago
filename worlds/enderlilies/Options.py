from worlds.AutoWorld import World
from BaseClasses import Item, Location, Dict
from typing import Dict, Tuple, Type, List
from dataclasses import dataclass
from Options import Choice, Option, DefaultOnToggle, Toggle, Range, PerGameCommonOptions
from .Names import names as el
from .StartingLocations import startingLocationsData

options: Dict[str, Option] = {}

# decorator to autofill options
def option(name: str):

    @classmethod
    def get_option(cls, world: World) -> Option:
        return getattr(world, cls.name)

    def decorator(cls: Type[Option]) -> Type[Option]:
        cls.name = name
        cls.get_option = get_option
        options[name] = cls
        return cls

    return decorator


@option("starting_spirit")
class StartingSpirit(Choice):
    """Defines the spirit you start with, starting spirit will have infinite usage.
    default: Any Main Spirit"""

    display_name = "Starting spirit"

    option_any_main_spirit = 26
    option_any_sub_spirit = 27

    option_umbral = 0
    option_gerrod = 1
    option_silva = 2
    option_julius = 3
    option_ulv = 4
    option_eleine = 5
    option_hoenir = 6
    option_faden = 7

    option_siegrid = 8
    option_youth = 9
    option_defender = 10
    option_bird = 11
    option_dog = 12
    option_archer = 13
    option_crypt = 14
    option_fungal = 15
    option_floral = 16
    option_sentinel = 17
    option_subject = 18
    option_executionner = 19
    option_sinner = 20
    option_champion = 21
    option_elder = 22
    option_chief = 23
    option_aegis = 24
    option_fellwyrm = 25

    spirits = [
        # Main Spirits
        "Umbral Knight",
        "Gerrod, the Elder Warrior",
        "Guardian Silva",
        "Knight Captain Julius",
        "Ulv, the Mad Knight",
        "Dark Witch Eleine",
        "Hoenir, Keeper of the Abyss",
        "Faden, the Heretic",
        # Sub Spirits
        "Guardian Siegrid",
        "Cliffside Hamlet Youth",
        "Headless Defender",
        "Western Merchant",
        "Castle Town Maiden",
        "Fallen Archer",
        "Elder Crypt Keeper",
        "Fungal Sorcerer",
        "Floral Sorceress",
        "Fallen Sentinel",
        "Hidden Test Subject",
        "Dark Executioner",
        "Incompetent Sinner",
        "Verboten Champion",
        "Cliffside Hamlet Elder",
        "Chief Guardian",
        "One-Eyed Royal Aegis",
        "Forsaken Fellwyrm",
    ]

    default = option_any_main_spirit
    def get_starting_weapon_pool(self) -> List[str]:
        if self.value == StartingSpirit.option_any_main_spirit:
            return StartingSpirit.spirits[:8]
        elif self.value == StartingSpirit.option_any_sub_spirit:
            return StartingSpirit.spirits[8:]
        else:
            return StartingSpirit.spirits[self.value]


@option("starting_location")
class StartingLocation(Choice):
    """Defines where you start the game.
    default: Start"""

    display_name = "Starting location"

    option_start = 0
    option_cellar = 3
    option_cathedral_cloister = 5
    option_saints_passage = 9
    option_crossroads = 12

    option_collapsed_shack = 19
    option_bridgehead = 23

    option_ruined_castle_cellar = 35
    option_guest_chamber = 38
    option_maelstrom_remparts = 41

    option_bastion_gates = 55
    option_courtyard = 61
    option_second_spire_chamber = 62
    option_mourninghall = 72

    option_dryad_lake = 78
    option_witchs_hermitage = 83
    option_covenhalls = 87

    option_bottom_of_the_well = 91
    option_charnel = 93
    option_ossuary = 103
    option_great_hall = 106

    option_aqueduct = 115
    option_cells = 123
    option_dark_chamber = 132
    option_execution_grounds = 138

    option_lab1 = 145
    option_lab2 = 150

    default = option_start

    def get_starting_location(self) -> str:
        return el[startingLocationsData[self.value].clientKey]


@option("item_pool_priority")
class ItemPoolPriority(Choice):
    """Defines what items will be kept in the pool when there are more items than locations left
    Useful: Give priority to useful items over filler (Default).
    Any: Priority is the same for any non-progression items.
    All: Leave all items in the pool and let Archipelago pick"""

    display_name = "Prioritize Useful Items"
    option_any = 0
    option_useful = 1
    option_all = 2
    default = option_useful

    def sort_items_list(self, items: List[Item], locations_count: int) -> List[Item]:
        def item_score(item: Item) -> int:
            if item.advancement:
                return 2
            if item.useful and self.value == ItemPoolPriority.option_useful:
                return 1
            return 0

        if self.value == ItemPoolPriority.option_all:
            return items
        items.sort(key=item_score, reverse=True)
        return items[:locations_count]


@option("goal")
class Goal(Choice):
    """Goal to complete for Archipelago
    Ending A - Benevolence.
    Ending B - Journey's End.
    Ending C - Dawn Prayer. (Default)
    Any Ending: Achieving any Ending."""

    display_name = "Goal"
    option_ending_a = 0
    option_ending_b = 1
    option_ending_c = 2
    option_any_ending = 3
    default = option_ending_c

    def get_victory_locations(self) -> List[str]:
        if self.value == Goal.option_ending_a:
            return ["Ending_A"]
        elif self.value == Goal.option_ending_b:
            return ["Ending_B"]
        elif self.value == Goal.option_ending_c:
            return ["Ending_C"]
        else:
            return ["Ending_A", "Ending_B", "Ending_C"]

# This option might not work as intended with room randomizer. 
@option("early_maneuver")
class EarlyManeuver(Choice):
    """Defines if a maneuver item, e.g. claw, should be placed early. 
    The goal of this option is to reduce possibility of early BK.

    local: Ensure that a maneuver item is in sphere 1 of the EL player.
    global: Ensure that a maneuver item is in sphere 1 of any player in the multiworld.
    none: Do nothing. (Default) """
    display_name = "Force early maneuver"
    option_none = 0
    option_local = 1
    option_global = 2

    default = option_none

    def get_early_maneuver(self, startLocationId) -> List[str]:
        # Only called if needed
        return [el[item] for item in startingLocationsData[startLocationId].earlyManeuverItems]
        

@option("shuffle_slots")
class ShuffleRelicsCosts(Toggle):
    """Shuffle the how many slots you need to equip each relics
    default: Off"""

    display_name = "Shuffle relics costs"

@option("minibosses_chapter")
class SubSpiritsIncreaseChapter(Toggle):
    """Increase the game difficulty whenever you defeat a Sub Spirit in Addition to Main Bosses
    default: Off"""

    display_name = "Sub-spirits chapters"

@option("ng_plus")
class NewGamePlusAI(Toggle):
    """Use NG+ AI for enemies with new patterns behaviours
    default: Off"""

    display_name = "NG+ AI"

@option("shuffle_upgrades")
class ShuffleSpiritsUpgrades(Toggle):
    """Shuffle what currency is required to upgrade each weapon
    default: Off"""

    display_name = "Shuffle spirits upgrades"

@option("force_ancient_souls")
class StartingWeaponUsesAncientSouls(Toggle):
    """Upgrading your starting spirit will require ancient souls
    default: Off"""

    display_name = "Starter uses ancient souls"

@option("shuffle_bgm")
class ShuffleBGM(Toggle):
    """Each room will have a random music from the BGM list
    default: Off"""

    display_name = "Random background music"

@option("start_chapter")
class ChapterMin(Range):
    """Defines starting chapter difficulty
    default: 1"""
    range_start = 1
    range_end = 10
    default = 1
    display_name = "Starting chapter"

@option("max_chapter")
class ChapterMax(Range):
    """Defines max chapter difficulty that you can reach during gameplay
    default: 10"""
    range_start = 1
    range_end = 10
    default = 10
    display_name = "Max chapter"
    
@option("stone_tablets_placement")
class StoneTabletsPlacement(Choice):
    """any: Stone tablets can be anywhere. (Default)
    region: Force stone tablet to be placed locally one in each main regions."""

    option_any = 0
    option_region = 1
    default = option_any
    display_name = "Stone tablets placement"
    regions = ['Ruined Castle', 'Catacombs', "Witch's Thicket", ('Twin Spires', 'Hinterlands'), 'Stockade', ('Verboten Domain', 'The Abyss'), 'Cliffside Hamlet']

    @classmethod
    def place_tablets_in_regions(cls, tablets_locations : List[Location], locations : List[Location]) -> List[Tuple[Location, Location]]:
        locations = tablets_locations + locations
        new_locations: List[Location]  = [next((location for location in locations if location.name.startswith(region))) for region in StoneTabletsPlacement.regions]
        tablet_to_swap = [location for location in tablets_locations if location not in new_locations]
        new_locations = [location for location in new_locations if location not in tablets_locations]
        return [(tablet_to_swap[i], new_locations[i]) for i in range(len(tablet_to_swap))]

@option("add_unused_items")
class AddUnusedItems(Toggle):
    """Add 7 unused relics and a +50HP jewel to the items pool
    default: Off"""

    display_name = "Add unused items"

# not implemented yet
#@option("dash_before_lance")
class DashBeforeLance(DefaultOnToggle):
    """Make Piercing Lance a progression of Dash meaning you will always find Dash first
    default: On"""

    display_name = "Dash before lance"
    
@option("entrance_randomizer")
class RandomizeEntrances(Toggle):
    """Randomize every room entrances and exits,
    ensure transitions are two-ways so you can go back and forth
    default: Off"""

    display_name = "Randomize Entrances"


@dataclass
class EnderLiliesGameOptions(PerGameCommonOptions):
    starting_spirit: StartingSpirit
    starting_location: StartingLocation
    item_pool_priority: ItemPoolPriority
    goal: Goal
    early_maneuver: EarlyManeuver
    shuffle_slots: ShuffleRelicsCosts
    minibosses_chapter: SubSpiritsIncreaseChapter
    ng_plus: NewGamePlusAI
    shuffle_upgrades: ShuffleSpiritsUpgrades
    force_ancient_souls: StartingWeaponUsesAncientSouls
    shuffle_bgm: ShuffleBGM
    start_chapter: ChapterMin
    max_chapter: ChapterMax
    stone_tablets_placement: StoneTabletsPlacement
    add_unused_items: AddUnusedItems
    # dash_before_lance: DashBeforeLance
    entrance_randomizer: RandomizeEntrances
