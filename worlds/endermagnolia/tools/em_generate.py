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
TEMPLATES_DIR = "templates"
ERROR_LOG = "generate_error.txt"


def find_template(templates_dir: str) -> str:
    if os.path.isdir(templates_dir):
        for name in sorted(os.listdir(templates_dir)):
            if name.endswith(".yaml"):
                return os.path.join(templates_dir, name)

    from Options import generate_yaml_templates

    generate_yaml_templates(templates_dir, False)
    for name in sorted(os.listdir(templates_dir)):
        if name.endswith(".yaml"):
            return os.path.join(templates_dir, name)

    raise Exception(f"Could not find an option template for {GAME}")


def main() -> None:
    here = os.path.dirname(os.path.abspath(sys.executable))
    target = here

    settings.skip_autosave = True
    settings.get_settings._cache = settings.Settings(None)
    settings.get_settings().general_options.output_path = target

    template = find_template(os.path.join(here, TEMPLATES_DIR))

    active_yaml = os.path.join(here, YAML_NAME)
    if not os.path.exists(active_yaml):
        shutil.copyfile(template, active_yaml)
        print(f"Created {YAML_NAME} with default options")

    empty_dir = os.path.join(here, TEMPLATES_DIR, "Presets")
    os.makedirs(empty_dir, exist_ok=True)

    args = Generate.mystery_argparse()
    args.weights_file_path = active_yaml
    args.player_files_path = empty_dir
    args.multi = 1
    args.outputpath = target

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
        world.generate_output(target)
        written += 1

    if not written:
        raise Exception(f"No {GAME} player found in {active_yaml}")

    print(f"Seed written to {os.path.join(target, 'seed.txt')}")


if __name__ == "__main__":
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
