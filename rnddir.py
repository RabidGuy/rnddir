# Todo:
#
# - - - - - - - - - - - - - - - - - - -
#
# Keep track of recent output in order to avoid sudden repeats.
#
#   Method 1) List last few choices in file equal to (length_of_listdir // 2).
#   Generate list of directories *excluding* those in recents file.
#
#   Method 2) List all known directories in file popping index zero for next
#   map, then re-insert map into random position after mid-point.

import os


def get_local_directories():
    cwd = os.getcwd()
    local_contents = os.listdir()
    directories = []
    for item in local_contents:
        item_path = os.sep.join([cwd, item])
        if os.path.isdir(item_path):
            directories.append(item)
    return directories


if __name__ == "__main__":
    from random import choice
    ldirs = get_local_directories()
    map_dir = choice(ldirs)
    map_name = map_dir
    try:
        with open(os.sep.join([map_dir, ".dircfg"])) as f:
            line = f.readline().strip()
            if line:
                map_name = line + ("\n%s%s" % (map_name, os.sep))
            else:
                map_name = "Invalid Name!" + ("\n%s%s" % (map_name, os.sep))
    except FileNotFoundError:
        pass
    print(map_name)
