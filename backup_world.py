# create zip of minecraft world
# copy to backup folder

import datetime
import shutil
import sys

world_path = "{ PATH TO MINECRAFT WORLD }"
folder_path = "{ PATH TO THIS FOLDER }"


def backup_world(backup_name: str):
    backup_path = f"{folder_path}/vanilla_oneblock/backups/{backup_name}"
    with open(f"{folder_path}/vanilla_oneblock/log.txt", "a") as f:
        f.write(f"{datetime.datetime.now().isoformat()} - backup {backup_name} taken\n")
    shutil.make_archive(backup_path, "zip", world_path)


# take in args for name of backup


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print("Please provide a name for the backup")
        sys.exit(1)
    backup_name = args[1]
    backup_world(backup_name)
