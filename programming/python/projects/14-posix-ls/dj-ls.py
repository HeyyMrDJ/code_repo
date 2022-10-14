#!/usr/local/bin/python3
'Personal project to see if I can recreate ls using python'

from pathlib import Path
import typer
from rich import print
# Get list of current files in the current folder


def get_items(path='.', recurse: bool = False):
    'Function to grab list of items at current or specified directory'
    mypath = Path(path)
    for child in mypath.iterdir():
        # print(child)
        if child.is_dir():
            print(f"[green]{child} [/green]")
            if recurse is True:
                get_items(child, True)
        if child.is_file():
            print(f"[white]{child} [/white]")

# Use recursion to grab all files and folders from the current directory

# Allow a different path to be provided by user


def main(path='.', recurse: bool = False):
    'Main Function'
    get_items(path, recurse)


if __name__ == "__main__":
    typer.run(main)
