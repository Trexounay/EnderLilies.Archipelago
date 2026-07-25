from typing import Optional

from BaseClasses import Item, ItemClassification, Location, Region

from .Items import ItemData, ItemGroup, items
from .Locations import LocationData

ENDERMAGNOLIA = "Ender Magnolia"


class EnderMagnoliaItem(Item):
    game = ENDERMAGNOLIA
    group: Optional[ItemGroup] = None

    @classmethod
    def from_name(cls, name: str, player: int):
        if name in items:
            return cls.from_data(items[name], player)
        return cls(name, ItemClassification.progression, None, player)

    @classmethod
    def from_data(cls, data: ItemData, player: int):
        item = cls(data.name, data.classification, data.code, player)
        item.group = data.group
        return item


class EnderMagnoliaLocation(Location):
    game = ENDERMAGNOLIA
    data: LocationData

    def __init__(self, player: int, name: str, data: LocationData, parent: Optional[Region] = None):
        address = data.address
        super().__init__(player, name, address, parent)
        self.data = data

    def key(self):
        return self.data.key


class EnderMagnoliaEvent(Location):
    game = ENDERMAGNOLIA

    def __init__(self, player: int, name: str, parent: Optional[Region] = None):
        super().__init__(player, name, None, parent)
