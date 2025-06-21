from typing import List, Optional, Dict
from enum import Enum
from BaseClasses import ItemClassification as IC
from dataclasses import dataclass, field

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
    def __init__(self, name):
        super().__init__(name, classification=IC.progression)

@dataclass()
class DataTable():
    name: str
    group: ItemGroup
    code: int
    rows: Dict[str, str]
    classification: IC = IC.filler
    codes: Dict[str, int] = field(init=False)

    def __post_init__(self):
        code = self.code
        self.codes = {}
        for entry in self.rows:
            self.codes[entry] = code
            code += 1

    def __getitem__(self, entry) -> ItemData:
        return ItemData(self.rows[entry], self.name + "." + entry, self.codes[entry], self.group, self.classification)

    def __len__(self) -> int:
        return len(self.rows)

    def __iter__(self):
        for entry in self.rows:
            yield self[entry]

aptitudes = DataTable("DT_ItemAptitudes", group=ItemGroup.Aptitude, classification=IC.progression, code=1000,rows = 
{
#    "Crouch"                 : "Crouch",
#    "Jump"                   : "Jump",
#    "dash"                   : "Sprint",
#    "dodge_weak"             : "Roll",
    "fast_travel"            : "Fast Travel",
    "Hook"                   : "Motley's Magic Strands",
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

costumes = DataTable("DT_ItemCostumes", group=ItemGroup.Costume, code=3000,rows = 
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

currencies = DataTable("DT_ItemCurrencies", group=ItemGroup.Currency, code=4000,rows = 
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
    "s5001_scythe"  : "Nola Soul Harverster",
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

stats = DataTable("DT_ItemStats", group=ItemGroup.Stat, code=12000,rows = 
{
    "attack_up_s"    : "Attack Up",
    "defense_up_s"   : "Defense Up",
    "hp_up_l"        : "Charmed Ore",
    "hp_up_s"        : "Charmed Fragment",
    "passive_slot_l" : "Tripartite Magic Vial",
    "passive_slot_s" : "Magic Vial",
    "shop_line_up"   : "Grimoire",
})

tips = DataTable("DT_ItemTips", group=ItemGroup.Tip, code=13000,rows = 
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

# items data and 
items : Dict[str, ItemData] = {item.name: item for item in [ 
    *aptitudes,*assists, *costumes, *currencies, *equipments, *quests,
    *keys, *materials, *passives, *skills, *spirits, *stats, *tips]
}

# items and quantity in the pool
pool = [
    # TODO: currencies -> need to handle pack of items
    # TODO: shop 
    assists["assist_001"],
    assists["assist_006"],
    assists["assist_009"],
    assists["assist_010"],
    *aptitudes,
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
    *quests,
    *passives, # +4
    *stats["hp_up_l"] * 3,
    *stats["hp_up_s"] * 44,
    stats["passive_slot_l"],
    *stats["passive_slot_s"] * 10,
    *stats["shop_line_up"] * 12,
    *skills, # +20
    *[*tips][:-24], # -24
]

events : Dict[str, ItemData] = {item.name: item for item in [ 
    EventData("Ruins 7 Lever"),
    EventData("Victory"),
]}