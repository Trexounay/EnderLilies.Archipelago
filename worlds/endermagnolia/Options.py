from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions

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
    option_shackled_beast_chain_whip = 15
    option_shackled_beast_charge = 16
    option_shackled_beast_benumbed_howl = 17
    option_luiseach_volcanic = 18
    option_luiseach_whirlwind = 19
    option_luiseach_cocytus = 20
    option_huginn_gust_wing = 21
    option_huginn_poison_cloud = 22
    option_huginn_flaming_feather = 23
    option_muninn_seeker = 24
    option_muninn_stun = 25
    option_muninn_bombard = 26
    option_yolvan_barrage = 27
    option_yolvan_lacerate = 28
    option_yolvan_eviscerate = 29

    default = option_nola_spirit_piercer

    def get_skill_name(self) -> str:
        return [*skills][self.value].name


class CentralElevatorFix(Choice):
    """
    Determines requirements to fix the Central Stratum elevator.

    vanilla: same as the original game
    key: find a key shuffled into the item pool
    free: the elevator is already fixed
    """

    display_name = "Central Elevator Fix"

    option_vanilla = 0
    option_key = 1
    option_free = 2

    default = option_vanilla


@dataclass
class EnderMagnoliaOptions(PerGameCommonOptions):
    starting_skill: StartingSkill
    central_elevator_fix: CentralElevatorFix


option_groups = [
    OptionGroup("Starting Setup", [
        StartingSkill,
    ]),
    OptionGroup("Logic", [
        CentralElevatorFix,
    ]),
]
