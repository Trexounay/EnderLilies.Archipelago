from dataclasses import dataclass
from typing import Dict, Tuple

from Options import (Choice, DefaultOnToggle, OptionGroup, PerGameCommonOptions, Range,
                     StartInventoryPool, Toggle)

from .Items import skills


class StartingSkill(Choice):
    """
    Determines which skill you start with.
    """

    display_name = "Starting Skill"
    slot_data = True

    option_nola_spirit_piercer = 0
    option_nola_soul_harvester = 1
    option_nola_vanquisher = 2
    option_reibolg_magic_tracer = 3
    option_reibolg_piercing_beam = 4
    option_reibolg_blast_volley = 5
    option_lito_blazing_fist = 6
    option_lito_glacial_fist = 7
    option_lito_rocket_fist = 8
    option_lorna_gravity_field = 9
    option_lorna_light_show = 10
    option_lorna_fire = 11
    option_no7_lunar_manifestation = 12
    option_no7_hail_dance = 13
    option_no7_thunder_flower = 14
    #option_shackled_beast_chain_whip = 15
    #option_shackled_beast_charge = 16
    #option_shackled_beast_benumbed_howl = 17
    option_luiseach_volcanic = 18
    option_luiseach_whirlwind = 19
    option_luiseach_cocytus = 20
    option_huginn_gust_wing = 21
    option_huginn_poison_cloud = 22
    option_huginn_flaming_feather = 23
    #option_muninn_seeker = 24
    #option_muninn_stun = 25
    #option_muninn_bombard = 26
    option_yolvan_barrage = 27
    option_yolvan_lacerate = 28
    option_yolvan_eviscerate = 29

    default = option_nola_spirit_piercer

    def get_skill_name(self) -> str:
        return [*skills][self.value].name


class StartWithFastTravel(DefaultOnToggle):
    """
    Start with Fast Travel instead of shuffling it into the item pool.
    """

    display_name = "Start With Fast Travel"


class StartWithHeal(DefaultOnToggle):
    """
    Start with Healing Ward instead of shuffling it into the item pool.
    """

    display_name = "Start With Healing Ward"


class StartingRespite(Choice):
    """
    Determines the respite you start the game at.
    """

    display_name = "Starting Respite"
    slot_data = True

    regions: Dict[int, Tuple[str, str]] = {
        # work vanilla
        0:  ("sys_init",          "Ruins14Right"),
        1:  ("sys_post_event",    "Ruins04LowerLeft"),
        2:  ("ruins_first",       "Ruins06Right"),
        3:  ("ruins_lab",         "Ruins11Right"),
        # work with 2 sided doors (ruins10, crossroad5, street3, quarry1)
        4:  ("crossroad_camp",    "Crossroad05Left"),
        5:  ("slum_camp",         "Slum01Left"),
        6:  ("street_clocktower", "Street05Left"),
        7:  ("street_towergate",  "Street15Left"),
        8:  ("mine_room1",        "Mine03Lower"),
        9:  ("mine_room2",        "Mine09Right"),
        10: ("mine_room3",        "Mine16Left"),
        12: ("tower_high",        "Tower05Lower"),
        13: ("tower_low",         "Tower13Lower"),
        14: ("tower_gate",        "Tower15Left"),
        15: ("forest_tree",       "Forest02LowerDoor"),
        18: ("swamp_lake",        "Swamp03Left"),
        19: ("swamp_center",      "Swamp07Respite"),
        21: ("quarry_room",       "Quarry13Left"),
        41: ("estate_room",       "Estate06Lower"),
        # work with elevator_key
        24: ("center_bench",      "Center01LeftDoor"),
        27: ("kowlon_room2",      "Kowloon37Left"),
        29: ("garden_room",       "Garden09Left"),
        35: ("paradice_room",     "Paradise10Left"),
        37: ("paradice_room3",    "Paradise07Left"),

        # dont work
        #11: ("sewer_left",        "Sewer10Left"),
        #17: ("forest_village",    "Forest21Left"),
        #20: ("swamp_trash",       "Swamp14Right"),
        #22: ("quarry_room2",      "Quarry09Left"),
        #23: ("quarry_room3",      "Quarry20Left"),
        #25: ("kowlon_room4",      "Kowloon03Left"),
        #26: ("kowlon_room",       "Kowloon23Lower"),
        #28: ("kowloon_room3",     "Kowloon43Left"),
        #30: ("garden_room2",      "Garden04Left"),
        #31: ("garden_room3",      "Garden10Left"),
        #32: ("factory_room",      "Factory03Left"),
        #33: ("factory_room2",     "Factory11Lower"),
        #34: ("factory_room3",     "Factory16Left"),
        #36: ("paradice_room2",    "Paradise31Left"),
        #38: ("labo_room",         "Labo09Left"),
        #39: ("labo_room2",        "Labo12Left"),
        #40: ("labo_room3",        "Labo15Left"),
        #42: ("summit_lobby",      "Summit20CenterDoor"),
        #43: ("summit_last",       "Summit26CenterDoor"),
        #44: ("roots_top",         "Roots07Left"),
        #45: ("roots_left",        "Roots13Lower"),
        #46: ("roots_right",       "Roots26Upper"),
        
        #16: ("forest_bridge",     ""),
    }

    vars().update({f"option_{name}": value for value, (name, _) in regions.items()})

    default = 0

    def get_region(self) -> str:
        return self.regions[self.value][1]

    def requires_elevator(self) -> bool:
        return self.value in {24, 27, 29, 35, 37}


class Goal(Choice):
    """
    Determines the victory condition.

    ending_a: reach ending A
    ending_b: reach ending B
    """

    display_name = "Goal"
    slot_data = True

    option_ending_a = 0
    option_ending_b = 1

    default = option_ending_a


class CentralElevatorFix(Choice):
    """
    Determines requirements to fix the Central Stratum elevator.

    vanilla: same as the original game
    key: find a key shuffled into the item pool
    free: the elevator is already fixed
    """

    display_name = "Central Elevator Fix"
    slot_data = True

    option_vanilla = 0
    option_key = 1
    option_free = 2

    default = option_vanilla


class AdvancedLogic(Toggle):
    """
    Include Nola, No.7, Reibolg and Incomplete Gear in the logic
    """

    display_name = "Advanced Logic"
    slot_data = True

    default = 0


class ProgressiveAptitudes(DefaultOnToggle):
    """
    Aptitudes are acquired in order.
    Dive -> Motley's Torrent
    Lar's Grip -> Lar's Swift Flight
    """

    display_name = "Progressive Aptitudes"
    slot_data = True


class MetaProgression(Toggle):
    """
    Places progression in locations that were just unlocked, so every one you find
    leads directly to the next one.

    Enabling this keeps every progression item inside your own world.
    """

    display_name = "Meta Progression"


class ChapterScaling(Choice):
    """
    Determines how the chapter value moves between Minimum Chapter and Maximum Chapter.

    vanilla: raises difficulty when you reach specific points
    progress: derived from completion, Minimum Chapter at 0% and Maximum Chapter at 100%
    """

    display_name = "Chapter Scaling"
    slot_data = True

    option_vanilla = 0
    option_progress = 1

    default = option_vanilla


class MinChapter(Range):
    """
    Lowest chapter value used to scale the game difficulty.
    """

    display_name = "Minimum Chapter"
    slot_data = True

    range_start = 0
    range_end = 16

    default = 0


class MaxChapter(Range):
    """
    Highest chapter value used to scale the game difficulty.
    """

    display_name = "Maximum Chapter"
    slot_data = True

    range_start = 0
    range_end = 16

    default = 15


class RelicCostShuffle(Toggle):
    """
    Shuffles the equip cost of relics.
    """

    display_name = "Relic Cost Shuffle"
    slot_data = True

    default = 0


class SkillCostShuffle(Toggle):
    """
    Shuffles the materials required to upgrade skills.
    """

    display_name = "Skill Cost Shuffle"
    slot_data = True

    default = 0


class ShuffleSP(Toggle):
    """
    Shuffles Attuner Arts for all skills.
    """

    display_name = "Shuffle Attuner Arts"
    slot_data = True

    default = 0

class ShuffleBGM(Toggle):
    """
    Shuffles the background music tracks.
    """

    display_name = "Shuffle BGM"
    slot_data = True

    default = 0


class GenerateSeedFile(Toggle):
    """
    Also generate a seed file for non-archipelago play.
    """

    display_name = "Generate Seed File"

    default = 0


@dataclass
class EnderMagnoliaOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    starting_skill: StartingSkill
    starting_respite: StartingRespite
    start_with_fast_travel: StartWithFastTravel
    start_with_heal: StartWithHeal
    central_elevator_fix: CentralElevatorFix
    advanced_logic: AdvancedLogic
    progressive_aptitudes: ProgressiveAptitudes
    meta_progression: MetaProgression
    chapter_scaling: ChapterScaling
    min_chapter: MinChapter
    max_chapter: MaxChapter
    relic_cost_shuffle: RelicCostShuffle
    skill_cost_shuffle: SkillCostShuffle
    shuffle_bgm: ShuffleBGM
    shuffle_sp: ShuffleSP
    generate_seed_file: GenerateSeedFile


slot_data_options = [name for name, option in EnderMagnoliaOptions.type_hints.items()
                     if getattr(option, "slot_data", False)]


em_option_groups = [
    OptionGroup("Goal", [
        Goal,
    ]),
    OptionGroup("Starting Setup", [
        StartingSkill,
        StartingRespite,
        StartWithFastTravel,
        StartWithHeal,
    ]),
    OptionGroup("Logic", [
        AdvancedLogic,
        CentralElevatorFix,
        ProgressiveAptitudes,
        MetaProgression,
    ]),
    OptionGroup("Misc", [
        ChapterScaling,
        MinChapter,
        MaxChapter,
        RelicCostShuffle,
        SkillCostShuffle,
        ShuffleBGM,
        ShuffleSP,
        GenerateSeedFile,
    ]),
]
