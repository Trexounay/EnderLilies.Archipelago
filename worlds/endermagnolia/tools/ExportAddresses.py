import importlib.util
import os
import sys
import types

_world = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __package__ not in (None, ""):
    from ..Items import items
    from ..Locations import locations
else:
    _pkg = "endermagnolia_export"
    _mod = types.ModuleType(_pkg)
    _mod.__path__ = [_world]
    sys.modules[_pkg] = _mod

    def _load(name):
        spec = importlib.util.spec_from_file_location(
            f"{_pkg}.{name}", os.path.join(_world, f"{name}.py"))
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module

    _load("Items")
    items = sys.modules[f"{_pkg}.Items"].items
    locations = _load("Locations").locations


def export(output_dir: str) -> None:
    os.makedirs(output_dir, exist_ok=True)

    loc_path = os.path.join(output_dir, "locations.txt")
    with open(loc_path, "w", encoding="utf-8") as f:
        for data in sorted(locations.values(), key=lambda d: d.address):
            if data.address is None or data.key is None:
                continue
            f.write(f"{data.address}:{data.key}\n")

    item_path = os.path.join(output_dir, "items.txt")
    with open(item_path, "w", encoding="utf-8") as f:
        for data in sorted(items.values(), key=lambda d: d.code):
            if data.code is None or data.key is None:
                continue
            f.write(f"{data.code}:{data.key}\n")

    print(f"Wrote {loc_path} ({len(locations)} locations)")
    print(f"Wrote {item_path} ({len(items)} items)")


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(_world, "gen")
    export(out)
