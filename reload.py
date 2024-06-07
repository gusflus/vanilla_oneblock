import datetime
import os
import shutil
import sys


def reload_world(backup_name: str):
    world_path = "/Users/gusflusser/Library/Application Support/minecraft/saves/Vanilla Skyblock/"
    with open("/Users/gusflusser/Projects/vanilla_oneblock/log.txt", "a") as f:
        f.write(f"{datetime.datetime.now().isoformat()} - reloaded {backup_name}\n")
    try:
        shutil.rmtree(world_path)
        os.makedirs(world_path)
        backup_path = (
            f"/Users/gusflusser/Projects/vanilla_oneblock/backups/{backup_name}.zip"
        )
        shutil.unpack_archive(backup_path, world_path)
    except FileNotFoundError:
        pass


# take in args for name of backup


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print("Please provide a name for the backup")
        sys.exit(1)
    backup_name = args[1]
    reload_world(backup_name)
