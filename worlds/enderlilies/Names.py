from typing import Dict

names : Dict[str, str] = {
    "umbral"                 : "Umbral Knight",                                       # Spirit.s5000
    "gerrod"                 : "Gerrod, the Elder Warrior",                           # Spirit.s5050
    "silva"                  : "Guardian Silva",                                      # Spirit.s5020
    "julius"                 : "Knight Captain Julius",                               # Spirit.s5030
    "ulv"                    : "Ulv, the Mad Knight",                                 # Spirit.s5070
    "eleine"                 : "Dark Witch Eleine",                                   # Spirit.s5040
    "hoenir"                 : "Hoenir, Keeper of the Abyss",                         # Spirit.s5060
    "faden"                  : "Faden, the Heretic",                                  # Spirit.s5080
    "siegrid"                : "Guardian Siegrid",                                    # Spirit.s5010
    "youth"                  : "Cliffside Hamlet Youth",                              # Spirit.s2012
    "defender"               : "Headless Defender",                                   # Spirit.s2002
    "bird"                   : "Western Merchant",                                    # Spirit.s2102
    "dog"                    : "Castle Town Maiden",                                  # Spirit.s2082
    "archer"                 : "Fallen Archer",                                       # Spirit.s2022
    "crypt"                  : "Elder Crypt Keeper",                                  # Spirit.s2162
    "fungal"                 : "Fungal Sorcerer",                                     # Spirit.s2122
    "floral"                 : "Floral Sorceress",                                    # Spirit.s2132
    "sentinel"               : "Fallen Sentinel",                                     # Spirit.s2192
    "subject"                : "Hidden Test Subject",                                 # Spirit.s2072
    "executionner"           : "Dark Executioner",                                    # Spirit.s2182
    "sinner"                 : "Incompetent Sinner",                                  # Spirit.s2052
    "champion"               : "Verboten Champion",                                   # Spirit.s2172
    "elder"                  : "Cliffside Hamlet Elder",                              # Spirit.s2112
    "chief"                  : "Chief Guardian",                                      # Spirit.s2092
    "aegis"                  : "One-Eyed Royal Aegis",                                # Spirit.s2032
    "fellwyrm"               : "Forsaken Fellwyrm",                                   # Spirit.s2232

    "djump"                  : "Guardian's Leap",                                     # Aptitude.double_jump
    "dodge"                  : "Guardian's Wings",                                    # Aptitude.Dodge
    "dash"                   : "Dash",                                                # Aptitude.dash
    "pierce"                 : "Piercing Spectral Lance",                             # Aptitude.dash_attack
    "slam"                   : "Giant's Hammer",                                      # Aptitude.pound_attack
    "swim"                   : "Witch's Bubble",                                      # Aptitude.dive
    "claw"                   : "Bloody Knight's Claws",                               # Aptitude.wallgrab
    "hook"                   : "Executioner's Hook",                                  # Aptitude.Hook
    "unlock"                 : "Unlock",                                              # Aptitude.door_unlock
    "ults"                   : "Last Rites",                                          # Aptitude.special_attack

    "dash/pierce"            : "Aptitude.dash,Aptitude.dash_attack",                  # EVENT
    "mask"                   : "Heretic's Mask",                                      # Passive.i_passive_ignore_damage_area
    "parry"                  : "Fretia's Ring",                                       # Passive.i_passive_parry
    "plume"                  : "Vibrant Plume",                                       # Passive.i_passive_jump_height_up
    "anklet"                 : "Spellbound Anklet",                                   # Passive.i_passive_move_speed_up
    "heal1"                  : "White Priestess Statue",                              # Passive.i_passive_heal_count_up_1
    "heal2"                  : "White Priestess' Earrings",                           # Passive.i_passive_heal_count_up_2
    "heal3"                  : "Priestess' Doll",                                     # Passive.i_passive_heal_count_up_3
    "tablet"                 : "Stone Tablet Fragment",                               # Generic.i_FinalPassivePart_Up
    "Aqueduct"               : "Stockade 02 - Executioner's Vow",                     # Oubliette_02_GAMEPLAY.BP_Interactable_Item_Tip3
    "BastionGates"           : "Twin Spires 03 - Bloodied Note 1",                    # Fort_03_GAMEPLAY.BP_Interactable_Item_Tip3
    "BridgeHead"             : "Cliffside Hamlet 09 - Hamlet Request 1",              # Village_09_GAMEPLAY.BP_Interactable_Item_Tip4
    "BottomOfTheWell"        : "Catacombs 01 - Fretia's Ring",                        # Cave_01_GAMEPLAY.BP_Interactable_Passive_Parry_2
    "CathedralCloister"      : "CathedralCloister",                                   # None
    "Cellar"                 : "White Parish 10 - On the Blighted 1",                 # Church_10_GAMEPLAY.BP_Interactable_Item_Tip_2
    "Cells"                  : "Stockade 06_1 - Hoenir's Diary 1",                    # Oubliette_06_1_GAMEPLAY.BP_Interactable_Item_Tip3
    "Charnel"                : "Catacombs 03 - Defense of the Twin Spires 2",         # Cave_03_GAMEPLAY.BP_Interactable_Item_Tip3
    "Courtyard"              : "Twin Spires 10 - Bloodied Note 2",                    # Fort_10_GAMEPLAY.BP_Interactable_Item_Tip3
    "CovenHalls"             : "Witch's Thicket 14 - The Parish Way 3",               # Forest_14_GAMEPLAY.BP_Interactable_Item_Tip3
    "Crossroads"             : "White Parish 08 - The Parish Way 2",                  # Church_08_GAMEPLAY.BP_Interactable_Item_Tip3
    "DarkChamber"            : "Stockade 10 - Executioner's Missive",                 # Oubliette_10_GAMEPLAY.BP_Interactable_Item_Tip3
    "CollapsedShack"         : "Cliffside Hamlet 05 - True Believer's Note",          # Village_05_GAMEPLAY.BP_Interactable_Item_Tip4
    "DryadLake"              : "Witch's Thicket 05 - Coven Handbook",                 # Forest_05_GAMEPLAY.BP_Interactable_Item_Tip4
    "ExecutionGrounds"       : "Stockade 14 - Hoenir's Diary 2",                      # Oubliette_14_GAMEPLAY.BP_Interactable_Item_Tip3
    "GreatHall"              : "Catacombs 16 - The Next White Priestess",             # Cave_16_GAMEPLAY.BP_Interactable_Item_Tip4
    "GuestChamber"           : "Ruined Castle 07 - Proof of Founding",                # Castle_07_GAMEPLAY.BP_Interactable_Item_Tip3
    "KingsChamber"           : "Ruined Castle 19 - King's Note 1",                    # Castle_19_GAMEPLAY.BP_Interactable_Item_Tip3
    "Lab1"                   : "Verboten Domain 01 - Faden's Archives 3",             # Swamp_1_GAMEPLAY.BP_Interactable_Item_Tip3
    "Lab2"                   : "Verboten Domain 06 - Verboten Domain Notice",         # Swamp_06_GAMEPLAY.BP_Interactable_Item_Tip3
    "Lab3"                   : "Verboten Domain 10 - Faden's Archives 4",             # Swamp_10_GAMEPLAY.BP_Interactable_Item_Tip3
    "Lab4"                   : "Verboten Domain 12 - Faden's Archives 2",             # Swamp_12_GAMEPLAY.BP_Interactable_Item_Tip3
    "Lab5"                   : "Verboten Domain 16 - Faden's Archives 1",             # Swamp_16_GAMEPLAY.BP_Interactable_Item_Tip3
    "MaelstromRemparts"      : "Ruined Castle 10 - Julius' Book",                     # Castle_10_GAMEPLAY.BP_Interactable_Item_Tip3
    "MonumentOfTheWindStart" : "MonumentOfTheWindStart",                              # Fort_16_GAMEPLAY.BP_Interactable_Item_Tip3
    "MourningHall"           : "MourningHall",                                        # None
    "Ossuary"                : "Catacombs 13 - Silva's Note 1",                       # Cave_13_GAMEPLAY.BP_Interactable_Item_Tip3
    "SaintsPassage"          : "White Parish 04 - Groa's Letter",                     # Church_04_GAMEPLAY.BP_Interactable_Item_Tip3
    "Start"                  : "White Parish 12 - Statue Inscription",                # Church_12_GAMEPLAY.BP_Interactable_Item_Tip1
    "WitchsHermitage"        : "Witch's Thicket 10 - Sorcerer's Notes",               # Forest_10_GAMEPLAY.BP_Interactable_Item_Tip3
    "Aegis"                  : "Ruined Castle 16 - One-Eyed Royal Aegis",             # Castle_16_GAMEPLAY.BP_e2032_BigKnight
    "AncientDragonClaw"      : "Twin Spires 19 - Ancient Dragon Claw",                # Fort_19_GAMEPLAY.BP_Interactable_Passives_Treasure_2
    "AnkletRoom"             : "Witch's Thicket 17 - Eleine's Diary 1",               # Forest_17_Map.BP_Interactable_Item_Tip5
    "Archer"                 : "Catacombs 19 - Fallen Archer",                        # Cave_19_GAMEPLAY.BP_e2022_Soldier
    "AurasRing"              : "Stockade 13_1 - Aura's Ring",                         # Oubliette_13_1_GAMEPLAY.BP_Interactable_Passives_Treasure_2
    "Bird"                   : "Cliffside Hamlet 04_1 - Western Merchant",            # Village_04_1_GAMEPLAY.BP_e2102_Crow
    "BlightWreathedBlade"    : "Ruined Castle 08 - Blightwreathed Blade",             # Castle_08_GAMEPLAY.BP_Interactable_Passive_expup_5
    "BlightedAppendage"      : "Verboten Domain 11 - Blighted Appendage",             # Swamp_11_GAMEPLAY.BP_Interactable_Passives_Treasure_2
    "BlightedHeart"          : "The Abyss 02 - Silva's Blight-Stained Note 2",        # Abyss_02_GAMEPLAY.BP_Interactable_Item_Tip3
    "BloodstainedRibbon"     : "Cliffside Hamlet 04 - Bloodstained Ribbon",           # Village_04_GAMEPLAY.BP_Interactable_Passives_Treasure_2
    "BrokenMusicBox"         : "Cliffside Hamlet 03 - Broken Music Box",              # Village_03_GAMEPLAY.BP_Interactable_Passives_Treasure_2
    "CaliviasRing"           : "Verboten Domain 07 - Calivia's Ring",                 # Swamp_07_GAMEPLAY.BP_Interactable_Passive_RecastTimeCut_Lv2_2
    "Cave11Tip"              : "Catacombs 11 - Silva's Note 2",                       # Cave_11_GAMEPLAY.BP_Interactable_Item_Tip3
    "Champion"               : "Verboten Domain 04 - Verboten Champion",              # Swamp_04_GAMEPLAY.BP_e2172_Inferior
    "Chief"                  : "White Parish 09 - Chief Guardian",                    # Church_09_GAMEPLAY.BP_e2092_Priest
    "CrackedFamiliarStone"   : "Witch's Thicket 08 - Cracked Familiar Stone",         # Forest_08_GAMEPLAY.BP_Interactable_Passive_Treasure2
    "DecayedCrown"           : "Ruined Castle 01 - Decayed Crown",                    # Castle_01_GAMEPLAY.BP_Interactable_Passive_Spirit_StunStaminaDamageUp_2
    "Defender"               : "Cliffside Hamlet 08 - Headless Defender",             # Village_08_GAMEPLAY.BP_e2002_Knight
    "Dog"                    : "Ruined Castle 01 - Castle Town Maiden",               # Castle_01_GAMEPLAY.BP_e2082_Dog
    "Elder"                  : "Cliffside Hamlet 14 - Cliffside Hamlet Elder",        # Village_14_GAMEPLAY.BP_e2112_Ork
    "EldredsRing"            : "Ruined Castle 18 - Eldred's Ring",                    # Castle_18_GAMEPLAY.BP_Interactable_Passives_Treasure_2
    "Eleine"                 : "Witch's Thicket 15 - Dark Witch Eleine",              # Forest_15_GAMEPLAY.BP_e5040_Witch
    "Executioner"            : "Stockade 12 - Dark Executioner",                      # Oubliette_12_GAMEPLAY.BP_e2182_Shadow
    "ExecutionersGloves"     : "Stockade 06_2 - Executioner's Gloves",                # Oubliette_06_2_GAMEPLAY.BP_Interactable_Passive_dmgup_maxHP_2
    "Faden"                  : "Verboten Domain 18 - Faden, the Heretic",             # Swamp_18_GAMEPLAY.BP_Interactable_Spirit_s5080_2
    "Fellwyrm"               : "Twin Spires 12 - Forsaken Fellwyrm",                  # Fort_12_GAMEPLAY.BP_e2232_Dragon
    "Floral"                 : "Witch's Thicket 11 - Floral Sorceress",               # Forest_11_GAMEPLAY.BP_e2132_Mandrake
    "Fort11Stagnant"         : "Twin Spires 11 - Stagnant Blight x30",                # Fort_11_GAMEPLAY.BP_SCR_LV1M_2190_4
    "Fort12HP"               : "Twin Spires 12 - Amulet Fragment",                    # Fort_12_GAMEPLAY.BP_Interactable_Item_MaxHPUp_01_7
    "Fort13Chain"            : "Twin Spires 13 - Chain of Sorcery",                   # Fort_13_GAMEPLAY.BP_Interactable_Item_PassiveSlot_Drop
    "Fungal"                 : "Witch's Thicket 06 - Fungal Sorcerer",                # Forest_06_GAMEPLAY.BP_e2122_Fungus
    "Gerrod"                 : "Cliffside Hamlet 10 - Gerrod, the Elder Warrior",     # Village_10_GAMEPLAY.BP_e5050_Giant
    "GiantsRing"             : "Cliffside Hamlet 13 - Giant's Ring",                  # Village_13_GAMEPLAY.BP_Interactable_Passives_Treasure_2
    "Grotto"                 : "Hinterlands 03 - King of the First Age's Torn Note 1",# Outside_03_GAMEPLAY.BP_Interactable_Item_Tip3
    "HereticsMask"           : "Verboten Domain 06 - Heretic's Mask",                 # Swamp_06_GAMEPLAY.BP_Interactable_Passives_Treasure_2
    "Hoenir"                 : "Stockade 15 - Hoenir, Keeper of the Abyss",           # Oubliette_15_GAMEPLAY.BP_e5060_Assassin
    "HolySpringWater"        : "Catacombs 18 - Holy Spring Water",                    # Cave_18_GAMEPLAY.BP_Interactable_Passive_healpowerup_2
    "ImmortalsCrest"         : "Twin Spires 15 - Immortal's Crest",                   # Fort_15_GAMEPLAY.BP_Interactable_Passives_Treasure_2
    "Julius"                 : "Ruined Castle 20 - Knight Captain Julius",            # Castle_20_GAMEPLAY.BP_e5030_Leader
    "KilteusRing"            : "Catacombs 06 - Kilteus' Ring",                        # Cave_06_GAMEPLAY.BP_Interactable_Passives_Treasure_2
    "ManisasRing"            : "Witch's Thicket 08 - Manisa's Ring",                  # Forest_08_GAMEPLAY.BP_Interactable_Passive_Treasure_2
    "NymphiliasRing"         : "Hinterlands 03 - Nymphilia's Ring",                   # Outside_03_GAMEPLAY.BP_Interactable_Passive_ShortHeal_2
    "PriestessDoll"          : "Ruined Castle 01 - Priestess' Doll",                  # Castle_01_GAMEPLAY.BP_Interactable_Passive_healcountup_4
    "RicorusRing"            : "Twin Spires 11 - Ricorus' Ring",                      # Fort_11_GAMEPLAY.BP_Interactable_Passives_Treasure_2
    "RoyalAegisCrest"        : "Ruined Castle 06 - Royal Aegis Crest",                # Castle_06_GAMEPLAY.BP_Interactable_Passives_Treasure_2
    "RuinedCastleCellar"     : "Ruined Castle 04 - Report from a Verboten Mage",      # Castle_04_GAMEPLAY.BP_Interactable_Item_Tip3
    "RuinedWitchsBook"       : "Witch's Thicket 11 - Ruined Witch's Book",            # Forest_11_GAMEPLAY.BP_Interactable_Passives_Treasure_2
    "RustedBlueOrnament"     : "Witch's Thicket 04 - Rusted Blue Ornament",           # Forest_04_GAMEPLAY.BP_Interactable_Passive_dmgup_swimming_2
    "SecondSpireChamber"     : "Twin Spires 08 - Hoenir's Diary 3",                   # Fort_08_GAMEPLAY.BP_Interactable_Item_Tip3
    "Sentinel"               : "Twin Spires 01 - Fallen Sentinel",                    # Fort_01_GAMEPLAY.BP_e2192_Gargoyle
    "Siegrid"                : "White Parish 03 - Guardian Siegrid",                  # Church_03_GAMEPLAY.BP_e5011_YoungerSister
    "Silva"                  : "Catacombs 23 - Guardian Silva",                       # Cave_23_GAMEPLAY.BP_e5021_OlderSister
    "Sinner"                 : "Verboten Domain 15 - Incompetent Sinner",             # Swamp_15_GAMEPLAY.BP_e2052_Toad
    "SnowdropBracelet"       : "Twin Spires 09 - Snowdrop Bracelet",                  # Fort_09_GAMEPLAY.BP_Interactable_Passive_dmgcut_Lv3_2
    "SoiledPrayerBeads"      : "White Parish 05 - Soiled Prayer Beads",               # Church_05_GAMEPLAY.BP_Interactable_Passive_MaxHPUp_Lv1_2
    "SpellboundAnklet"       : "Witch's Thicket 17 - Spellbound Anklet",              # Forest_17_GAMEPLAY.BP_Interactable_Passives_Treasure_2
    "Spider"                 : "Catacombs 07 - Elder Crypt Keeper",                   # Cave_07_GAMEPLAY.BP_e2162_Spider
    "Subject"                : "Stockade 07_2 - Hidden Test Subject",                 # Oubliette_07_2_GAMEPLAY.BP_e2072_Mimic
    "TowerAlcove"            : "Ruined Castle 15 - Priestess' Castle Memo",           # Castle_15_GAMEPLAY.BP_Interactable_Item_Tip3
    "Ulv"                    : "Twin Spires 21 - Ulv, the Mad Knight",                # Fort_21_GAMEPLAY.BP_e5070_Killer
    "VibrantPlume"           : "White Parish 09 - Vibrant Plume",                     # Church_09_GAMEPLAY.BP_Interactable_Passive_JumpHeightUp_2
    "Village800"             : "Cliffside Hamlet 15 - Stagnant Blight x800",          # Village_15_GAMEPLAY.BP_SCR_LV1LL_0000_2
    "WeatheredNecklace"      : "Verboten Domain 09 - Weathered Necklace",             # Swamp_09_GAMEPLAY.BP_Interactable_Passives_Treasure_2
    "WhitePriestessEarrings" : "The Abyss 02 - White Priestess' Earrings",            # Abyss_02_GAMEPLAY.BP_Interactable_Passive_healcountup_2
    "WhitePriestessStatue"   : "Catacombs 21 - White Priestess Statue",               # Cave_21_GAMEPLAY.BP_Interactable_Passive_healcountup_2
    "Youth"                  : "White Parish 07 - Cliffside Hamlet Youth",            # Church_07_GAMEPLAY.BP_e2012_Slime_Unique

    "Abyss01Bottom"          : "Map.map_abyss_01.2",                                  # EVENT
    "Abyss01Top"             : "Map.map_abyss_01.S18",                                # EVENT
    "Abyss02Right"           : "Map.map_abyss_02.3",                                  # EVENT
    "Abyss02Top"             : "Map.map_abyss_02.1",                                  # EVENT
    "Abyss03Left"            : "Map.map_abyss_03.2",                                  # EVENT
    "Abyss04Bottom"          : "Map.map_abyss_04.5",                                  # EVENT
    "Abyss04Top"             : "Map.map_abyss_04.2",                                  # EVENT
    "Abyss05Top"             : "Map.map_abyss_05.4",                                  # EVENT
    "Castle01Left"           : "Map.map_castle_01.0",                                 # EVENT
    "Castle01Right1"         : "Map.map_castle_01.2B",                                # EVENT
    "Castle01Right2"         : "Map.map_castle_01.2",                                 # EVENT
    "Castle01Top"            : "Map.map_castle_01.10",                                # EVENT
    "Castle02Bottom"         : "Map.map_castle_02.4",                                 # EVENT
    "Castle02Left1"          : "Map.map_castle_02.1B",                                # EVENT
    "Castle02Left2"          : "Map.map_castle_02.1",                                 # EVENT
    "Castle02Top"            : "Map.map_castle_02.5",                                 # EVENT
    "Castle03Bottom"         : "Map.map_castle_03.5",                                 # EVENT
    "Castle03Top1"           : "Map.map_castle_03.11A",                               # EVENT
    "Castle03Top2"           : "Map.map_castle_03.11B",                               # EVENT
    "Castle04Top"            : "Map.map_castle_04.2",                                 # EVENT
    "Castle05Bottom"         : "Map.map_castle_05.2",                                 # EVENT
    "Castle05Left"           : "Map.map_castle_05.8",                                 # EVENT
    "Castle05Right"          : "Map.map_castle_05.6",                                 # EVENT
    "Castle05Top"            : "Map.map_castle_05.3",                                 # EVENT
    "Castle06Left"           : "Map.map_castle_06.5",                                 # EVENT
    "Castle06Right"          : "Map.map_castle_06.7",                                 # EVENT
    "Castle06Top"            : "Map.map_castle_06.12",                                # EVENT
    "Castle07Left"           : "Map.map_castle_07.6",                                 # EVENT
    "Castle07Right"          : "Map.map_castle_07.F1",                                # EVENT
    "Castle08Right"          : "Map.map_castle_08.5",                                 # EVENT
    "Castle08Top"            : "Map.map_castle_08.9",                                 # EVENT
    "Castle09Bottom"         : "Map.map_castle_09.8",                                 # EVENT
    "Castle09Left"           : "Map.map_castle_09.10",                                # EVENT
    "Castle09Right"          : "Map.map_castle_09.11",                                # EVENT
    "Castle10Bottom"         : "Map.map_castle_10.1",                                 # EVENT
    "Castle10Right"          : "Map.map_castle_10.9",                                 # EVENT
    "Castle11Bottom1"        : "Map.map_castle_11.3A",                                # EVENT
    "Castle11Bottom2"        : "Map.map_castle_11.3B",                                # EVENT
    "Castle11Left"           : "Map.map_castle_11.9",                                 # EVENT
    "Castle11Right"          : "Map.map_castle_11.12",                                # EVENT
    "Castle11Top"            : "Map.map_castle_11.13",                                # EVENT
    "Castle12Bottom"         : "Map.map_castle_12.6",                                 # EVENT
    "Castle12Left"           : "Map.map_castle_12.11",                                # EVENT
    "Castle12Right"          : "Map.map_castle_12.21",                                # EVENT
    "Castle13Bottom"         : "Map.map_castle_13.11",                                # EVENT
    "Castle13Left"           : "Map.map_castle_13.17",                                # EVENT
    "Castle13Right"          : "Map.map_castle_13.14",                                # EVENT
    "Castle14Left"           : "Map.map_castle_14.13",                                # EVENT
    "Castle14Top"            : "Map.map_castle_14.15",                                # EVENT
    "Castle15Bottom"         : "Map.map_castle_15.14",                                # EVENT
    "Castle15Left"           : "Map.map_castle_15.16",                                # EVENT
    "Castle16Right"          : "Map.map_castle_16.15",                                # EVENT
    "Castle17Right"          : "Map.map_castle_17.13",                                # EVENT
    "Castle17Top"            : "Map.map_castle_17.18",                                # EVENT
    "Castle18Bottom"         : "Map.map_castle_18.17",                                # EVENT
    "Castle18Right"          : "Map.map_castle_18.19",                                # EVENT
    "Castle18Top"            : "Map.map_castle_18.16",                                # EVENT
    "Castle19Left"           : "Map.map_castle_19.18",                                # EVENT
    "Castle19Right"          : "Map.map_castle_19.20",                                # EVENT
    "Castle20Left"           : "Map.map_castle_20.19",                                # EVENT
    "Castle21Left"           : "Map.map_castle_21.12",                                # EVENT
    "Cave01Bottom"           : "Map.map_cave_01.2",                                   # EVENT
    "Cave01Left"             : "Map.map_cave_01.V12",                                 # EVENT
    "Cave02Bottom"           : "Map.map_cave_02.7",                                   # EVENT
    "Cave02Right"            : "Map.map_cave_02.5",                                   # EVENT
    "Cave02Top"              : "Map.map_cave_02.1",                                   # EVENT
    "Cave03Left"             : "Map.map_cave_03.7",                                   # EVENT
    "Cave03Right"            : "Map.map_cave_03.8",                                   # EVENT
    "Cave03Top"              : "Map.map_cave_03.6",                                   # EVENT
    "Cave04Bottom"           : "Map.map_cave_04.5",                                   # EVENT
    "Cave04Left"             : "Map.map_cave_04.12",                                  # EVENT
    "Cave04Right"            : "Map.map_cave_04.16",                                  # EVENT
    "Cave05Bottom"           : "Map.map_cave_05.6",                                   # EVENT
    "Cave05Left"             : "Map.map_cave_05.2",                                   # EVENT
    "Cave05Right"            : "Map.map_cave_05.10",                                  # EVENT
    "Cave05Top"              : "Map.map_cave_05.4",                                   # EVENT
    "Cave06Bottom"           : "Map.map_cave_06.3",                                   # EVENT
    "Cave06Top"              : "Map.map_cave_06.5",                                   # EVENT
    "Cave07Right"            : "Map.map_cave_07.3",                                   # EVENT
    "Cave07Top"              : "Map.map_cave_07.2",                                   # EVENT
    "Cave08Bottom"           : "Map.map_cave_08.17",                                  # EVENT
    "Cave08Left"             : "Map.map_cave_08.3",                                   # EVENT
    "Cave08Right"            : "Map.map_cave_08.11",                                  # EVENT
    "Cave08Top"              : "Map.map_cave_08.9",                                   # EVENT
    "Cave09Bottom"           : "Map.map_cave_09.8",                                   # EVENT
    "Cave09Right"            : "Map.map_cave_09.21",                                  # EVENT
    "Cave09Top"              : "Map.map_cave_09.10",                                  # EVENT
    "Cave10Bottom"           : "Map.map_cave_10.9",                                   # EVENT
    "Cave10Left"             : "Map.map_cave_10.5",                                   # EVENT
    "Cave10Right"            : "Map.map_cave_10.23",                                  # EVENT
    "Cave10Top"              : "Map.map_cave_10.16",                                  # EVENT
    "Cave11Left"             : "Map.map_cave_11.8",                                   # EVENT
    "Cave11Right1"           : "Map.map_cave_11.18",                                  # EVENT
    "Cave11Right2"           : "Map.map_cave_11.18B",                                 # EVENT
    "Cave11Top"              : "Map.map_cave_11.13",                                  # EVENT
    "Cave12Right"            : "Map.map_cave_12.4",                                   # EVENT
    "Cave13Bottom"           : "Map.map_cave_13.11",                                  # EVENT
    "Cave13Left"             : "Map.map_cave_13.23",                                  # EVENT
    "Cave13Right"            : "Map.map_cave_13.20",                                  # EVENT
    "Cave13Top"              : "Map.map_cave_13.14",                                  # EVENT
    "Cave14Bottom"           : "Map.map_cave_14.13",                                  # EVENT
    "Cave14Left"             : "Map.map_cave_14.15",                                  # EVENT
    "Cave14Right"            : "Map.map_cave_14.22",                                  # EVENT
    "Cave15Left"             : "Map.map_cave_15.16",                                  # EVENT
    "Cave15Right"            : "Map.map_cave_15.14",                                  # EVENT
    "Cave16Bottom"           : "Map.map_cave_16.10",                                  # EVENT
    "Cave16Left"             : "Map.map_cave_16.4",                                   # EVENT
    "Cave16Right"            : "Map.map_cave_16.15",                                  # EVENT
    "Cave17Top"              : "Map.map_cave_17.8",                                   # EVENT
    "Cave18Left1"            : "Map.map_cave_18.11",                                  # EVENT
    "Cave19Left"             : "Map.map_cave_19.21",                                  # EVENT
    "Cave19Top"              : "Map.map_cave_19.20",                                  # EVENT
    "Cave20Bottom"           : "Map.map_cave_20.19",                                  # EVENT
    "Cave20Left"             : "Map.map_cave_20.13",                                  # EVENT
    "Cave20Top"              : "Map.map_cave_20.22",                                  # EVENT
    "Cave21Left"             : "Map.map_cave_21.9",                                   # EVENT
    "Cave21Right"            : "Map.map_cave_21.19",                                  # EVENT
    "Cave22Bottom"           : "Map.map_cave_22.20",                                  # EVENT
    "Cave22Left"             : "Map.map_cave_22.14",                                  # EVENT
    "Cave22Right"            : "Map.map_cave_22.F2",                                  # EVENT
    "Cave23Left"             : "Map.map_cave_23.10",                                  # EVENT
    "Cave23Right"            : "Map.map_cave_23.13",                                  # EVENT
    "Church01Bottom"         : "Map.map_church_01.1",                                 # EVENT
    "Church01Left"           : "Map.map_church_01.12",                                # EVENT
    "Church01Top"            : "Map.map_church_01.2",                                 # EVENT
    "Church02Right"          : "Map.map_church_02.10",                                # EVENT
    "Church02Top"            : "Map.map_church_02.0",                                 # EVENT
    "Church03Left"           : "Map.map_church_03.0",                                 # EVENT
    "Church03Right"          : "Map.map_church_03.1",                                 # EVENT
    "Church04Left"           : "Map.map_church_04.0",                                 # EVENT
    "Church04Right"          : "Map.map_church_04.1",                                 # EVENT
    "Church05Bottom"         : "Map.map_church_05.11",                                # EVENT
    "Church05Right"          : "Map.map_church_05.1",                                 # EVENT
    "Church05Top"            : "Map.map_church_05.9",                                 # EVENT
    "Church06Left"           : "Map.map_church_06.0",                                 # EVENT
    "Church06Right"          : "Map.map_church_06.1",                                 # EVENT
    "Church07Left"           : "Map.map_church_07.0",                                 # EVENT
    "Church07Right"          : "Map.map_church_07.1",                                 # EVENT
    "Church08Bottom"         : "Map.map_church_08.2",                                 # EVENT
    "Church08Left"           : "Map.map_church_08.0",                                 # EVENT
    "Church08Top"            : "Map.map_church_08.1",                                 # EVENT
    "Church09Bottom"         : "Map.map_church_09.5",                                 # EVENT
    "Church09Top"            : "Map.map_church_09.14",                                # EVENT
    "Church10Left"           : "Map.map_church_10.2",                                 # EVENT
    "Church10Right"          : "Map.map_church_10.11",                                # EVENT
    "Church11Left"           : "Map.map_church_11.10",                                # EVENT
    "Church11Top"            : "Map.map_church_11.5",                                 # EVENT
    "Church12Bottom"         : "Map.map_church_12.3",                                 # EVENT
    "Church12Right"          : "Map.map_church_12.1",                                 # EVENT
    "Church13Top"            : "Map.map_church_13.6",                                 # EVENT
    "Church14Bottom"         : "Map.map_church_14.9",                                 # EVENT
    "Forest01Right"          : "Map.map_forest_01.2",                                 # EVENT
    "Forest01Top"            : "Map.map_forest_01.C8",                                # EVENT
    "Forest02Left"           : "Map.map_forest_02.1",                                 # EVENT
    "Forest02Right1"         : "Map.map_forest_02.4",                                 # EVENT
    "Forest02Right2"         : "Map.map_forest_02.3",                                 # EVENT
    "Forest03Left"           : "Map.map_forest_03.2",                                 # EVENT
    "Forest03Right"          : "Map.map_forest_03.5",                                 # EVENT
    "Forest04Left"           : "Map.map_forest_04.2",                                 # EVENT
    "Forest04Right"          : "Map.map_forest_04.6",                                 # EVENT
    "Forest05Left"           : "Map.map_forest_05.3",                                 # EVENT
    "Forest05Right"          : "Map.map_forest_05.7",                                 # EVENT
    "Forest05Top"            : "Map.map_forest_05.4",                                 # EVENT
    "Forest06Bottom"         : "Map.map_forest_06.7",                                 # EVENT
    "Forest07Bottom"         : "Map.map_forest_07.8",                                 # EVENT
    "Forest07Left"           : "Map.map_forest_07.5",                                 # EVENT
    "Forest07Right"          : "Map.map_forest_07.O1",                                # EVENT
    "Forest07Top"            : "Map.map_forest_07.6",                                 # EVENT
    "Forest08Right"          : "Map.map_forest_08.10",                                # EVENT
    "Forest08Top"            : "Map.map_forest_08.7",                                 # EVENT
    "Forest09Left"           : "Map.map_forest_09.S2",                                # EVENT
    "Forest09Top"            : "Map.map_forest_09.10",                                # EVENT
    "Forest10Bottom1"        : "Map.map_forest_10.9",                                 # EVENT
    "Forest10Bottom2"        : "Map.map_forest_10.11",                                # EVENT
    "Forest10Left"           : "Map.map_forest_10.8",                                 # EVENT
    "Forest10Right"          : "Map.map_forest_10.12",                                # EVENT
    "Forest11Right"          : "Map.map_forest_11.14",                                # EVENT
    "Forest11Top"            : "Map.map_forest_11.10",                                # EVENT
    "Forest12Bottom"         : "Map.map_forest_12.13",                                # EVENT
    "Forest12Left"           : "Map.map_forest_12.10",                                # EVENT
    "Forest12Right"          : "Map.map_forest_12.17",                                # EVENT
    "Forest13Bottom"         : "Map.map_forest_13.14",                                # EVENT
    "Forest13Right"          : "Map.map_forest_13.16",                                # EVENT
    "Forest13Top"            : "Map.map_forest_13.12",                                # EVENT
    "Forest14Bottom"         : "Map.map_forest_14.15",                                # EVENT
    "Forest14Left"           : "Map.map_forest_14.11",                                # EVENT
    "Forest14Top"            : "Map.map_forest_14.13",                                # EVENT
    "Forest15Top"            : "Map.map_forest_15.14",                                # EVENT
    "Forest16Left"           : "Map.map_forest_16.13",                                # EVENT
    "Forest17Left"           : "Map.map_forest_17.12",                                # EVENT
    "Fort01Left1"            : "Map.map_fort_01.C7",                                  # EVENT
    "Fort01Left2"            : "Map.map_fort_01.V15",                                 # EVENT
    "Fort01Right"            : "Map.map_fort_01.3",                                   # EVENT
    "Fort02Left"             : "Map.map_fort_02.C22",                                 # EVENT
    "Fort02Right"            : "Map.map_fort_02.3",                                   # EVENT
    "Fort03Left1"            : "Map.map_fort_03.1",                                   # EVENT
    "Fort03Left2"            : "Map.map_fort_03.2",                                   # EVENT
    "Fort03Right"            : "Map.map_fort_03.4",                                   # EVENT
    "Fort03Top"              : "Map.map_fort_03.5",                                   # EVENT
    "Fort04Left"             : "Map.map_fort_04.3",                                   # EVENT
    "Fort04Top"              : "Map.map_fort_04.5",                                   # EVENT
    "Fort05Bottom1"          : "Map.map_fort_05.3",                                   # EVENT
    "Fort05Bottom2"          : "Map.map_fort_05.4",                                   # EVENT
    "Fort05Right"            : "Map.map_fort_05.6",                                   # EVENT
    "Fort05Top"              : "Map.map_fort_05.15",                                  # EVENT
    "Fort06Bottom"           : "Map.map_fort_06.10",                                  # EVENT
    "Fort06Left"             : "Map.map_fort_06.5",                                   # EVENT
    "Fort06Right"            : "Map.map_fort_06.7",                                   # EVENT
    "Fort07Bottom1"          : "Map.map_fort_07.9",                                   # EVENT
    "Fort07Bottom2"          : "Map.map_fort_07.9B",                                  # EVENT
    "Fort07Left"             : "Map.map_fort_07.6",                                   # EVENT
    "Fort07Right"            : "Map.map_fort_07.8",                                   # EVENT
    "Fort07Top"              : "Map.map_fort_07.11",                                  # EVENT
    "Fort08Left"             : "Map.map_fort_08.7",                                   # EVENT
    "Fort09Left"             : "Map.map_fort_09.10",                                  # EVENT
    "Fort09Right"            : "Map.map_fort_09.O3",                                  # EVENT
    "Fort09Top1"             : "Map.map_fort_09.7",                                   # EVENT
    "Fort09Top2"             : "Map.map_fort_09.7B",                                  # EVENT
    "Fort10Right"            : "Map.map_fort_10.9",                                   # EVENT
    "Fort10Top"              : "Map.map_fort_10.6",                                   # EVENT
    "Fort11Bottom"           : "Map.map_fort_11.7",                                   # EVENT
    "Fort11Left"             : "Map.map_fort_11.12",                                  # EVENT
    "Fort11Top1"             : "Map.map_fort_11.13",                                  # EVENT
    "Fort11Top2"             : "Map.map_fort_11.53",                                  # EVENT
    "Fort12Left"             : "Map.map_fort_12.16",                                  # EVENT
    "Fort12Right"            : "Map.map_fort_12.11",                                  # EVENT
    "Fort12Top"              : "Map.map_fort_12.14",                                  # EVENT
    "Fort13Bottom1"          : "Map.map_fort_13.11",                                  # EVENT
    "Fort13Bottom2"          : "Map.map_fort_13.11B",                                 # EVENT
    "Fort13Left"             : "Map.map_fort_13.14",                                  # EVENT
    "Fort13Top"              : "Map.map_fort_13.19",                                  # EVENT
    "Fort14Bottom"           : "Map.map_fort_14.12",                                  # EVENT
    "Fort14Left"             : "Map.map_fort_14.15",                                  # EVENT
    "Fort14Right"            : "Map.map_fort_14.13",                                  # EVENT
    "Fort15Bottom"           : "Map.map_fort_15.5",                                   # EVENT
    "Fort15Right1"           : "Map.map_fort_15.14",                                  # EVENT
    "Fort15Right2"           : "Map.map_fort_15.16",                                  # EVENT
    "Fort15Right3"           : "Map.map_fort_15.16B",                                 # EVENT
    "Fort15Top"              : "Map.map_fort_15.17",                                  # EVENT
    "Fort16Left1"            : "Map.map_fort_16.15",                                  # EVENT
    "Fort16Left2"            : "Map.map_fort_16.15B",                                 # EVENT
    "Fort16Right"            : "Map.map_fort_16.12",                                  # EVENT
    "Fort16Top"              : "Map.map_fort_16.18",                                  # EVENT
    "Fort17Bottom"           : "Map.map_fort_17.15",                                  # EVENT
    "Fort17Right"            : "Map.map_fort_17.18",                                  # EVENT
    "Fort18Bottom"           : "Map.map_fort_18.16",                                  # EVENT
    "Fort18Left"             : "Map.map_fort_18.17",                                  # EVENT
    "Fort18Right"            : "Map.map_fort_18.19",                                  # EVENT
    "Fort19Bottom"           : "Map.map_fort_19.13",                                  # EVENT
    "Fort19Left"             : "Map.map_fort_19.18",                                  # EVENT
    "Fort19Top"              : "Map.map_fort_19.20",                                  # EVENT
    "Fort20Bottom"           : "Map.map_fort_20.19",                                  # EVENT
    "Fort20Top"              : "Map.map_fort_20.21",                                  # EVENT
    "Fort21Bottom"           : "Map.map_fort_21.20",                                  # EVENT
    "Oubliette01Left"        : "Map.map_oubliette_01.F7",                             # EVENT
    "Oubliette01Right"       : "Map.map_oubliette_01.2",                              # EVENT
    "Oubliette02Left"        : "Map.map_oubliette_02.1",                              # EVENT
    "Oubliette02Right1"      : "Map.map_oubliette_02.5",                              # EVENT
    "Oubliette02Right2"      : "Map.map_oubliette_02.4",                              # EVENT
    "Oubliette03Left"        : "Map.map_oubliette_03.4",                              # EVENT
    "Oubliette03Right"       : "Map.map_oubliette_03.10",                             # EVENT
    "Oubliette03Top"         : "Map.map_oubliette_03.5",                              # EVENT
    "Oubliette04Left"        : "Map.map_oubliette_04.2",                              # EVENT
    "Oubliette04Right"       : "Map.map_oubliette_04.3",                              # EVENT
    "Oubliette051Bottom"     : "Map.map_oubliette_05_1.5",                            # EVENT
    "Oubliette052Bottom1"    : "Map.map_oubliette_05_2.5",                            # EVENT
    "Oubliette052Bottom2"    : "Map.map_oubliette_05_2.5B",                           # EVENT
    "Oubliette053Top"        : "Map.map_oubliette_05_3.5",                            # EVENT
    "Oubliette05Bottom1"     : "Map.map_oubliette_05.7_1",                            # EVENT
    "Oubliette05Bottom2"     : "Map.map_oubliette_05.5_3",                            # EVENT
    "Oubliette05Bottom3"     : "Map.map_oubliette_05.3",                              # EVENT
    "Oubliette05Left"        : "Map.map_oubliette_05.2",                              # EVENT
    "Oubliette05Right"       : "Map.map_oubliette_05.6",                              # EVENT
    "Oubliette05Top1"        : "Map.map_oubliette_05.5_1",                            # EVENT
    "Oubliette05Top2"        : "Map.map_oubliette_05.5_2",                            # EVENT
    "Oubliette05Top3"        : "Map.map_oubliette_05.7_2",                            # EVENT
    "Oubliette05Top4"        : "Map.map_oubliette_05.5_2B",                           # EVENT
    "Oubliette061Left"       : "Map.map_oubliette_06_1.7",                            # EVENT
    "Oubliette062Bottom2"    : "Map.map_oubliette_06_2.7",                            # EVENT
    "Oubliette063Left1"      : "Map.map_oubliette_06_3.7",                            # EVENT
    "Oubliette064Top"        : "Map.map_oubliette_06_4.7",                            # EVENT
    "Oubliette06Bottom"      : "Map.map_oubliette_06.10",                             # EVENT
    "Oubliette06Left"        : "Map.map_oubliette_06.5",                              # EVENT
    "Oubliette06Right"       : "Map.map_oubliette_06.7",                              # EVENT
    "Oubliette071Top"        : "Map.map_oubliette_07_1.5",                            # EVENT
    "Oubliette072Bottom"     : "Map.map_oubliette_07_2.5",                            # EVENT
    "Oubliette07Bottom1"     : "Map.map_oubliette_07.9",                              # EVENT
    "Oubliette07Bottom2"     : "Map.map_oubliette_07.6_2",                            # EVENT
    "Oubliette07Left1"       : "Map.map_oubliette_07.6_3",                            # EVENT
    "Oubliette07Left2"       : "Map.map_oubliette_07.6",                              # EVENT
    "Oubliette07Right1"      : "Map.map_oubliette_07.6_1",                            # EVENT
    "Oubliette07Right2"      : "Map.map_oubliette_07.13",                             # EVENT
    "Oubliette07Top"         : "Map.map_oubliette_07.6_4",                            # EVENT
    "Oubliette08Left"        : "Map.map_oubliette_08.9",                              # EVENT
    "Oubliette08Right"       : "Map.map_oubliette_08.11",                             # EVENT
    "Oubliette08Top"         : "Map.map_oubliette_08.13",                             # EVENT
    "Oubliette09Left"        : "Map.map_oubliette_09.10",                             # EVENT
    "Oubliette09Right"       : "Map.map_oubliette_09.8",                              # EVENT
    "Oubliette09Top"         : "Map.map_oubliette_09.7",                              # EVENT
    "Oubliette10Left1"       : "Map.map_oubliette_10.3",                              # EVENT
    "Oubliette10Left2"       : "Map.map_oubliette_10.17",                             # EVENT
    "Oubliette10Right"       : "Map.map_oubliette_10.9",                              # EVENT
    "Oubliette10Top"         : "Map.map_oubliette_10.6",                              # EVENT
    "Oubliette11Bottom"      : "Map.map_oubliette_11.13_2",                           # EVENT
    "Oubliette11Left1"       : "Map.map_oubliette_11.13",                             # EVENT
    "Oubliette11Left2"       : "Map.map_oubliette_11.8",                              # EVENT
    "Oubliette11Right1"      : "Map.map_oubliette_11.12",                             # EVENT
    "Oubliette11Right2"      : "Map.map_oubliette_11.14",                             # EVENT
    "Oubliette11Top"         : "Map.map_oubliette_11.13_1",                           # EVENT
    "Oubliette12Left"        : "Map.map_oubliette_12.11",                             # EVENT
    "Oubliette131Bottom"     : "Map.map_oubliette_13_1.11",                           # EVENT
    "Oubliette132Top"        : "Map.map_oubliette_13_2.11",                           # EVENT
    "Oubliette13Bottom"      : "Map.map_oubliette_13.8",                              # EVENT
    "Oubliette13Left"        : "Map.map_oubliette_13.7",                              # EVENT
    "Oubliette13Right"       : "Map.map_oubliette_13.11",                             # EVENT
    "Oubliette14Left"        : "Map.map_oubliette_14.11",                             # EVENT
    "Oubliette14Right"       : "Map.map_oubliette_14.15",                             # EVENT
    "Oubliette15Left"        : "Map.map_oubliette_15.14",                             # EVENT
    "Oubliette15Right"       : "Map.map_oubliette_15.16",                             # EVENT
    "Oubliette16Left"        : "Map.map_oubliette_16.15",                             # EVENT
    "Oubliette16Right"       : "Map.map_oubliette_16.O1",                             # EVENT
    "Oubliette17Bottom"      : "Map.map_oubliette_17.S6",                             # EVENT
    "Oubliette17Right"       : "Map.map_oubliette_17.10",                             # EVENT
    "Outside01Left1"         : "Map.map_outside_01.3",                                # EVENT
    "Outside01Left2"         : "Map.map_outside_01.O16",                              # EVENT
    "Outside01Right"         : "Map.map_outside_01.2",                                # EVENT
    "Outside02Left"          : "Map.map_outside_02.1",                                # EVENT
    "Outside03Right"         : "Map.map_outside_03.1",                                # EVENT
    "Outside03Top"           : "Map.map_outside_03.F9",                               # EVENT
    "Swamp04Bottom"          : "Map.map_swamp_04.5",                                  # EVENT
    "Swamp04Left"            : "Map.map_swamp_04.3",                                  # EVENT
    "Swamp05Bottom"          : "Map.map_swamp_05.7",                                  # EVENT
    "Swamp05Left"            : "Map.map_swamp_05.9",                                  # EVENT
    "Swamp05Right"           : "Map.map_swamp_05.6",                                  # EVENT
    "Swamp05Top"             : "Map.map_swamp_05.4",                                  # EVENT
    "Swamp06Left"            : "Map.map_swamp_06.5",                                  # EVENT
    "Swamp06Top"             : "Map.map_swamp_06.O17",                                # EVENT
    "Swamp07Bottom"          : "Map.map_swamp_07.16",                                 # EVENT
    "Swamp07Left"            : "Map.map_swamp_07.8",                                  # EVENT
    "Swamp07Right"           : "Map.map_swamp_07.5",                                  # EVENT
    "Swamp07Top"             : "Map.map_swamp_07.3",                                  # EVENT
    "Swamp08Right1"          : "Map.map_swamp_08.7",                                  # EVENT
    "Swamp08Right2"          : "Map.map_swamp_08.15",                                 # EVENT
    "Swamp08Top"             : "Map.map_swamp_08.14",                                 # EVENT
    "Swamp09Bottom1"         : "Map.map_swamp_09.13",                                 # EVENT
    "Swamp09Bottom2"         : "Map.map_swamp_09.13B",                                # EVENT
    "Swamp09Right1"          : "Map.map_swamp_09.3",                                  # EVENT
    "Swamp09Right2"          : "Map.map_swamp_09.5",                                  # EVENT
    "Swamp10Right"           : "Map.map_swamp_10.13",                                 # EVENT
    "Swamp11Bottom"          : "Map.map_swamp_11.15",                                 # EVENT
    "Swamp11Left"            : "Map.map_swamp_11.14",                                 # EVENT
    "Swamp12Bottom"          : "Map.map_swamp_12.4",                                  # EVENT
    "Swamp12Left"            : "Map.map_swamp_12.15",                                 # EVENT
    "Swamp12TP"              : "Map.map_swamp_12.A5",                                 # EVENT
    "Swamp13Bottom"          : "Map.map_swamp_13.14",                                 # EVENT
    "Swamp13Left"            : "Map.map_swamp_13.10",                                 # EVENT
    "Swamp13Top1"            : "Map.map_swamp_13.9",                                  # EVENT
    "Swamp13Top2"            : "Map.map_swamp_13.9B",                                 # EVENT
    "Swamp14Bottom"          : "Map.map_swamp_14.8",                                  # EVENT
    "Swamp14Right"           : "Map.map_swamp_14.11",                                 # EVENT
    "Swamp14Top"             : "Map.map_swamp_14.13",                                 # EVENT
    "Swamp15Left"            : "Map.map_swamp_15.8",                                  # EVENT
    "Swamp15Right"           : "Map.map_swamp_15.12",                                 # EVENT
    "Swamp15Top"             : "Map.map_swamp_15.11",                                 # EVENT
    "Swamp16Left"            : "Map.map_swamp_16.17",                                 # EVENT
    "Swamp16Top"             : "Map.map_swamp_16.7",                                  # EVENT
    "Swamp17Left"            : "Map.map_swamp_17.18",                                 # EVENT
    "Swamp17Right"           : "Map.map_swamp_17.16",                                 # EVENT
    "Swamp18Bottom"          : "Map.map_swamp_18.A1",                                 # EVENT
    "Swamp18Right"           : "Map.map_swamp_18.17",                                 # EVENT
    "Swamp1Bottom"           : "Map.map_swamp_01.3",                                  # EVENT
    "Swamp1Left"             : "Map.map_swamp_01.2",                                  # EVENT
    "Swamp2Right"            : "Map.map_swamp_02.1",                                  # EVENT
    "Swamp2Top"              : "Map.map_swamp_02.F9",                                 # EVENT
    "Swamp3Bottom"           : "Map.map_swamp_03.7",                                  # EVENT
    "Swamp3Left"             : "Map.map_swamp_03.9",                                  # EVENT
    "Swamp3Right"            : "Map.map_swamp_03.4",                                  # EVENT
    "Swamp3Top"              : "Map.map_swamp_03.1",                                  # EVENT
    "Village01Bottom"        : "Map.map_village_01.0",                                # EVENT
    "Village01Right"         : "Map.map_village_01.1",                                # EVENT
    "Village02Bottom"        : "Map.map_village_02.13",                               # EVENT
    "Village02Left"          : "Map.map_village_02.0",                                # EVENT
    "Village02Right"         : "Map.map_village_02.1",                                # EVENT
    "Village03Bottom1"       : "Map.map_village_03.0",                                # EVENT
    "Village03Bottom2"       : "Map.map_village_03.2",                                # EVENT
    "Village03Right"         : "Map.map_village_03.5",                                # EVENT
    "Village041Bottom"       : "Map.map_village_04_1.0",                              # EVENT
    "Village04Right"         : "Map.map_village_04.5",                                # EVENT
    "Village04Top"           : "Map.map_village_04.2",                                # EVENT
    "Village05Left"          : "Map.map_village_05.3",                                # EVENT
    "Village05Right"         : "Map.map_village_05.1",                                # EVENT
    "Village05Top"           : "Map.map_village_05.4",                                # EVENT
    "Village06Bottom"        : "Map.map_village_06.12",                               # EVENT
    "Village06Left"          : "Map.map_village_06.0",                                # EVENT
    "Village06Right1"        : "Map.map_village_06.1",                                # EVENT
    "Village06Right2"        : "Map.map_village_06.8",                                # EVENT
    "Village07Left"          : "Map.map_village_07.0",                                # EVENT
    "Village07Right"         : "Map.map_village_07.9",                                # EVENT
    "Village07Top"           : "Map.map_village_07.14",                               # EVENT
    "Village08Left"          : "Map.map_village_08.6",                                # EVENT
    "Village08Right"         : "Map.map_village_08.9",                                # EVENT
    "Village09Left1"         : "Map.map_village_09.7",                                # EVENT
    "Village09Left2"         : "Map.map_village_09.8",                                # EVENT
    "Village09Right1"        : "Map.map_village_09.1",                                # EVENT
    "Village09Right2"        : "Map.map_village_09.2",                                # EVENT
    "Village10Left"          : "Map.map_village_10.0",                                # EVENT
    "Village10Right"         : "Map.map_village_10.1",                                # EVENT
    "Village111Bottom"       : "Map.map_village_11_1.0",                              # EVENT
    "Village11Left"          : "Map.map_village_11.0",                                # EVENT
    "Village11Right"         : "Map.map_village_11.1",                                # EVENT
    "Village11Top"           : "Map.map_village_11.2",                                # EVENT
    "Village12Left1"         : "Map.map_village_12.13",                               # EVENT
    "Village12Left2"         : "Map.map_village_12.16",                               # EVENT
    "Village12Right"         : "Map.map_village_12.C1",                               # EVENT
    "Village12Top"           : "Map.map_village_12.6",                                # EVENT
    "Village13Left"          : "Map.map_village_13.2",                                # EVENT
    "Village13Right"         : "Map.map_village_13.12",                               # EVENT
    "Village13Top"           : "Map.map_village_13.0",                                # EVENT
    "Village14Bottom"        : "Map.map_village_14.7",                                # EVENT
    "Village15Left"          : "Map.map_village_15.0",                                # EVENT
    "Village15Right"         : "Map.map_village_15.F1",                               # EVENT
    "Village16Right"         : "Map.map_village_16.12",                               # EVENT   
}
