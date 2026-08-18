from typing import Dict, Tuple
from BaseClasses import Item
from worlds.generic.Rules import ItemRule
from rule_builder.rules import Has, Rule, True_
from .Items import ItemGroup
from .Options import CentralElevatorFix, Goal
from .Types import EnderMagnoliaItem


def is_item_group(item: Item, group: ItemGroup) -> bool:
    return isinstance(item, EnderMagnoliaItem) and item.group == group

completion_rules: Dict[int, Rule] = {
	Goal.option_ending_a : Has('Ending'),
	Goal.option_ending_b : Has('Ending') & Has("Lilia's Blighted Ring"),
}

# no mats in shop
shop_item_rule: ItemRule = lambda i : not is_item_group(i, ItemGroup.Currency)

items_rules: Dict[str, ItemRule] = {
    # only skills
    "Starting Skill":  lambda i : is_item_group(i, ItemGroup.Skill),
}

shop_rules: Dict[Tuple[str, str], Rule] = {
	('Slum01Left',   'Shop')           : Has('Defeat Yolvan'),
	('Center01LowerLeft',   'Shop')    : Has('Defeat Gilroy'),

	('Shop',         'Shop Level 1' )  : True_(),
	('Shop',         'Shop Level 2' )  : Has('Grimoire', 1),
	('Shop',         'Shop Level 3' )  : Has('Grimoire', 2),
	('Shop',         'Shop Level 4' )  : Has('Grimoire', 3),
	('Shop',         'Shop Level 5' )  : Has('Grimoire', 4),
	('Shop',         'Shop Level 6' )  : Has('Grimoire', 5),
	('Shop',         'Shop Level 7' )  : Has('Grimoire', 6),
	('Shop',         'Shop Level 8' )  : Has('Grimoire', 7),
	('Shop',         'Shop Level 9' )  : Has('Grimoire', 8),
	('Shop',         'Shop Level 10')  : Has('Grimoire', 9),
	('Shop',         'Shop Level 11')  : Has('Grimoire', 10),
	('Shop',         'Shop Level 12')  : Has('Grimoire', 11),
	('Shop',         'Shop Level 13')  : Has('Grimoire', 12),
}

elevator_rules: Dict[int, Rule] = {
	CentralElevatorFix.option_key  : Has('Grand Lift Key'),
	CentralElevatorFix.option_free : True_(),
}

levy_rules: Dict[Tuple[str, str], Rule] = {
	('Menu',         'Levy Quest Reward 1') : Has('Meet Levy', 1),
	('Menu',         'Levy Quest Reward 2') : Has('Meet Levy', 2),
	('Menu',         'Levy Quest Reward 3') : Has('Meet Levy', 3),
	('Menu',         'Levy Quest Reward 4') : Has('Meet Levy', 4),
	('Menu',         'Levy Quest Reward 5') : Has('Meet Levy', 5),
}
