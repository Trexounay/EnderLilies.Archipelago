from typing import Collection, Dict, List, NamedTuple, Optional, Set, Tuple

from BaseClasses import CollectionState, Item, Location
from Fill import FillError, sweep_from_pool
from worlds.AutoWorld import World

MAX_BACKTRACKS = 200

Unit = List[Item]
Placement = Tuple[Location, Item]


class Frame(NamedTuple):
    state: CollectionState
    seen: Set[Location]
    spheres: List[List[Location]]
    used: Set[Location]
    items: List[Item]
    placements: List[Placement]
    candidates: Optional[List[Unit]]


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

    def minimal_group(self, frame: Frame, blocked: List[Item]) -> Unit:
        group = blocked
        order = list(blocked)
        self.random.shuffle(order)
        for item in order:
            trial = [other for other in group if other is not item]
            if trial and self.opens_new(frame, trial):
                group = trial
        return group

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
        items = [item for item in frame.items if id(item) not in taken]
        return Frame(state, set(found), frame.spheres + [fresh], used, items, placements, None)

    def expand(self, frame: Frame) -> Frame:
        ready: List[Unit] = []
        blocked: List[Item] = []
        opens: Dict[str, bool] = {}
        for item in frame.items:
            if item.name not in opens:
                opens[item.name] = self.opens_new(frame, [item])
                if opens[item.name]:
                    ready.append([item])
            if not opens[item.name]:
                blocked.append(item)

        candidates = ready
        room = self.free_slots(frame)
        if len(blocked) >= 2 and room >= 2 and self.opens_new(frame, blocked):
            group = self.minimal_group(frame, blocked)
            if len(group) <= room:
                candidates = ready + [group]

        self.random.shuffle(candidates)
        return frame._replace(candidates=candidates)

    def build(self, items: List[Item]) -> Tuple[List[Placement], List[Item]]:
        state = sweep_from_pool(CollectionState(self.world.multiworld), locations=self.locations)
        found = self.reachable(state)
        current = Frame(state, set(found), [found], set(), items, [], None)

        stack: List[Frame] = []
        budget = MAX_BACKTRACKS

        while current.items:
            if current.candidates is None:
                current = self.expand(current)
                if not current.candidates and not self.opens_new(current, current.items):
                    return current.placements, current.items

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


def remove_dead_events(world: World) -> None:
    locations = world.multiworld.get_locations(world.player)
    pool = [item for item in world.multiworld.itempool if item.player == world.player]
    state = sweep_from_pool(CollectionState(world.multiworld), pool, locations)

    dead = [location for location in locations
            if location.is_event and not location.can_reach(state)]
    for location in dead:
        location.parent_region.locations.remove(location)


def meta_progression_fill(world: World) -> None:
    items = [item for item in world.multiworld.itempool
             if item.player == world.player and item.advancement]
    if not items:
        return

    placements, dropped = Chain(world).build(items)

    chained = {id(item) for item in items}
    world.multiworld.itempool[:] = [item for item in world.multiworld.itempool
                                    if id(item) not in chained]
    world.multiworld.itempool.extend(world.create_filler() for _ in dropped)

    for location, item in placements:
        location.place_locked_item(item)

    remove_dead_events(world)
