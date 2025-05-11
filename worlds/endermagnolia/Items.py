from typing import Optional, Dict
from enum import Enum
from BaseClasses import ItemClassification as IC


class ItemGroup(Enum):
    """
    Used to group items
    """
    #Abilities
    Ability     = 0
    #Equipement
    Carapace    = 1
    Bracelet    = 2
    Totem       = 3
    #Relic
    Relic       = 4
    #Collection 
    QuestItem   = 5
    Component   = 6
    KeyItem     = 7
    Upgrade     = 8
    Action      = 9
    Ally        = 10
    #Message
    Finding     = 11

class ItemData():
    name: str
    key: Optional[str]
    code: Optional[int]
    count: Optional[int]
    classification: IC
    item_group: Optional[ItemGroup]
    unused: bool

    def __init__(self, name, key: Optional[str] = None, code:Optional[int]=None,
                 group:Optional[ItemGroup]=None, count: Optional[int]=1,
                classification:IC=IC.filler):
        self.name = name
        self.key = key
        self.code = code
        self.count = count
        self.classification = classification
        self.item_group = group


items : Dict[str, ItemData] = {item.name: item for item in [ 
    ItemData("Homunculus Research Log 1"     , code=1, key="DT_ItemTips.tip_homunculusrecord_01", group=ItemGroup.Finding),
    ItemData("Subterranean Testing Site Key" , code=3, key="DT_ItemKeys.key_ruins_tuto",          group=ItemGroup.KeyItem, classification=IC.progression),
    ItemData("Lito"                          , code=4, key="DT_ItemSpirits.s5030_rogue",          group=ItemGroup.Ally, classification=IC.progression),
    ItemData("Nola"                          , code=5, key="DT_ItemSpirits.s5000_reaper",         group=ItemGroup.Ally, classification=IC.progression),
    ItemData("Charmed Fragment"              , code=6, key="DT_ItemStats.hp_up_s",                group=ItemGroup.Upgrade),
    ItemData("Worn Experiment Log"           , code=7, key="DT_ItemTips.tip_ruinsrecords_01",     group=ItemGroup.Finding),

    ItemData("Healing Ward"                  , code=2, key="DT_ItemAptitudes.heal",               group=ItemGroup.Action),
    #ItemData("Dodge"                         , code=8, key="DT_ItemAptitudes.dodge",              group=ItemGroup.Action, classification=IC.progression),
    ItemData("Aerial Jump"                   , code=9, key="DT_ItemAptitudes.double_jump",        group=ItemGroup.Action, classification=IC.progression),
    ItemData("Hati's Charge"                 , code=10, key="DT_ItemAptitudes.dash_charge",       group=ItemGroup.Action, classification=IC.progression),
                                             
# event
    ItemData("Ruins 7 Lever"                 , classification=IC.progression),
    ItemData("Victory"                       , classification=IC.progression),
]}
