#! /usr/bin/env python3

import fnmatch
from os import listdir
from os.path import sep, isdir
from pathlib import Path
from sys import argv, exit

from PIL import Image

HELP = """
Script to convert images to pdf

HOW TO USE:

    convert_img_to_pdf image.png
    convert_img_to_pdf .
    convert_img_to_pdf /home/user/Pictures 

If you want to change something, you have to modify the script
From Xizuth to the world
"""


def get_path_abs(path_raw: str):
    path_file = Path(path_raw) or Path(".")

    if not path_file.is_absolute():
        return path_file.absolute()

    return path_file


def get_name(full_path: str) -> dict:
    """
    """
    name = full_path.split(sep)[-1]
    return {"name": name.split(".")[0],
            "extension": name.split(".")[-1]}


def search_type(name_file: str) -> bool:
    extensions = ["png", "jpeg", "jpg"]

    for ext in extensions:
        if fnmatch.fnmatch(name_file, f"*.{ext}"):
            return True
    return False


def read_files_from_folder(path):
    dir_list = listdir(path)

    for file in dir_list:
        if search_type(file):
            convert_image(file)


def convert_image(path: str):
    path_img = get_path_abs(path)
    img = Image.open(path_img)
    img = img.convert("RGB")
    new_name = f'{get_name(path)["name"]}.pdf'

    img.save(new_name)
    print(f"Converted to: {get_path_abs(new_name)}")
    return img


def cli():
    if len(argv) < 2 or len(argv) > 2:
        print(HELP)
        exit(1)

    path_file = argv[1]

    if path_file == "--help":
        print(HELP)
        exit(0)

    try:
        if isdir(path_file):
            read_files_from_folder(path_file)
        else:
            convert_image(path_file)
    except Exception as e:
        print(e)
        print(HELP)
        exit(1)

    exit(0)


def main():
    cli()


if __name__ == "__main__":
    main()
