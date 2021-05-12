from pathlib import Path 

BASE_DIR = Path().absolute()
SOURCE_DIR=Path.joinpath(BASE_DIR, "src")

storage, _=str(BASE_DIR).split("0")
INTERNAL_STORAGE =storage + "0"

OUTPUT_DIR=Path.joinpath(Path(INTERNAL_STORAGE) ,"movieditor_dir")
