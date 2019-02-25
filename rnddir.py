# Todo:
#
# - - - - - - - - - - - - - - - - - - -
#
# Update config file to JSON so that values can be stored in associative array.
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

import os
import random


FILENAME_CONFIG = ".rnddircfg"
# FILENAME_HISTORY = ".rnddirhist"
# DEFAULT_HISTORY_LINES = 5


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
    return random.choice(ldirs) + os.sep


if __name__ == "__main__":
    directory = choose_random_directory()
    try:
        with open(os.sep.join([directory, FILENAME_CONFIG])) as f:
            line = f.readline().strip()
            if line:
                out = line + ("\n%s" % directory)
            else:
                out = ("No name given in %s" %
                       (directory + FILENAME_CONFIG)
                      ) + ("\n%s" % directory)
    except FileNotFoundError:
        out = directory
    print(out)
