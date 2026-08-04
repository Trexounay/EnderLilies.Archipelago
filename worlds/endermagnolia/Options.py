from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, OptionGroup, PerGameCommonOptions, Range, Toggle

from .Items import skills


class StartingSkill(Choice):
    """
    Determines which skill you start with.
    """

    display_name = "Starting Skill"

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


class ProgressiveAptitudes(DefaultOnToggle):
    """
    Aptitudes are acquired in order.
    Dive -> Motley's Torrent
    Lar's Grip -> Lar's Swift Flight
    """

    display_name = "Progressive Aptitudes"
    slot_data = True


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


class GenerateSeedFile(Toggle):
    """
    Also generate a seed file for non-archipelago play.
    """

    display_name = "Generate Seed File"

    default = 0


@dataclass
class EnderMagnoliaOptions(PerGameCommonOptions):
    goal: Goal
    starting_skill: StartingSkill
    start_with_fast_travel: StartWithFastTravel
    start_with_heal: StartWithHeal
    central_elevator_fix: CentralElevatorFix
    progressive_aptitudes: ProgressiveAptitudes
    min_chapter: MinChapter
    max_chapter: MaxChapter
    relic_cost_shuffle: RelicCostShuffle
    generate_seed_file: GenerateSeedFile


slot_data_options = [name for name, option in EnderMagnoliaOptions.type_hints.items()
                     if getattr(option, "slot_data", False)]


option_groups = [
    OptionGroup("Goal", [
        Goal,
    ]),
    OptionGroup("Starting Setup", [
        StartingSkill,
        StartWithFastTravel,
        StartWithHeal,
    ]),
    OptionGroup("Logic", [
        CentralElevatorFix,
        ProgressiveAptitudes,
    ]),
    OptionGroup("Misc", [
        MinChapter,
        MaxChapter,
        RelicCostShuffle,
        GenerateSeedFile,
    ]),
]
