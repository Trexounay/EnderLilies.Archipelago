from itertools import combinations
from typing import Collection, List, NamedTuple, Optional, Set, Tuple

from BaseClasses import CollectionState, Item, Location
from Fill import FillError, sweep_from_pool
from worlds.AutoWorld import World

MAX_ATTEMPTS = 5
MAX_BACKTRACKS = 200

CONJUNCTIONS = [
    ("Frost Lord's Mark", "Milius Lord's Mark"),
    ("Blighted Pupil", "Stele of the Land of Origin"),
    ("Dive", "Motley's Torrent"),
    ("Lar's Grip", "Lar's Swift Flight"),
    ("Progressive Dive", "Progressive Dive"),
    ("Progressive Lar's Grip", "Progressive Lar's Grip"),
]

Unit = List[Item]
Placement = Tuple[Location, Item]


class Frame(NamedTuple):
    state: CollectionState
    seen: Set[Location]
    spheres: List[List[Location]]
    used: Set[Location]
    units: List[Unit]
    placements: List[Placement]
    candidates: Optional[List[Unit]]


def build_units(items: List[Item]) -> List[Unit]:
    units: List[Unit] = [[item] for item in items]
    for names in CONJUNCTIONS:
        pool = list(items)
        bundle: Unit = []
        for name in names:
            index = next((i for i, item in enumerate(pool) if item.name == name), None)
            if index is None:
                break
            bundle.append(pool.pop(index))
        if len(bundle) == len(names):
            units.append(bundle)
    return units


def distinct(units: List[Unit]) -> List[Item]:
    known: Set[int] = set()
    items: List[Item] = []
    for unit in units:
        for item in unit:
            if id(item) not in known:
                known.add(id(item))
                items.append(item)
    return items


class Chain:
    def __init__(self, world: World) -> None:
        self.world = world
        self.random = world.random
        self.locations: Collection[Location] = world.multiworld.get_locations(world.player)

    def reachable(self, state: CollectionState) -> List[Location]:
        return [location for location in self.locations
                if not location.is_event and location.can_reach(state)]

    def opens_new(self, frame: Frame, items: List[Item]) -> bool:
        swept = sweep_from_pool(frame.state, items, self.locations)
        return any(location not in frame.seen and not location.is_event and location.can_reach(swept)
                   for location in self.locations)

    def free_slots(self, frame: Frame) -> int:
        return sum(1 for location in frame.spheres[-1]
                   if location.item is None and location not in frame.used)

    def emerging_pair(self, frame: Frame) -> List[Unit]:
        loners = [unit[0] for unit in frame.units if len(unit) == 1]
        pairs = list(combinations(loners, 2))
        self.random.shuffle(pairs)
        for first, second in pairs:
            pair = [first, second]
            if self.opens_new(frame, pair):
                return [pair]
        return []

    def place_unit(self, frame: Frame, unit: Unit) -> Optional[Frame]:
        state = frame.state.copy()
        used = set(frame.used)
        placements = list(frame.placements)

        for item in unit:
            slots = [location for location in frame.spheres[-1]
                     if location.item is None and location not in used
                     and location.can_fill(state, item, False)]
            if not slots:
                return None
            location = self.random.choice(slots)
            used.add(location)
            placements.append((location, item))
            state.collect(item, prevent_sweep=True)

        state.sweep_for_advancements(self.locations)
        found = self.reachable(state)
        fresh = [location for location in found if location not in frame.seen]

        taken = {id(item) for item in unit}
        units = [rest for rest in frame.units if not any(id(item) in taken for item in rest)]
        return Frame(state, set(found), frame.spheres + [fresh], used, units, placements, None)

    def expand(self, frame: Frame) -> Frame:
        ready = [unit for unit in frame.units if self.opens_new(frame, unit)]
        alone = {id(unit[0]) for unit in ready if len(unit) == 1}
        candidates = [unit for unit in ready
                      if len(unit) == 1 or not any(id(item) in alone for item in unit)]

        if not candidates and self.free_slots(frame) >= 2:
            candidates = self.emerging_pair(frame)

        self.random.shuffle(candidates)
        return frame._replace(candidates=candidates)

    def build(self, units: List[Unit]) -> Tuple[List[Placement], List[Item]]:
        state = sweep_from_pool(CollectionState(self.world.multiworld), locations=self.locations)
        found = self.reachable(state)
        current = Frame(state, set(found), [found], set(), units, [], None)

        stack: List[Frame] = []
        budget = MAX_BACKTRACKS

        while current.units:
            if current.candidates is None:
                current = self.expand(current)
                if not current.candidates:
                    rest = distinct(current.units)
                    if not self.opens_new(current, rest):
                        return current.placements, rest

            child = None
            while current.candidates and child is None:
                child = self.place_unit(current, current.candidates.pop())

            if child is not None:
                stack.append(current)
                current = child
                continue

            budget -= 1
            if not stack or budget <= 0:
                raise FillError("Meta progression: no viable chain found",
                                multiworld=self.world.multiworld)
            current = stack.pop()

        return current.placements, []


def meta_progression_fill(world: World) -> None:
    items = [item for item in world.multiworld.itempool
             if item.player == world.player and item.advancement]
    if not items:
        return

    chain = Chain(world)
    units = build_units(items)
    for attempt in range(MAX_ATTEMPTS):
        try:
            placements, dropped = chain.build(units)
            break
        except FillError:
            if attempt == MAX_ATTEMPTS - 1:
                raise

    chained = {id(item) for item in items}
    world.multiworld.itempool[:] = [item for item in world.multiworld.itempool
                                    if id(item) not in chained]
    world.multiworld.itempool.extend(world.create_filler() for _ in dropped)

    for location, item in placements:
        location.place_locked_item(item)
