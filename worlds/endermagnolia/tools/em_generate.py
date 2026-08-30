"""Ender Magnolia offline seed generator.
"""
import os
import shutil
import sys

import settings
import Generate
from Main import main as ERmain

GAME = "Ender Magnolia"
YAML_NAME = "player.yaml"
SPOILER_NAME = "spoiler.txt"
TEMPLATES_DIR = "templates"
ERROR_LOG = "generate_error.txt"


def render_templates(target: str) -> str:
    import Utils
    from Options import generate_yaml_templates
    from worlds import AutoWorldRegister

    world = AutoWorldRegister.world_types.get(GAME)
    if world is None:
        raise Exception(f"{GAME} did not load, cannot render its template")

    required = world.manifest.get("minimum_ap_version")

    original = Utils.__version__
    try:
        if required:
            Utils.__version__ = required
        generate_yaml_templates(target, False)
    finally:
        Utils.__version__ = original

    return os.path.join(target, f"{GAME}.yaml")


def find_template(templates_dir: str) -> str:
    if os.path.isdir(templates_dir):
        for name in sorted(os.listdir(templates_dir)):
            if name.endswith(".yaml"):
                return os.path.join(templates_dir, name)

    return render_templates(templates_dir)


def main() -> None:
    exe_dir = os.path.dirname(os.path.abspath(sys.executable))

    settings.skip_autosave = True
    settings.get_settings._cache = settings.Settings(None)

    template = find_template(os.path.join(exe_dir, TEMPLATES_DIR))

    active_yaml = os.path.join(exe_dir, YAML_NAME)
    if not os.path.exists(active_yaml):
        shutil.copyfile(template, active_yaml)
        print(f"Created {YAML_NAME} with default options")

    empty_dir = os.path.join(exe_dir, TEMPLATES_DIR, "Presets")
    os.makedirs(empty_dir, exist_ok=True)

    args = Generate.mystery_argparse()
    args.weights_file_path = active_yaml
    args.player_files_path = empty_dir
    args.multi = 1
    args.outputpath = exe_dir

    erargs, seed = Generate.main(args)
    erargs.skip_output = True

    multiworld = ERmain(erargs, seed)

    if not multiworld.fulfills_accessibility():
        raise Exception("Generated seed is not accessible, aborting without writing the seed file")

    written = 0
    for player in multiworld.player_ids:
        if multiworld.game[player] != GAME:
            continue
        world = multiworld.worlds[player]
        world.options.generate_seed_file.value = 1
        world.generate_output(exe_dir)
        written += 1

    if not written:
        raise Exception(f"No {GAME} player found in {active_yaml}")

    print(f"Seed written to {os.path.join(exe_dir, 'seed.txt')}")

    spoiler_path = os.path.join(exe_dir, SPOILER_NAME)
    multiworld.spoiler.create_playthrough(create_paths=False)
    multiworld.spoiler.to_file(spoiler_path)
    print(f"Spoiler written to {spoiler_path}")


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--template":
        print(f"Template written to {render_templates(sys.argv[2])}")
        sys.exit(0)

    log_path = os.path.join(os.path.dirname(os.path.abspath(sys.executable)), ERROR_LOG)
    if os.path.exists(log_path):
        os.remove(log_path)

    try:
        main()
    except Exception:
        import traceback

        with open(log_path, "w", encoding="utf-8") as f:
            f.write(traceback.format_exc())
        sys.exit(1)
