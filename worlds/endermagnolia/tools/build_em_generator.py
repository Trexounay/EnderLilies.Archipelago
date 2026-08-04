"""Minimal standalone Ender Magnolia seed generator build.
"""
import os
import sys
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
KEEP_WORLDS = {"generic"}
OUT = REPO / "build" / "EnderMagnolia.Randomizer"

os.chdir(REPO)
sys.path.insert(0, str(REPO))

import cx_Freeze

exes = [
    cx_Freeze.Executable(
        script=str(HERE / "em_generate.py"),
        target_name="GenerateSeed.exe",
        base=None,
    )
]

cx_Freeze.setup(
    name="EnderMagnoliaGenerate",
    version="1.0.0",
    description="Ender Magnolia offline seed generator",
    executables=exes,
    options={
        "build_exe": {
            "packages": ["worlds", "websockets"],
            "includes": ["rule_builder.cached_world"],
            "excludes": [
                "numpy", "Cython", "PySide2", "PIL", "pandas",
                "kivy", "kivymd", "kivy_deps", "sc2",
                "tkinter", "unittest", "pydoc_data",
                "test", "distutils", "setuptools", "pip",
                "cx_Freeze", "freeze_core", "lief", "sqlite3",
            ],
            "zip_include_packages": ["*"],
            "zip_exclude_packages": ["worlds"],
            "include_msvcr": False,
            "optimize": 1,
            "build_exe": str(OUT),
        },
    },
    script_args=["build_exe"],
)

worlds_dir = OUT / "lib" / "worlds"
for entry in worlds_dir.iterdir():
    if entry.is_dir() and entry.name not in KEEP_WORLDS:
        shutil.rmtree(entry)
        print(f"pruned {entry.name}")

(OUT / "custom_worlds").mkdir(exist_ok=True)

data_out = OUT / "data"
data_out.mkdir(exist_ok=True)
for name in ("options.yaml", "GLOBAL.apignore"):
    shutil.copyfile(REPO / "data" / name, data_out / name)
    print(f"added data/{name}")

