from typing import List, Optional, Dict
from enum import Enum, IntFlag
from dataclasses import dataclass, field

try:
    from BaseClasses import ItemClassification as IC
except ImportError:
    class IC(IntFlag):
        filler = 0
        progression = 1
        useful = 2
        trap = 4
        skip_balancing = 8
        deprioritized = 16

class   ItemGroup(Enum):
    Aptitude = 1
    Assist = 2
    Costume = 3
    Currency = 4
    Equipment = 5
    Quest = 6
    Key = 7
    Material = 8
    Passive = 9
    Skill = 10
    Spirit = 11
    Stat = 12
    Tip = 13

@dataclass
class ItemData():
    name: str
    key: Optional[str] = None
    code: Optional[int] = None
    group: Optional[ItemGroup] = None
    classification: IC = IC.filler
    
    def __rmul__(self, other):
        return [self for _ in range(other)]

    def __mul__(self, other):
        return [self for _ in range(other)]

class EventData(ItemData):
    def __init__(self, key, name):
        super().__init__(name, key, classification=IC.progression)

@dataclass()
class DataTable():
    name: str
    group: ItemGroup
    code: int
    rows: Dict[str, str]
    classification: IC = IC.useful
    codes: Dict[str, int] = field(init=False)
    _items: Dict[str, ItemData] = field(init=False)

    def __post_init__(self):
        code = self.code
        self.codes = {}
        self._items = {}
        for entry in self.rows:
            self.codes[entry] = code
            code += 1

    def __getitem__(self, entry) -> ItemData:
        if entry not in self._items:
            self._items[entry] = ItemData(self.rows[entry], self.name + "." + entry, self.codes[entry], self.group, self.classification)
        return self._items[entry]

    def __len__(self) -> int:
        return len(self.rows)

    def __iter__(self):
        for entry in self.rows:
            yield self[entry]

@dataclass()
class CustomTable():
    code: int
    rows: Dict[str, tuple]
    classification: IC = IC.progression
    _items: Dict[str, ItemData] = field(init=False)

    def __post_init__(self):
        code = self.code
        self._items = {}
        for name, (key, group) in self.rows.items():
            self._items[name] = ItemData(name, key, code, group, self.classification)
            code += 1

    def __getitem__(self, name) -> ItemData:
        return self._items[name]

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items.values())
        
aptitudes = DataTable("DT_ItemAptitudes", group=ItemGroup.Aptitude, classification=IC.progression, code=1000,rows = 
{
#    "Crouch"                 : "Crouch",
#    "Jump"                   : "Jump",
#    "dash"                   : "Sprint",
#    "dodge_weak"             : "Roll",
    "fast_travel"            : "Fast Travel",
    "hook"                   : "Motley's Magic Strands",
    "SP"                     : "Attuner Arts",
    "dash_charge"            : "Hati's Charge",
    "dash_charge_underwater" : "Motley's Torrent",
    "dive"                   : "Dive",
    "dodge"                  : "Dodge",
    "double_jump"            : "Aerial Jump",
    "heal"                   : "Healing Ward",
    "high_jump"              : "Garm's Ascent",
    "pile_attack"            : "Garm's Iron Stake",
    "wall_charge"            : "Lar's Swift Flight",
    "wall_grab"              : "Lar's Grip",
})

assists = DataTable("DT_ItemAssists", group=ItemGroup.Assist, code=2000,rows = 
{
    "assist_001" : "Krios",
    "assist_002" : "Taurus",
    "assist_003" : "Gemini",
    "assist_004" : "Carcinus",
    "assist_005" : "Regulus",
    "assist_006" : "Spica",
    "assist_007" : "Lyra",
    "assist_008" : "Ares",
    "assist_009" : "Chiron",
    "assist_010" : "Typhon",
    "assist_011" : "Ilion",
    "assist_012" : "Cetus",
})

costumes = DataTable("DT_ItemCostumes", group=ItemGroup.Costume, classification=IC.filler, code=3000,rows = 
{
    "p0000" : "Sorcerer's Academy Uniform",
    "p0010" : "Azure Mantle",
    "p0011" : "Attuner's Mantle Ex",
    "p0020" : "Attuner's Mantle",
    "p0021" : "Attuner's Mantle Ex 2",
    "p0030" : "Mantle of Milius",
    "p0031" : "Mantle of Milius Ex",
    "p0040" : "Levy's Mantle",
    "p0041" : "Levy's Mantle Ex",
    "p0042" : "Levy's Mantle Ex 2",
    "p0050" : "White Priestess' Attire",
    "p0051" : "White Priestess' Attire Ex",
    "p0060" : "Land's End Priestess Garb",
})

currencies = DataTable("DT_ItemCurrencies", classification=IC.filler, group=ItemGroup.Currency, code=4000,rows = 
{
    "Default" : "Materials",
    "grade"   : "Fragments",
    "rare"    : "Scrap",
})

equipments = DataTable("DT_ItemEquipments", group=ItemGroup.Equipment, code=5000,rows = 
{
    "armor_001"  : "Worn Bangle",
    "armor_002"  : "Crude Bangle",
    "armor_003"  : "Thistle Bangle",
    "armor_004"  : "Stone Bangle",
    "armor_005"  : "Bone Bangle",
    "armor_006"  : "Dagger Bangle",
    "armor_007"  : "Chloe's Bracelet",
    "armor_008"  : "Crimson Bangle",
    "armor_009"  : "Flower Bangle",
    "armor_010"  : "Beast Bangle",
    "armor_011"  : "Central Stratum Bangle",
    "armor_012"  : "Yggdrasil Bangle",
    "armor_013"  : "Spire Bangle",
    "armor_014"  : "Abelia's Bracelet",
    "armor_015"  : "Declan's Binds",
    "armor_016"  : "Lunar Bangle",
    "armor_017"  : "Sol Bangle",
    "armor_018"  : "Aster Bangle",
    "armor_019"  : "Upper Stratum Bangle",
    "armor_020"  : "Ancient's Fury",
    "armor_021"  : "Celestial Bangle",
    "shield_001" : "Protective Carapace",
    "shield_002" : "Enhancer",
    "shield_003" : "Reflective Carapace",
    "shield_004" : "Pyroflective Carapace",
    "shield_005" : "High Enhancer",
    "shield_006" : "Impact Carapace",
    "shield_007" : "Blessed Carapace",
    "shield_008" : "Primordial Heirloom",
    "shield_009" : "Luiseach's Carapace",
})

quests = DataTable("DT_ItemQuests", group=ItemGroup.Quest, classification=IC.progression, code=6000,rows = 
{
    "quest_amulet"     : "Faintly Glowing Aegis Curio",
    "quest_artifact"   : "Mutated Mineral",
    "quest_bird"       : "Avian Remains",
    "quest_board"      : "Milius Resident Records",
    "quest_eye"        : "Blighted Pupil",
    "quest_lithograph" : "Stele of the Land of Origin",
    "quest_perfume"    : "Black Perfume",
    "quest_stone"      : "Frost Vestige",
})

keys = DataTable("DT_ItemKeys", group=ItemGroup.Key, classification=IC.progression, code=7000,rows = 
{
    "key_higher_a"   : "Frost Lord's Mark",
    "key_higher_b"   : "Milius Lord's Mark",
    "key_lower"      : "Lower Stratum Key",
    "key_owner"      : "Grand Sorcerer's Key",
    "key_ruins_tuto" : "Subterranean Testing Site Key",
})

materials = DataTable("DT_ItemMaterials", group=ItemGroup.Material, code=8000,rows = 
{
    "parts_lv2_b"   : "Experimental Amplifier",
    "parts_lv2_c"   : "Mixed Parts",
    "parts_lv3_a"   : "???",
    "parts_lv3_b"   : "Obsolete Core",
    "parts_lv3_c"   : "Antiquated Parts",
    "parts_lv4_a"   : "New Model Core",
    "parts_lv4_b"   : "Magic Amplifier",
    "parts_lv4_c"   : "New Model Parts",
    "parts_lv5_a"   : "Special Alloy Core",
    "parts_lv5_b"   : "Special Alloy Amplifier",
    "parts_lv5_c"   : "Special Alloy Part",
    "parts_lv6_a"   : "Origin Gem Core",
    "parts_lv6_b"   : "Administrator's Amplifier",
    "parts_lv6_c"   : "Highest Grade Parts",
    "parts_s5000_a" : "Unidentified Core",
    "parts_s5000_b" : "Unidentified Amplifier",
    "parts_s5000_c" : "Unidentified Transformer",
})

passives = DataTable("DT_ItemPassives", group=ItemGroup.Passive, code=9000,rows = 
{

    "damage_cut_debuff_down_1"          : "Labourer's Tag",
    "damage_cut_debuffed_1"             : "Bloodstained Stuffed Toy",
    "damage_cut_maxhp_1"                : "Beast Horn Ornanment",
    "damage_cut_minhp_1"                : "Effigy",
    "damage_cut_physic_1"               : "Tarnished Tag",
    "damage_cut_sp_gauge_1"             : "Crtystallised Fusion",
    "damage_up_airborne_1"              : "Sanguinary Raven",
    "damage_up_debuffed_1"              : "Battered Grimoire",
    "damage_up_grounded_1"              : "Chain Belt",
    "damage_up_maxhp_1"                 : "Magic Strange Charm",
    "damage_up_minhp_1"                 : "Jagged Crystal",
    "damage_up_skillcategory_auto_1"    : "House Milius Earrings",
    "damage_up_skillcategory_combo_1"   : "Echo Device",
    "damage_up_skillcategory_defence_1" : "Arena Tower Demon Mask",
    "damage_up_skillcategory_repeat_1"  : "Pure Floral Necklace",
    "damage_up_skillcategory_special_1" : "Cracked Magicite Dagger",
    "damage_up_sp_gauge_1"              : "Priestess' Tears",
    "damage_up_swimming_1"              : "Attuner's Pendant",
    "damage_up_targetdebuffed_1"        : "Vivid Claws",
    "damage_up_targetstunned_1"         : "Cleaner's Tag",
    "debuff_cut_burn_1"                 : "Crimson Ribbon",
    "debuff_damage_up_a_1"              : "Survey Team Gauntlet",
    "debuff_damage_up_b_1"              : "Sorcerer's Gauntlet",
    "dodge_long"                        : "Evasive Fragrance",
    "ending_flag"                       : "Lilia's Blighted Ring",
    "experience_up_1"                   : "Blighted Dice",
    "exploration_charge_short"          : "Enhancement Gear",
    "gold_up_1"                         : "Eye of the Beast",
    "heal_short"                        : "Ward Propagator",
    "higher_mobility"                   : "Leg Enhancement Gear",
    "junk_up_1"                         : "Eye of the Homunculus",
    "onattack_instantkill_1"            : "Abelia's Ring",
    "onattack_restorehp_1"              : "Declan's Ring",
    "onattack_restorehp_damage_1"       : "Cain's Ring",
    "onkill_drops_1"                    : "Headless Gold Statue",
    "onkill_reduce_cooldowns_1"         : "Magicite Hairpin",
    "onkill_restorehp_1"                : "Helix Crystal",
    "onkill_restoresp_1"                : "Attuner's Earrings",
    "reduce_gravity"                    : "Incomplete Gear",
    "reduce_skill_cooldown_1"           : "Eye of the Ancients",
    "restore_sp_up_a_1"                 : "Chief Attuner's Ring",
    "restore_sp_up_b_1"                 : "Nameless Priestess' Ring",
    "stamina_damage_up_a_1"             : "Blighted Talisman",
    "stamina_damage_up_b_1"             : "Mysterious Glowing Can",
})

skills = DataTable("DT_ItemSkills", group=ItemGroup.Skill, code=10000,rows = 
{
    "s5000_sword"   : "Nola Spirit Piercer",
    "s5001_scythe"  : "Nola Soul Harvester",
    "s5002_axe"     : "Nola Vanquisher",
    "s5010_blaster" : "Reibolg Magic Tracer",
    "s5011_lazer"   : "Reibolg Piercing Beam",
    "s5012_granade" : "Reibolg Blast Volley",
    "s5030_punch"   : "Lito Blazing Fist",
    "s5031_bomb"    : "Lito Glacial Fist",
    "s5032_roket"   : "Lito Rocket Fist",
    "s5040_reflect" : "Lorna Gravity Field",
    "s5041_gravit"  : "Lorna Light Show",
    "s5042_ignit"   : "Lorna Fire",
    "s5050_moon"    : "No.7 Lunar Manifestation",
    "s5051_snow"    : "No.7 Hail Dance",
    "s5052_flower"  : "No.7 Thunder Flower",
    "s5060_chain"   : "Shackled Beast Chain Whip",
    "s5061_horn"    : "Shackled Beast Charge",
    "s5062_voice"   : "Shackled Beast Benumbed Howl",
    "s5070_fire"    : "Luiseach Volcanic",
    "s5071_thunder" : "Luiseach Whirlwind",
    "s5072_ice"     : "Luiseach Cocytus",
    "s5080_wing"    : "Huginn Gust Wing",
    "s5081_trail"   : "Huginn Poison Cloud",
    "s5082_gast"    : "Huginn Flaming Feather",
    "s5090_homing"  : "Muninn Seeker",
    "s5091_stun"    : "Muninn Stun",
    "s5092_fall"    : "Muninn Bombard",
    "s5110_gatling" : "Yolvan Barrage",
    "s5111_saw"     : "Yolvan Lacerate",
    "s5112_drill"   : "Yolvan Eviscerate",
})

spirits = DataTable("DT_ItemSpirits", group=ItemGroup.Spirit, code=11000,rows = 
{
    "s5000_reaper" : "Nola",
    "s5010_lancer" : "Reibolg",
    "s5030_rogue"  : "Lito",
    "s5040_maiden" : "Lorna",
    "s5050_ronin"  : "No.7",
    "s5060_beast"  : "Shackled Beast",
    "s5070_witch"  : "Luiseach",
    "s5080_hawk"   : "Huginn",
    "s5090_owl"    : "Muninn",
    "s5110_gunman" : "Yolvan",
})

stats = DataTable("DT_ItemStats", classification=IC.filler, group=ItemGroup.Stat, code=12000,rows = 
{
    "attack_up_s"    : "Attack Up",
    "defense_up_s"   : "Defense Up",
    "hp_up_l"        : "Charmed Ore",
    "hp_up_s"        : "Charmed Fragment",
    "passive_slot_l" : "Tripartite Magic Vial",
    "passive_slot_s" : "Magic Vial",
    "shop_line_up"   : "Grimoire",
})

tips = DataTable("DT_ItemTips", classification=IC.filler, group=ItemGroup.Tip, code=13000,rows = 
{
    "tip_administrationrecord_01" : "Factory Management Records",
    "tip_bloodstaineddiary_01"    : "Bloodstained Diary",
    "tip_caladriusrecord_01"      : "Caladrius Records",
    "tip_cassiabook_01"           : "Cassia's Grimoire",
    "tip_chieftunerjournal_01"    : "Chief Attuner's Journal",
    "tip_corrosionboard_01"       : "Corroded Warning Sign",
    "tip_degrandsrecord_01"       : "Declan's Records",
    "tip_disposaljournal_01"      : "Blighted Note",
    "tip_engineermemoirs_01"      : "Arcane Smith's Musings",
    "tip_enhancementplan_01"      : "Miner Enchancement Project",
    "tip_fightingtower_01"        : "Arena Tower Flyer",
    "tip_freeze_01"               : "Survey Teams Notes",
    "tip_frostgrimoire_01"        : "Book of the Blighted",
    "tip_frostsrecord_01"         : "Frost Confidential Records 1",
    "tip_frostsrecord_02"         : "Frost Confidential Records 2",
    "tip_gilroyrecords_01"        : "Gilroy Examination Record",
    "tip_gilroysterminal_01"      : "Gilroy's Communication Device",
    "tip_homunculusrecord_01"     : "Homunculus Research Log 1",
    "tip_homunculusrecord_02"     : "Homunculus Research Log 2",
    "tip_landend_01"              : "Words on Land's End",
    "tip_lightsilence_01"         : "Silencing Light Documents",
    "tip_liliasdiary_01"          : "Lilia's Diary",
    "tip_lowestrecord_01"         : "Depths Survey Record",
    "tip_magicrecord_01"          : "Magicite Mining Record",
    "tip_miliusbook_01"           : "Chronicles of Milius",
    "tip_mothersnote_01"          : "Mother's Note",
    "tip_motleysterminal_01"      : "Motley's Communication Device",
    "tip_painting_01"             : "Worries of a Sorcerer",
    "tip_prisonwall_01"           : "Words Etched into Cell",
    "tip_prophecybook_01"         : "Blighted Prophecy",
    "tip_raggedpastedown_01"      : "Tattered Notice",
    "tip_researchersjournal_01"   : "Fugitive Researcher's Notes",
    "tip_ruinsrecords_01"         : "Worn Experiment Log",
    "tip_searchrecord_01"         : "Homunculus Expedition Report",
    "tip_secretletter_01"         : "Spy's Letter",
    "tip_surveillancerecord_01"   : "Worker's Surveillance Records",
    "tip_tombstone_01"            : "Words Etched into Stone",
    "tip_tornjournal_01"          : "Journal of an Attuner",
    "tip_tornletter_01"           : "Broken Warning Sign",
    "tip_towerumbrella_01"        : "Document on the Empyrean Parasol",
    "tip_townboard_01"            : "Tavern Bulletin Board",
    "tip_tunerjournal_01"         : "Notification of Restricted Areas",
    "tip_tunerletter_01"          : "Tattered Letter",
    "tip_upperterminal_01"        : "Upper Stratum Communication Device",
    "tip_vials_01"                : "Letter in a Bottle",
    "tip_workerscode_01"          : "Subterranean Laborer's Code",
    "tip_writingwall_01"          : "Writing Etched Into the Wall",
    "tip_yoransdiary_01"          : "Joran's Notes 1",
    "tip_yoransdiary_02"          : "Joran's Notes 2",
})

custom = CustomTable(code=14000, rows =
{
    "Central Stratum Elevator Key" : ("DT_ItemKeys.key_elevator", ItemGroup.Key),
})

events : Dict[str, ItemData] = {key: EventData(key, name) for key, name in {
    "EVT_ev_n_LilyEvent_Forest_001"    : "Lily in Crimson Forest",
    "EVT_ev_n_LilyEvent_Garden_001"    : "Lily in Sorcerer Academy",
	'EVT_ev_s_LilyEvent_Roots_002'     : "Lily in Land of Origin",
    "EVT_ev_s_0180_StreetElevatorFix"  : "Fix Street Elevator",
    "EVT_ev_s_e6050_Master_Defeat"     : "Defeat Gilroy",
	'EVT_ev_s_0080_FrostAndOwl'        : "Heath Mine",
	'EVT_ev_s_e0030_Guard_Defeat'      : "Defeat City Stratum Guard",
	'EVT_ev_s_e0122_Wheeler_Defeat'    : "Defeat Miner Unit",
	'EVT_ev_s_e0233_Researcher_Defeat' : "Defeat Eliza",
	'EVT_ev_s_n0233_RescueSuccess_001' : "Save Students",
    'EVT_ev_s_n7043_Quarry_Tuner'      : "Joran Intro",
    'EVT_ev_s_e5110_Gunman_Defeat'     : "Defeat Yolvan",
    'EVT_ev_s_n7042_Swamp_Tuner'       : "Unlock Relic Refinery",
    'EVT_ev_s_e6010_Cluster_Defeat'    : "Defeat Motley",
    'EVT_ev_s_e0289_BansheeMessage'    : "Banshee Message",
    
    "EVT_ev_n_Student_a_001"           : "Garden 2 Student 1",
    "EVT_ev_n_Student_b_001"           : "Garden 2 Student 2",
    "EVT_ev_n_Student_c_001"           : "Garden 2 Student 3",
    "EVT_ev_n_Student_d_001"           : "Garden 6 Student 1",
    "EVT_ev_n_Student_e_001"           : "Garden 6 Student 2",

    
	'EVT_ev_n_Levy_Treasure1_001'      : "Meet Levy 1 time",
	'EVT_ev_n_Levy_Treasure2_001'      : "Meet Levy 2 times",
	'EVT_ev_n_Levy_Treasure3_001'      : "Meet Levy 3 times",
	'EVT_ev_n_Levy_Treasure4_001'      : "Meet Levy 4 times",
	'EVT_ev_n_Levy_Treasure5_001'      : "Meet Levy 5 times",
	'EVT_ev_n_Levy_Treasure6_001'      : "Meet Levy in Land of Origin",
	'EVT_ev_s_e5012_RootsLancer_Defeat': "Defeat Reibolg",
	'EVT_ev_s_e5200_Pounder_Defeat'    : "Defeat Garm",
	'EVT_ev_s_e6000_Rider_Defeat'      : "Defeat Veol",

    "center05right_lever"              : "Center 5 Lever",
    "estate06right_lever"              : "Estate 6 Lever",
    "forest02right_lever"              : "Forest 2 Lever",
    "forest03right_lever"              : "Forest 3 Lever",
    "forest19right_lever"              : "Forest 19 Lever",
    "garden02center_lever"             : "Garden 2 Center Lever",
    "garden02left_lever"               : "Garden 2 Left Lever",
    "garden02lowerleft_lever"          : "Garden 2 Lower Left Lever",
    "garden02lowerrightleft_lever"     : "Garden 2 Lower Right Left Lever",
    "garden02lowerrightright_lever"    : "Garden 2 Lower Right Right Lever",
    "kowloon06right_lever"             : "Kowloon 6 Lever",
    "kowloon09upper_lever"             : "Kowloon 9 Lever",
    "kowloon15lower_lever"             : "Kowloon 15 Lever",
    "kowloon34lower_lever"             : "Kowloon 34 Lever",
    "kowloon36left_lever"              : "Kowloon 36 Lever",
    "kowloon40right_lever"             : "Kowloon 40 Lever",
    "kowloon42upper_lever"             : "Kowloon 42 Lever",
    "labo03left_lever"                 : "Labo 3 Left Lever",
    "labo03right_lever"                : "Labo 3 Right Lever",
    "labo05lower_lever"                : "Labo 5 Lower Lever",
    "labo05upper_lever"                : "Labo 5 Upper Lever",
    "labo18right_lever"                : "Labo 18 Lever",
    "labo19left_lever"                 : "Labo 19 Lever",
    "mine04right_lever"                : "Mine 4 Lever",
    "mine08right_lever"                : "Mine 8 Lever",
    "mine13right_lever"                : "Mine 13 Lever",
    "paradise04left_lever"             : "Paradise 4 Lever",
    "paradise19center_lever"           : "Paradise 19 Lever",
    "quarry15upper_lever"              : "Quarry 15 Lever",
    "roots11lower_lever"               : "Roots 11 Lever",
    "roots20upper_lever"               : "Roots 20 Lever",
    "ruins07upperright_lever"          : "Ruins 7 Lever",
    "sewer15lower_lever"               : "Sewer 15 Lever",
    "street02left_lever"               : "Street 2 Lever",
    "street05lowerright_lever"         : "Street 5 Lever",
    "summit08lowerright_lever"         : "Summit 8 Lever",
    "summit16right_lever"              : "Summit 16 Lever",
    "summit20upper_lever"              : "Summit 20 Lever",
    "summit23left_lever"               : "Summit 23 Left Lever",
    "summit23upper_lever"              : "Summit 23 Upper Lever",
    "summit25right_lever"              : "Summit 25 Right Lever",
    "summit25upper_lever"              : "Summit 25 Upper Lever",
    "summit27upper_lever"              : "Summit 27 Lever",
    "swamp10upper_lever"               : "Swamp 10 Lever",
    "swamp11left_lever"                : "Swamp 11 Left Lever",
    "swamp11right_lever"               : "Swamp 11 Right Lever",
    "swamp12left_lever"                : "Swamp 12 Lever",
    "tower01centerright_lever"         : "Tower 1 Lever",
    
    "Ending"                           : "Ending",

    "levy_treasure"                    : "Meet Levy",
}.items()}

# items required by logic
assists["assist_012"].classification = IC.progression
stats["shop_line_up"].classification = IC.progression

# 297
vanilla_pool = [
    *aptitudes,
    assists["assist_001"],
    assists["assist_006"],
    assists["assist_009"],
    assists["assist_010"],
    costumes["p0030"],
    costumes["p0040"],
    costumes["p0050"],
    *currencies["Default"] * 35,
    *currencies["rare"] * 13,
    equipments["armor_007"],
    equipments["armor_008"],
    equipments["armor_014"],
    equipments["armor_015"],
    equipments["armor_020"],
    equipments["armor_021"],
    equipments["shield_008"],
    equipments["shield_009"],
    *keys,
    *materials["parts_lv2_b"]   * 2,
    *materials["parts_lv3_b"]   * 2,
    *materials["parts_lv4_a"]   * 2,
    *materials["parts_lv4_b"]   * 3,
    *materials["parts_lv5_a"]   * 3,
    *materials["parts_lv5_b"]   * 2,
    *materials["parts_lv6_a"]   * 7,
    *materials["parts_lv6_b"]   * 9,
    *materials["parts_s5000_a"] * 3,
    *materials["parts_s5000_b"] * 3,
    *materials["parts_s5000_c"] * 3,
    passives["damage_cut_debuff_down_1"],
    passives["damage_cut_debuffed_1"],
    passives["damage_cut_maxhp_1"],
    passives["damage_cut_minhp_1"],
    passives["damage_cut_physic_1"],
    passives["damage_cut_sp_gauge_1"],
    passives["damage_up_airborne_1"],
    passives["damage_up_debuffed_1"],
    passives["damage_up_grounded_1"],
    passives["damage_up_maxhp_1"],
    passives["damage_up_minhp_1"],
    passives["damage_up_skillcategory_auto_1"],
    passives["damage_up_skillcategory_combo_1"],
    passives["damage_up_skillcategory_defence_1"],
    passives["damage_up_skillcategory_repeat_1"],
    passives["damage_up_skillcategory_special_1"],
    passives["damage_up_sp_gauge_1"],
    passives["damage_up_swimming_1"],
    passives["damage_up_targetdebuffed_1"],
    passives["damage_up_targetstunned_1"],
    passives["debuff_cut_burn_1"],
    passives["debuff_damage_up_a_1"],
    passives["debuff_damage_up_b_1"],
    passives["ending_flag"],
    passives["experience_up_1"],
    passives["gold_up_1"],
    passives["junk_up_1"],
    passives["onattack_instantkill_1"],
    passives["onattack_restorehp_1"],
    passives["onattack_restorehp_damage_1"],
    passives["onkill_drops_1"],
    passives["onkill_reduce_cooldowns_1"],
    passives["onkill_restorehp_1"],
    passives["onkill_restoresp_1"],
    passives["reduce_gravity"],
    passives["reduce_skill_cooldown_1"],
    passives["restore_sp_up_a_1"],
    passives["restore_sp_up_b_1"],
    passives["stamina_damage_up_a_1"],
    passives["stamina_damage_up_b_1"],
    *quests,
    *spirits,
    *stats["hp_up_l"] * 3,
    *stats["hp_up_s"] * 44,
    stats["passive_slot_l"],
    *stats["passive_slot_s"] * 10,
    *stats["shop_line_up"] * 12,
    *tips,
]

# 91
shop_pool = [
    assists["assist_002"],
    assists["assist_003"],
    assists["assist_004"],
    assists["assist_005"],
    assists["assist_007"],
    assists["assist_008"],
    assists["assist_011"],
    assists["assist_012"],
    equipments["armor_001"],
    equipments["armor_002"],
    equipments["armor_003"],
    equipments["armor_004"],
    equipments["armor_005"],
    equipments["armor_006"],
    equipments["armor_009"],
    equipments["armor_010"],
    equipments["armor_011"],
    equipments["armor_012"],
    equipments["armor_013"],
    equipments["armor_016"],
    equipments["armor_017"],
    equipments["armor_018"],
    equipments["armor_019"],
    equipments["shield_001"],
    equipments["shield_002"],
    equipments["shield_003"],
    equipments["shield_004"],
    equipments["shield_005"],
    equipments["shield_006"],
    equipments["shield_007"],
    *materials["parts_lv2_c"] * 2,
    *materials["parts_lv3_c"] * 2,
    *materials["parts_lv4_c"] * 4,
    *materials["parts_lv5_c"] * 4,
    *materials["parts_lv6_c"] * 9,
    passives["heal_short"],
    passives["higher_mobility"],
    passives["dodge_long"],
    passives["exploration_charge_short"],
    stats["hp_up_l"],
    *stats["passive_slot_s"] * 35,
]

# 20 upgrade materials required to unlock the skills, replaced by the skills themselves
skills_materials = [
    *materials["parts_lv2_b"]   * 2,
    *materials["parts_lv2_c"]   * 2,
    *materials["parts_lv3_b"]   * 2,
    *materials["parts_lv3_c"]   * 2,
    *materials["parts_lv4_b"]   * 1,
    *materials["parts_lv4_c"]   * 2,
    *materials["parts_lv5_b"]   * 2,
    *materials["parts_lv5_c"]   * 2,
    *materials["parts_lv6_b"]   * 2,
    *materials["parts_lv6_c"]   * 1,
    *materials["parts_s5000_b"] * 1,
    *materials["parts_s5000_c"] * 1,
]

# computed pool (vanilla + shop - skills_materials + skills - spirits)
# we remove 48/49 tips to flatten shop items
pool = [
    *aptitudes,
    *assists,
    *equipments,
    *keys,
    *passives,
    *quests,
    *skills,
    *[*tips][:-48],

    costumes["p0030"],
    costumes["p0040"],
    costumes["p0050"],

    *currencies["Default"] * 35,
    *currencies["rare"] * 13,

    *materials["parts_lv4_a"]   * 2,
    *materials["parts_lv4_b"]   * 2,
    *materials["parts_lv4_c"]   * 2,
    *materials["parts_lv5_a"]   * 3,
    *materials["parts_lv5_c"]   * 2,
    *materials["parts_lv6_a"]   * 7,
    *materials["parts_lv6_b"]   * 7,
    *materials["parts_lv6_c"]   * 8,
    *materials["parts_s5000_a"] * 3,
    *materials["parts_s5000_b"] * 2,
    *materials["parts_s5000_c"] * 2,

    *stats["hp_up_l"] * 4,
    *stats["hp_up_s"] * 44,
    stats["passive_slot_l"],
    *stats["passive_slot_s"] * 45,
    *stats["shop_line_up"] * 12,
]

# items for IDs
items : Dict[str, ItemData] = {item.name: item for item in [
    *aptitudes,*assists, *costumes, *currencies, *equipments, *quests,
    *keys, *materials, *passives, *skills, *spirits, *stats, *tips, *custom]
}
