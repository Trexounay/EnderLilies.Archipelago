from rule_builder.rules import HasAll, HasAny

TORRENT   = HasAll("Dive", "Dodge", "Motley's Torrent")
WALL_DASH = HasAll("Lars' Grip", "Lars' Swift Flight")

# advanced
FLOWER2   = HasAll("Incomplete Gear", "No.7 Thunder Flower")
REIBOLG   = HasAny("Reibolg Magic Tracer", "Reibolg Piercing Beam", "Reibolg Blast Volley")
RONIN     = HasAny("No.7 Lunar Manifestation", "No.7 Hail Dance", "No.7 Thunder Flower")
STALL     = HasAny("Nola Spirit Piercer", "Nola Soul Harvester", "Nola Vanquisher")

Aliases = {
    "axe"     : "s5002_axe",
    "blaster" : "s5010_blaster",
    "flower"  : "s5052_flower",
    "granade" : "s5012_granade",
    "grav"    : "reduce_gravity",
    "lazer"   : "s5011_lazer",
    "moon"    : "s5050_moon",
    "scythe"  : "s5001_scythe",
    "snow"    : "s5051_snow",
    "sword"   : "s5000_sword",
}


