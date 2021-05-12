import os
from pathlib import Path

BASE_DIR = Path(".")
SOURCE_DIR=Path.joinpath(BASE_DIR, "src")

# if the source directory does not exist
if not SOURCE_DIR.exists():
	os.makedirs(str(SOURCE_DIR))


OUTPUT_DIR=Path.joinpath(BASE_DIR
,"output")

# if the output directory does not exist
if not OUTPUT_DIR.exists():
	os.makedirs(str(OUTPUT_DIR))
