# Todo:
#
# - - - - - - - - - - - - - - - - - - -
#
# Keep track of recent output in order to avoid sudden repeats.
#
#   Use Method 3.
#
#       Method 1) List last few choices in file equal to (length_of_listdir // N).
#       Generate list of directories *excluding* those in recents file.
#
#       Method 2) List all known directories in file popping index zero for next
#       map, then re-insert map into random position after mid-point.
#
#       Method 3) List last few choices in file equal to (length_of_listdir // N).
#       Attempt to select an unlisted, random directory a finite number of times.
#       If no choice is made within that many attempts, use directory selected at
#       last iteration.

import json
import os
import random


FILENAME_CONFIG = ".rnddircfg.json"
# FILENAME_HISTORY = ".rnddirhist"
# DEFAULT_HISTORY_LENGTH = 5


def get_local_directories():
    cwd = os.getcwd()
    local_contents = os.listdir()
    directories = []
    for item in local_contents:
        item_path = os.sep.join([cwd, item])
        if os.path.isdir(item_path):
            directories.append(item)
    return directories


def choose_random_directory():
    ldirs = get_local_directories()
    return random.choice(ldirs)


def get_directory_config(directory):
    """Get configuration options for chosen directory.

    Returns config object if valid config file exists,
    else returns None.

    """
    config_path = os.sep.join([directory, FILENAME_CONFIG])
    if os.path.exists(config_path):
        with open(os.sep.join([directory, FILENAME_CONFIG])) as f:
            config = json.load(f)
        return config
    else:
        return None


if __name__ == "__main__":
    directory = choose_random_directory()
    config = get_directory_config(directory)
    if config:
        try:
            out = "\n".join([config["name"], directory])
        except KeyError:
            out = directory
    else:
        out = directory
    print(out)
