import os
import pkgutil
import typing

import Utils
from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes

from . import poke_data
from .items import item_table
from .text import encode_text
from .pokemon import set_mon_palettes
from .regions import PokemonRBWarp, map_ids, town_map_coords
from .rock_tunnel import randomize_rock_tunnel
from .rom_addresses import rom_addresses

if typing.TYPE_CHECKING:
    from . import PokemonRedBlueWorld


class PokemonRedProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Pokemon Red and Blue"
    hash = "3d45c1ee9abd5738df46d2bdda8b57dc"
    patch_file_ending = ".apred"
    result_file_ending = ".gb"

    procedure = [
        ("apply_bsdiff4", ["base_patch.bsdiff4"]),
        ("apply_tokens", ["token_data.bin"]),
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
        from . import PokemonRedBlueWorld
        with open(PokemonRedBlueWorld.settings.red_rom_file, "rb") as infile:
            base_rom_bytes = bytes(infile.read())

        return base_rom_bytes


class PokemonBlueProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Pokemon Red and Blue"
    hash = "50927e843568814f7ed45ec4f944bd8b"
    patch_file_ending = ".apblue"
    result_file_ending = ".gb"

    procedure = [
        ("apply_bsdiff4", ["base_patch.bsdiff4"]),
        ("apply_tokens", ["token_data.bin"]),
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
        from . import PokemonRedBlueWorld
        with open(PokemonRedBlueWorld.settings.blue_rom_file, "rb") as infile:
            base_rom_bytes = bytes(infile.read())

        return base_rom_bytes


def write_quizzes(world: "PokemonRedBlueWorld", patch: PokemonBlueProcedurePatch | PokemonRedProcedurePatch):
    random = world.random

    def get_quiz(q: int, a: int):
        if q == 0:
            r = random.randint(0, 3)
            if r == 0:
                mon = world.trade_mons["Trade_Dux"]
                text = "A woman in<LINE>Vermilion City<CONT>"
            elif r == 1:
                mon = world.trade_mons["Trade_Lola"]
                text = "A man in<LINE>Cerulean City<CONT>"
            elif r == 2:
                mon = world.trade_mons["Trade_Marcel"]
                text = "Someone on Route 2<LINE>"
            elif r == 3:
                mon = world.trade_mons["Trade_Spot"]
                text = "Someone on Route 5<LINE>"
            if not a:
                answers.append(0)
                old_mon = mon
                while old_mon == mon:
                    mon = random.choice(list(poke_data.pokemon_data.keys()))

            return encode_text(f"{text}was looking for<CONT>{mon}?<DONE>")
        elif q == 1:
            for location in world.multiworld.get_filled_locations():
                if location.item.name == "Secret Key" and location.item.player == world.player:
                    break
            player_name = world.multiworld.player_name[location.player]
            if not a:
                if len(world.multiworld.player_name) > 1:
                    old_name = player_name
                    while old_name == player_name:
                        player_name = random.choice(list(world.multiworld.player_name.values()))
                else:
                    return encode_text("You're playing<LINE>in a multiworld<CONT>with other<CONT>players?<DONE>")
            if world.multiworld.get_entrance(
                    "Cinnabar Island-G to Cinnabar Gym", world.player).connected_region.name == "Cinnabar Gym":
                if player_name == world.multiworld.player_name[world.player]:
                    player_name = "yourself"
                player_name = encode_text(player_name, force=True, safety=True)
                return encode_text(f"The Secret Key was<LINE>found by<CONT>") + player_name + encode_text("?<DONE>")
            else:
                # Might not have found it yet
                if player_name == world.multiworld.player_name[world.player]:
                    return encode_text(f"The Secret Key was<LINE>placed in<CONT>your own world?<DONE>")
                player_name = encode_text(player_name, force=True, safety=True)
                return (encode_text(f"The Secret Key was<LINE>placed in<CONT>") + player_name
                        + encode_text("'s<CONT>world?<DONE>"))
        elif q == 2:
            if a:
                return encode_text(f"#mon is<LINE>pronounced<CONT>Po-kay-mon?<DONE>")
            else:
                if random.randint(0, 1):
                    return encode_text(f"#mon is<LINE>pronounced<CONT>Po-key-mon?<DONE>")
                else:
                    return encode_text(f"#mon is<LINE>pronounced<CONT>Po-kuh-mon?<DONE>")
        elif q == 3:
            starters = [" ".join(world.multiworld.get_location(
                f"Oak's Lab - Starter {i}", world.player).item.name.split(" ")[1:]) for i in range(1, 4)]
            mon = random.choice(starters)
            nots = random.choice(range(8, 16, 2))
            if random.randint(0, 1):
                while mon in starters:
                    mon = random.choice(list(poke_data.pokemon_data.keys()))
                    if a:
                        nots += 1
            elif not a:
                nots += 1
            text = f"{mon} was<LINE>"
            while nots > 0:
                i = random.randint(1, min(4, nots))
                text += ("not " * i) + "<CONT>"
                nots -= i
            text += "a starter choice?<DONE>"
            return encode_text(text)
        elif q == 4:
            if a:
                tm_text = world.local_tms[27]
            else:
                if world.options.randomize_tm_moves:
                    wrong_tms = world.local_tms.copy()
                    wrong_tms.pop(27)
                    tm_text = random.choice(wrong_tms)
                else:
                    tm_text = "TOMBSTONER"
            return encode_text(f"TM28 contains<LINE>{tm_text.upper()}?<DONE>")
        elif q == 5:
            i = 8
            while not a and i in [1, 8]:
                i = random.randint(0, int("99999999"[random.randint(0, 7):]))
            return encode_text(f"There are {i}<LINE>certified #MON<CONT>LEAGUE BADGEs?<DONE>")
        elif q == 6:
            i = 2
            while not a and i in [1, 2]:
                i = random.randint(0, random.choice([9, 99]))
            return encode_text(f"POLIWAG evolves {i}<LINE>times?<DONE>")
        elif q == 7:
            q2 = random.randint(0, 2)
            if q2 == 0:
                entity = "Motor Carrier"
                if not a:
                    entity = random.choice(["Driver", "Shipper"])
                return encode_text("Title 49 of the<LINE>U.S. Code of<CONT>Federal<CONT>Regulations part<CONT>397.67 "
                                   f"states<CONT>that the<CONT>{entity}<CONT>is responsible<CONT>for planning<CONT>"
                                   "routes when<CONT>hazardous<CONT>materials are<CONT>transported?<DONE>")
            elif q2 == 1:
                if a:
                    state = random.choice(
                        ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
                         "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas",
                         "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
                         "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Jersey", "New Mexico",
                         "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
                         "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
                         "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"])
                else:
                    state = "New Hampshire"
                return encode_text(
                    f"As of 2024,<LINE>{state}<CONT>has a law<CONT>requiring all<CONT>front seat vehicle<CONT>occupants to use<CONT>seatbelts?<DONE>")
            elif q2 == 2:
                if a:
                    country = random.choice(["The United States", "Mexico", "Canada", "Germany", "France", "China",
                                             "Russia", "Spain", "Brazil", "Ukraine", "Saudi Arabia", "Egypt"])
                else:
                    country = random.choice(["The U.K.", "Pakistan", "India", "Japan", "Australia",
                                             "New Zealand", "Thailand"])
                return encode_text(f"As of 2020,<LINE>drivers in<CONT>{country}<CONT>drive on the<CONT>right side of<CONT>the road?<DONE>")
        elif q == 8:
            mon = random.choice(list(poke_data.evolution_levels.keys()))
            level = poke_data.evolution_levels[mon]
            if not a:
                level += random.choice(range(1, 6)) * random.choice((-1, 1))
            return encode_text(f"{mon} evolves<LINE>at level {level}?<DONE>")
        elif q == 9:
            move = random.choice(list(world.local_move_data.keys()))
            actual_type = world.local_move_data[move]["type"]
            question_type = actual_type
            while question_type == actual_type and not a:
                question_type = random.choice(list(poke_data.type_ids.keys()))
            return encode_text(f"{move} is<LINE>{question_type} type?<DONE>")
        elif q == 10:
            mon = random.choice(list(poke_data.pokemon_data.keys()))
            actual_type = world.local_poke_data[mon][random.choice(("type1", "type2"))]
            question_type = actual_type
            while question_type in [world.local_poke_data[mon]["type1"], world.local_poke_data[mon]["type2"]] and not a:
                question_type = random.choice(list(poke_data.type_ids.keys()))
            return encode_text(f"{mon} is<LINE>{question_type} type?<DONE>")
        elif q == 11:
            equation = ""
            while "*" not in equation:
                equation = f"{random.randint(0, 9)} {random.choice(['+', '-', '*'])} {random.randint(0, 9)} {random.choice(['+', '-', '*'])} {random.randint(0, 9)} {random.choice(['+', '-', '*'])} {random.randint(0, 9)}"
            result = eval(equation)
            question_result = result
            if not a:
                modifiers = random.sample(range(3), 3)
                for modifier in modifiers:
                    question_result = eval(equation[:modifier * 4] + "(" + equation[modifier * 4:(modifier * 4) + 5]
                                           + ")" + equation[5 + (modifier * 4):])
                    if question_result != result:
                        break
                else:
                    question_result += random.choice(range(1, 6)) * random.choice((-1, 1))

            return encode_text(f"{equation}<LINE>= {question_result}?<DONE>")
        elif q == 12:
            route = random.choice((12, 16))
            actual_mon = world.multiworld.get_location(f"Route {route} - Sleeping Pokemon",
                                                       world.player).item.name.split("Static ")[1]
            question_mon = actual_mon
            while question_mon == actual_mon and not a:
                question_mon = random.choice(list(poke_data.pokemon_data.keys()))
            return encode_text(f"{question_mon} was<LINE>sleeping on route<CONT>{route}?<DONE>")
        elif q == 13:
            type1 = random.choice(list(poke_data.type_ids.keys()))
            type2 = random.choice(list(poke_data.type_ids.keys()))
            eff_msgs = ["super effective<CONT>", "no ", "not very<CONT>effective<CONT>", "normal "]
            for matchup in world.type_chart:
                if matchup[0] == type1 and matchup[1] == type2:
                    if matchup[2] > 10:
                        eff = eff_msgs[0]
                    elif matchup[2] == 0:
                        eff = eff_msgs[1]
                    elif matchup[2] < 10:
                        eff = eff_msgs[2]
                    else:
                        eff = eff_msgs[3]
                    break
            else:
                eff = eff_msgs[3]
            if not a:
                eff_msgs.remove(eff)
                eff = random.choice(eff_msgs)
            return encode_text(f"{type1} deals<LINE>{eff}damage to<CONT>{type2} type?<DONE>")
        elif q == 14:
            fossil_level = world.multiworld.get_location("Fossil Level - Trainer Parties",
                                                         world.player).party_data[0]["level"]
            if not a:
                fossil_level += random.choice((-5, 5))
            return encode_text(f"Fossil #MON<LINE>revive at level<CONT>{fossil_level}?<DONE>")
        elif q == 15:
            if a:
                fodmap = random.choice(["garlic", "onion", "milk", "watermelon", "cherries", "wheat", "barley",
                                        "pistachios", "cashews", "kidney beans", "apples", "honey"])
            else:
                fodmap = random.choice(["carrots", "potatoes", "oranges", "pineapple", "blueberries", "parmesan",
                                        "eggs", "beef", "chicken", "oat", "rice", "maple syrup", "peanuts"])
            are_is = "are" if fodmap[-1] == "s" else "is"
            return encode_text(f"According to<LINE>Monash Uni.,<CONT>{fodmap} {are_is}<CONT>considered high<CONT>in FODMAPs?<DONE>")

    answers = [random.randint(0, 1) for _ in range(6)]
    questions = random.sample((range(0, 16)), 6)
    question_texts: list[bytearray] = []
    for i, question in enumerate(questions):
        question_texts.append(get_quiz(question, answers[i]))

    for i, quiz in enumerate(["A", "B", "C", "D", "E", "F"]):
        patch.write_token(APTokenTypes.WRITE, rom_addresses[f"Quiz_Answer_{quiz}"], bytes([int(not answers[i]) << 4 | (i + 1)]))
        patch.write_token(APTokenTypes.WRITE, rom_addresses[f"Text_Quiz_{quiz}"], bytes(question_texts[i]))


def generate_output(world: "PokemonRedBlueWorld", output_directory: str):
    game_version = world.options.game_version.current_key

    patch_type = PokemonBlueProcedurePatch if game_version == "blue" else PokemonRedProcedurePatch
    patch = patch_type(player=world.player, player_name=world.player_name)
    patch.write_file("base_patch.bsdiff4", pkgutil.get_data(__name__, f"basepatch_{game_version}.bsdiff4"))

    def write_bytes(address: int, data: typing.Sequence[int] | int):
        if isinstance(data, int):
            data = bytes([data])
        else:
            data = bytes(data)

        patch.write_token(APTokenTypes.WRITE, address, data)

    pallet_connections = {entrance: world.multiworld.get_entrance(f"Pallet Town to {entrance}",
                                                                  world.player).connected_region.name
                          for entrance in ["Player's House 1F", "Oak's Lab", "Rival's House"]}
    paths = None

    if pallet_connections["Player's House 1F"] == "Oak's Lab":
        paths = (bytes([0x00, 4, 0x80, 5, 0x40, 1, 0xE0, 1, 0xFF]), bytes([0x40, 2, 0x20, 5, 0x80, 5, 0xFF]))
    elif pallet_connections["Rival's House"] == "Oak's Lab":
        paths = (bytes([0x00, 4, 0xC0, 3, 0x40, 1, 0xE0, 1, 0xFF]), bytes([0x40, 2, 0x10, 3, 0x80, 5, 0xFF]))

    if paths:
        write_bytes(rom_addresses["Path_Pallet_Oak"], paths[0])
        write_bytes(rom_addresses["Path_Pallet_Player"], paths[1])

    if pallet_connections["Rival's House"] == "Player's House 1F":
        write_bytes(rom_addresses["Pallet_Fly_Coords"], [0x2F, 0xC7, 0x06, 0x0D, 0x00, 0x01])
    elif pallet_connections["Oak's Lab"] == "Player's House 1F":
        write_bytes(rom_addresses["Pallet_Fly_Coords"], [0x5F, 0xC7, 0x0C, 0x0C, 0x00, 0x00])

    for region in world.multiworld.get_regions(world.player):
        for entrance in region.exits:
            if isinstance(entrance, PokemonRBWarp):
                world.multiworld.spoiler.set_entrance(entrance.name, entrance.connected_region.name, "entrance",
                                                      world.player)
                warp_ids = (entrance.warp_id,) if isinstance(entrance.warp_id, int) else entrance.warp_id
                warp_to_ids = (entrance.target,) if isinstance(entrance.target, int) else entrance.target
                for i, warp_id in enumerate(warp_ids):
                    address = rom_addresses[entrance.address]
                    if "Elevator" in entrance.parent_region.name:
                        address += (2 * warp_id)
                    else:
                        address += (4 * warp_id)
                    while i > len(warp_to_ids) - 1:
                        i -= len(warp_to_ids)
                    connected_map_name = entrance.connected_region.name.split("-")[0]
                    write_bytes(address, [
                        0 if "Elevator" in connected_map_name else warp_to_ids[i],
                        map_ids[connected_map_name]
                    ])

    if world.options.door_shuffle == "simple":
        for (entrance, _, _, map_coords_entries, map_name, _) in town_map_coords.values():
            destination = world.multiworld.get_entrance(entrance, world.player).connected_region.name
            (_, x, y, _, _, map_order_entry) = town_map_coords[destination]
            for map_coord_entry in map_coords_entries:
                write_bytes(rom_addresses["Town_Map_Coords"] + (map_coord_entry * 4) + 1, (y << 4) | x)
            write_bytes(rom_addresses["Town_Map_Order"] + map_order_entry, map_ids[map_name])

    if not world.options.key_items_only:
        for i, gym_leader in enumerate(("Pewter Gym - Brock TM", "Cerulean Gym - Misty TM",
                                        "Vermilion Gym - Lt. Surge TM", "Celadon Gym - Erika TM",
                                        "Fuchsia Gym - Koga TM", "Saffron Gym - Sabrina TM",
                                        "Cinnabar Gym - Blaine TM", "Viridian Gym - Giovanni TM")):
            item_name = world.multiworld.get_location(gym_leader, world.player).item.name
            if item_name.startswith("TM"):
                try:
                    tm = int(item_name[2:4])
                    move = poke_data.moves[world.local_tms[tm - 1]]["id"]
                    write_bytes(rom_addresses["Gym_Leader_Moves"] + (2 * i), move)
                except KeyError:
                    pass

    def set_trade_mon(address, loc):
        mon = world.multiworld.get_location(loc, world.player).item.name
        write_bytes(rom_addresses[address], poke_data.pokemon_data[mon]["id"])
        world.trade_mons[address] = mon

    if game_version == "red":
        set_trade_mon("Trade_Terry", "Safari Zone Center - Wild Pokemon - 5")
        set_trade_mon("Trade_Spot", "Safari Zone East - Wild Pokemon - 1")
    else:
        set_trade_mon("Trade_Terry", "Safari Zone Center - Wild Pokemon - 7")
        set_trade_mon("Trade_Spot", "Safari Zone East - Wild Pokemon - 7")
    set_trade_mon("Trade_Marcel", "Route 24 - Wild Pokemon - 6")
    set_trade_mon("Trade_Sailor", "Pokemon Mansion 1F - Wild Pokemon - 3")
    set_trade_mon("Trade_Dux", "Route 3 - Wild Pokemon - 2")
    set_trade_mon("Trade_Marc", "Route 23/Cerulean Cave Fishing - Super Rod Pokemon - 1")
    set_trade_mon("Trade_Lola", "Route 10/Celadon Fishing - Super Rod Pokemon - 1")
    set_trade_mon("Trade_Doris", "Cerulean Cave 1F - Wild Pokemon - 9")
    set_trade_mon("Trade_Crinkles", "Route 12 - Wild Pokemon - 4")

    write_bytes(rom_addresses["Fly_Location"], world.fly_map_code)
    write_bytes(rom_addresses["Map_Fly_Location"], world.town_map_fly_map_code)

    if world.options.fix_combat_bugs:
        write_bytes(rom_addresses["Option_Fix_Combat_Bugs"], 1)
        write_bytes(rom_addresses["Option_Fix_Combat_Bugs_Focus_Energy"],  0x28)  # jr z
        write_bytes(rom_addresses["Option_Fix_Combat_Bugs_HP_Drain_Dream_Eater"], 0x1A)  # ld a, (de)
        write_bytes(rom_addresses["Option_Fix_Combat_Bugs_PP_Restore"], 0xe6)  # and a, direct
        write_bytes(rom_addresses["Option_Fix_Combat_Bugs_PP_Restore"] + 1, 0b0011111)
        write_bytes(rom_addresses["Option_Fix_Combat_Bugs_Struggle"], 0xe6)  # and a, direct
        write_bytes(rom_addresses["Option_Fix_Combat_Bugs_Struggle"] + 1, 0x3f)
        write_bytes(rom_addresses["Option_Fix_Combat_Bugs_Dig_Fly"], 0b10001100)
        write_bytes(rom_addresses["Option_Fix_Combat_Bugs_Heal_Effect"], 0x20)  # jr nz,
        write_bytes(rom_addresses["Option_Fix_Combat_Bugs_Heal_Effect"] + 1, 5)  # 5 bytes ahead
        write_bytes(rom_addresses["Option_Fix_Combat_Bugs_Heal_Stat_Modifiers"], 1)

    if world.options.poke_doll_skip == "in_logic":
        write_bytes(rom_addresses["Option_Silph_Scope_Skip"], 0x00)      # nop
        write_bytes(rom_addresses["Option_Silph_Scope_Skip"] + 1, 0x00)  # nop
        write_bytes(rom_addresses["Option_Silph_Scope_Skip"] + 2, 0x00)  # nop

    if world.options.bicycle_gate_skips == "patched":
        write_bytes(rom_addresses["Option_Route_16_Gate_Fix"], 0x00)      # nop
        write_bytes(rom_addresses["Option_Route_16_Gate_Fix"] + 1, 0x00)  # nop
        write_bytes(rom_addresses["Option_Route_18_Gate_Fix"], 0x00)      # nop
        write_bytes(rom_addresses["Option_Route_18_Gate_Fix"] + 1, 0x00)  # nop

    if world.options.door_shuffle:
        write_bytes(rom_addresses["Entrance_Shuffle_Fuji_Warp"], 1)  # prevent warping to Fuji's House from Pokemon Tower 7F

    if world.options.all_elevators_locked:
        write_bytes(rom_addresses["Option_Locked_Elevator_Celadon"], 0x20)  # jr nz
        write_bytes(rom_addresses["Option_Locked_Elevator_Silph"], 0x20)    # jr nz

    if world.options.tea:
        write_bytes(rom_addresses["Option_Tea"], 1)
        write_bytes(rom_addresses["Guard_Drink_List"], 0x54)
        write_bytes(rom_addresses["Guard_Drink_List"] + 1, 0)
        write_bytes(rom_addresses["Guard_Drink_List"] + 2, 0)
        write_bytes(rom_addresses["Text_Saffron_Gate"],
                    encode_text("<LINE>Gee, I have the<CONT>worst caffeine<CONT>headache though."
                                "<PARA>Oh wait there,<LINE>the road's closed.<DONE>"))

        write_bytes(rom_addresses["Tea_Key_Item_A"], 0x28)  #  jr .z
        write_bytes(rom_addresses["Tea_Key_Item_B"], 0x28)  #  jr .z
        write_bytes(rom_addresses["Tea_Key_Item_C"], 0x28)  #  jr .z

    write_bytes(rom_addresses["Fossils_Needed_For_Second_Item"], world.options.second_fossil_check_condition.value)

    write_bytes(rom_addresses["Option_Lose_Money"], int(not world.options.lose_money_on_blackout.value))

    if world.options.extra_key_items:
        write_bytes(rom_addresses["Option_Extra_Key_Items_A"], 1)
        write_bytes(rom_addresses["Option_Extra_Key_Items_B"], 1)
        write_bytes(rom_addresses["Option_Extra_Key_Items_C"], 1)
        write_bytes(rom_addresses["Option_Extra_Key_Items_D"], 1)
    write_bytes(rom_addresses["Option_Split_Card_Key"], world.options.split_card_key.value)
    write_bytes(rom_addresses["Option_Blind_Trainers"], round(world.options.blind_trainers.value * 2.55))
    write_bytes(rom_addresses["Option_Cerulean_Cave_Badges"], world.options.cerulean_cave_badges_condition.value)
    write_bytes(rom_addresses["Option_Cerulean_Cave_Key_Items"], world.options.cerulean_cave_key_items_condition.total)
    write_bytes(rom_addresses["Text_Cerulean_Cave_Badges"], encode_text(str(world.options.cerulean_cave_badges_condition.value)))
    write_bytes(rom_addresses["Text_Cerulean_Cave_Key_Items"], encode_text(str(world.options.cerulean_cave_key_items_condition.total) + " key items."))
    write_bytes(rom_addresses["Option_Encounter_Minimum_Steps"], world.options.minimum_steps_between_encounters.value)
    write_bytes(rom_addresses["Option_Route23_Badges"], world.options.victory_road_condition.value)
    write_bytes(rom_addresses["Option_Victory_Road_Badges"], world.options.route_22_gate_condition.value)
    write_bytes(rom_addresses["Option_Elite_Four_Pokedex"], world.options.elite_four_pokedex_condition.total)
    write_bytes(rom_addresses["Option_Elite_Four_Key_Items"], world.options.elite_four_key_items_condition.total)
    write_bytes(rom_addresses["Option_Elite_Four_Badges"], world.options.elite_four_badges_condition.value)
    write_bytes(rom_addresses["Text_Elite_Four_Badges"], encode_text(str(world.options.elite_four_badges_condition.value)))
    write_bytes(rom_addresses["Text_Elite_Four_Key_Items"], encode_text(str(world.options.elite_four_key_items_condition.total) + " key items, and"))
    write_bytes(rom_addresses["Text_Elite_Four_Pokedex"], encode_text(str(world.options.elite_four_pokedex_condition.total) + " #MON"))
    write_bytes(rom_addresses["Trainer_Screen_Total_Key_Items"], encode_text(str(world.total_key_items), length=2))

    write_bytes(rom_addresses["Option_Viridian_Gym_Badges"], world.options.viridian_gym_condition.value)
    write_bytes(rom_addresses["Option_EXP_Modifier"], world.options.exp_modifier.value)
    if not world.options.require_item_finder:
        write_bytes(rom_addresses["Option_Itemfinder"], 0)  # nop
    if world.options.extra_strength_boulders:
        for i in range(0, 3):
            write_bytes(rom_addresses["Option_Boulders"] + (i * 3), 0x15)
    if world.options.extra_key_items:
        for i in range(0, 4):
            write_bytes(rom_addresses["Option_Rock_Tunnel_Extra_Items"] + (i * 3), 0x15)
    if world.options.old_man == "open_viridian_city":
        write_bytes(rom_addresses["Option_Old_Man"], 0x11)
        write_bytes(rom_addresses["Option_Old_Man_Lying"], 0x15)
    write_bytes(rom_addresses["Option_Route3_Guard_B"], world.options.route_3_condition.value)
    if world.options.route_3_condition == "open":
        write_bytes(rom_addresses["Option_Route3_Guard_A"], 0x11)
    if not world.options.robbed_house_officer:
        write_bytes(rom_addresses["Option_Trashed_House_Guard_A"], 0x15)
        write_bytes(rom_addresses["Option_Trashed_House_Guard_B"], 0x11)
    if world.options.require_pokedex:
        write_bytes(rom_addresses["Require_Pokedex_A"], 1)
        write_bytes(rom_addresses["Require_Pokedex_B"], 1)
        write_bytes(rom_addresses["Require_Pokedex_C"], 1)
    else:
        write_bytes(rom_addresses["Require_Pokedex_D"], 0x18)  # jr
    if world.options.dexsanity:
        write_bytes(rom_addresses["Option_Dexsanity_A"], 1)
        write_bytes(rom_addresses["Option_Dexsanity_B"], 1)
    if world.options.all_pokemon_seen:
        write_bytes(rom_addresses["Option_Pokedex_Seen"], 1)
    money = str(world.options.starting_money.value).zfill(6)
    write_bytes(rom_addresses["Starting_Money_High"], int(money[:2], 16))
    write_bytes(rom_addresses["Starting_Money_Middle"], int(money[2:4], 16))
    write_bytes(rom_addresses["Starting_Money_Low"], int(money[4:], 16))
    write_bytes(rom_addresses["Text_Badges_Needed_Viridian_Gym"],
                encode_text(str(world.options.viridian_gym_condition.value))[0])
    write_bytes(rom_addresses["Text_Rt23_Badges_A"],
                encode_text(str(world.options.victory_road_condition.value))[0])
    write_bytes(rom_addresses["Text_Rt23_Badges_B"],
                encode_text(str(world.options.victory_road_condition.value))[0])
    write_bytes(rom_addresses["Text_Rt23_Badges_C"],
                encode_text(str(world.options.victory_road_condition.value))[0])
    write_bytes(rom_addresses["Text_Rt23_Badges_D"],
                encode_text(str(world.options.victory_road_condition.value))[0])
    write_bytes(rom_addresses["Text_Badges_Needed"],
                encode_text(str(world.options.elite_four_badges_condition.value))[0])
    write_bytes(rom_addresses["Text_Magikarp_Salesman"],
                encode_text(" ".join(world.multiworld.get_location("Route 4 Pokemon Center - Pokemon For Sale", world.player).item.name.upper().split()[1:])))

    if world.options.badges_needed_for_hm_moves.value == 0:
        for hm_move in poke_data.hm_moves:
            write_bytes(rom_addresses["HM_" + hm_move + "_Badge_a"], [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    elif world.extra_badges:
        written_badges = {}
        badge_codes = {"Boulder Badge": 0x47, "Cascade Badge": 0x4F,
                       "Thunder Badge": 0x57, "Rainbow Badge": 0x5F,
                       "Soul Badge": 0x67, "Marsh Badge": 0x6F,
                       "Volcano Badge": 0x77, "Earth Badge": 0x7F}
        for hm_move, badge in world.extra_badges.items():
            write_bytes(rom_addresses["HM_" + hm_move + "_Badge_b"], badge_codes[badge])
            move_text = hm_move
            if badge not in ["Marsh Badge", "Volcano Badge", "Earth Badge"]:
                move_text = ", " + move_text
            rom_address = rom_addresses["Badge_Text_" + badge.replace(" ", "_")]
            if badge in written_badges:
                rom_address += len(written_badges[badge])
                move_text = ", " + move_text
            write_bytes(rom_address, encode_text(move_text.upper()))
            written_badges[badge] = move_text
        for badge in ["Marsh Badge", "Volcano Badge", "Earth Badge"]:
            if badge not in written_badges:
                write_bytes(rom_addresses["Badge_Text_" + badge.replace(" ", "_")], encode_text("Nothing"))

    type_loc = rom_addresses["Type_Chart"]
    for matchup in world.type_chart:
        if matchup[2] != 10:  # don't needlessly divide damage by 10 and multiply by 10
            write_bytes(type_loc, [poke_data.type_ids[matchup[0]], poke_data.type_ids[matchup[1]], matchup[2]])
            type_loc += 3
    write_bytes(type_loc, b"\xFF\xFF\xFF")

    if world.options.normalize_encounter_chances.value:
        chances = [25, 51, 77, 103, 129, 155, 180, 205, 230, 255]
        for i, chance in enumerate(chances):
            write_bytes(rom_addresses["Encounter_Chances"] + (i * 2), chance)

    for mon, mon_data in world.local_poke_data.items():
        if mon == "Mew":
            address = rom_addresses["Base_Stats_Mew"]
        else:
            address = rom_addresses["Base_Stats"] + (28 * (mon_data["dex"] - 1))
        write_bytes(address + 1, world.local_poke_data[mon]["hp"])
        write_bytes(address + 2, world.local_poke_data[mon]["atk"])
        write_bytes(address + 3, world.local_poke_data[mon]["def"])
        write_bytes(address + 4, world.local_poke_data[mon]["spd"])
        write_bytes(address + 5, world.local_poke_data[mon]["spc"])
        write_bytes(address + 6, poke_data.type_ids[world.local_poke_data[mon]["type1"]])
        write_bytes(address + 7, poke_data.type_ids[world.local_poke_data[mon]["type2"]])
        write_bytes(address + 8, world.local_poke_data[mon]["catch rate"])
        write_bytes(address + 15, poke_data.moves[world.local_poke_data[mon]["start move 1"]]["id"])
        write_bytes(address + 16, poke_data.moves[world.local_poke_data[mon]["start move 2"]]["id"])
        write_bytes(address + 17, poke_data.moves[world.local_poke_data[mon]["start move 3"]]["id"])
        write_bytes(address + 18, poke_data.moves[world.local_poke_data[mon]["start move 4"]]["id"])
        write_bytes(address + 20, world.local_poke_data[mon]["tms"])
        if mon in world.learnsets and world.learnsets[mon]:
                address = rom_addresses["Learnset_" + mon.replace(" ", "")]
                for i, move in enumerate(world.learnsets[mon]):
                    write_bytes((address + 1) + i * 2, poke_data.moves[move]["id"])

    write_bytes(rom_addresses["Option_Aide_Rt2"], world.options.oaks_aide_rt_2.value)
    write_bytes(rom_addresses["Option_Aide_Rt11"], world.options.oaks_aide_rt_11.value)
    write_bytes(rom_addresses["Option_Aide_Rt15"], world.options.oaks_aide_rt_15.value)

    if world.options.safari_zone_normal_battles.value == 1:
        write_bytes(rom_addresses["Option_Safari_Zone_Battle_Type"], 255)

    if world.options.reusable_tms.value:
        write_bytes(rom_addresses["Option_Reusable_TMs"], 0xC9)

    write_bytes(rom_addresses["Option_Always_Half_STAB"], int(not world.options.same_type_attack_bonus.value))

    if world.options.better_shops:
        inventory = ["Poke Ball", "Great Ball", "Ultra Ball"]
        if world.options.better_shops.value == 2:
            inventory.append("Master Ball")
        inventory += ["Potion", "Super Potion", "Hyper Potion", "Max Potion", "Full Restore", "Revive", "Antidote",
                      "Awakening", "Burn Heal", "Ice Heal", "Paralyze Heal", "Full Heal", "Repel", "Super Repel",
                      "Max Repel", "Escape Rope"]
        shop_data = [0xFE, len(inventory)]
        shop_data += [item_table[item].id - 172000000 for item in inventory]
        shop_data.append(0xFF)
        for shop in range(1, 11):
            write_bytes(rom_addresses[f"Shop{shop}"], shop_data)
    if world.options.stonesanity:
        write_bytes(rom_addresses["Shop_Stones"], [0xFE, 1, item_table["Poke Doll"].id - 172000000, 0xFF])

    price = str(world.options.master_ball_price.value).zfill(6)
    price = [int(price[:2], 16), int(price[2:4], 16), int(price[4:], 16)]
    write_bytes(rom_addresses["Price_Master_Ball"], price)  # Money values in Red and Blue are weird

    from collections import Counter
    start_inventory = Counter(item.code for item in reversed(world.multiworld.precollected_items[world.player]))
    for item, value in start_inventory.items():
        write_bytes(rom_addresses["Start_Inventory"] + item - 172000000, min(value, 255))

    set_mon_palettes(world, patch)

    for move_data in world.local_move_data.values():
        if move_data["id"] == 0:
            continue
        address = rom_addresses["Move_Data"] + ((move_data["id"] - 1) * 6)
        write_bytes(address, [move_data["id"], move_data["effect"], move_data["power"],
                              poke_data.type_ids[move_data["type"]], round(move_data["accuracy"] * 2.55),
                              move_data["pp"]])

    TM_IDs = [poke_data.moves[move]["id"] for move in world.local_tms]
    write_bytes(rom_addresses["TM_Moves"], TM_IDs)

    if world.options.randomize_rock_tunnel:
        seed = randomize_rock_tunnel(patch, world.random)
        write_bytes(rom_addresses["Text_Rock_Tunnel_Sign"], encode_text(f"SEED: <LINE>{seed}"))

    mons = [mon["id"] for mon in poke_data.pokemon_data.values()]
    world.random.shuffle(mons)
    write_bytes(rom_addresses["Title_Mon_First"], mons.pop())
    for mon in range(0, 16):
        write_bytes(rom_addresses["Title_Mons"] + mon, mons.pop())
    if world.options.game_version.value:
        mons.sort(key=lambda mon: 0 if mon == world.multiworld.get_location("Oak's Lab - Starter 1", world.player).item.name
                  else 1 if mon == world.multiworld.get_location("Oak's Lab - Starter 2", world.player).item.name else
                  2 if mon == world.multiworld.get_location("Oak's Lab - Starter 3", world.player).item.name else 3)
    else:
        mons.sort(key=lambda mon: 0 if mon == world.multiworld.get_location("Oak's Lab - Starter 2", world.player).item.name
                  else 1 if mon == world.multiworld.get_location("Oak's Lab - Starter 1", world.player).item.name else
                  2 if mon == world.multiworld.get_location("Oak's Lab - Starter 3", world.player).item.name else 3)
    write_bytes(rom_addresses["Title_Seed"], encode_text(world.multiworld.seed_name[-20:], 20, True))

    slot_name = world.multiworld.player_name[world.player]
    slot_name.replace("@", " ")
    slot_name.replace("<", " ")
    slot_name.replace(">", " ")
    write_bytes(rom_addresses["Title_Slot_Name"], encode_text(slot_name, 16, True, True))

    if world.trainer_name == "choose_in_game":
        write_bytes(rom_addresses["Skip_Player_Name"], 0)
    else:
        write_bytes(rom_addresses["Player_Name"], world.trainer_name)
    if world.rival_name == "choose_in_game":
        write_bytes(rom_addresses["Skip_Rival_Name"], 0)
    else:
        write_bytes(rom_addresses["Rival_Name"], world.rival_name)

    write_bytes(0xFF00, 2)  # client compatibility version
    rom_name = bytearray(f"AP{Utils.__version__.replace('.', '')[0:3]}_{world.player}_{world.multiworld.seed:11}\0",
                          "utf8")[:21]
    rom_name.extend([0] * (21 - len(rom_name)))
    write_bytes(0xFFC6, rom_name)
    write_bytes(0xFFDB, world.multiworld.seed_name.encode())
    write_bytes(0xFFF0, world.multiworld.player_name[world.player].encode())

    world.finished_level_scaling.wait()

    write_quizzes(world, patch)

    for location in world.multiworld.get_locations(world.player):
        if location.party_data:
            for party in location.party_data:
                if not isinstance(party["party_address"], list):
                    addresses = [rom_addresses[party["party_address"]]]
                    parties = [party["party"]]
                else:
                    addresses = [rom_addresses[address] for address in party["party_address"]]
                    parties = party["party"]
                levels = party["level"]
                for address, party in zip(addresses, parties):
                    if isinstance(levels, int):
                        write_bytes(address, levels)
                        address += 1
                        for mon in party:
                            write_bytes(address, poke_data.pokemon_data[mon]["id"])
                            address += 1
                    else:
                        address += 1
                        for level, mon in zip(levels, party):
                            write_bytes(address, [level, poke_data.pokemon_data[mon]["id"]])
                            address += 2
                    # This assert can't be done with procedure patch tokens.
                    # assert data[address] == 0 or location.name == "Fossil Level - Trainer Parties"
            continue
        elif location.rom_address is None:
            continue
        if location.item and location.item.player == world.player:
            if location.rom_address:
                rom_address = location.rom_address
                if not isinstance(rom_address, list):
                    rom_address = [rom_address]
                for address in rom_address:
                    if location.item.name in poke_data.pokemon_data.keys():
                        write_bytes(address, poke_data.pokemon_data[location.item.name]["id"])
                    elif " ".join(location.item.name.split()[1:]) in poke_data.pokemon_data.keys():
                        write_bytes(address, poke_data.pokemon_data[" ".join(location.item.name.split()[1:])]["id"])
                    else:
                        item_id = world.item_name_to_id[location.item.name] - 172000000
                        if item_id > 255:
                            item_id -= 256
                        write_bytes(address, item_id)
                    if location.level:
                        write_bytes(location.level_address, location.level)

        else:
            rom_address = location.rom_address
            if not isinstance(rom_address, list):
                rom_address = [rom_address]
            for address in rom_address:
                write_bytes(address, 0x2C)  # AP Item

    patch.write_file("token_data.bin", patch.get_token_binary())
    out_file_name = world.multiworld.get_out_file_name_base(world.player)
    patch.write(os.path.join(output_directory, f"{out_file_name}{patch.patch_file_ending}"))
