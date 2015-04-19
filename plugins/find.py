import os
import subprocess


def get(lighthouse, query):
    proc = subprocess.Popen(["find", os.path.expanduser("~"), "-name", query], stdout=subprocess.PIPE)
    find_out, err = proc.communicate()
    find_array = find_out.split("\n")[:-1]
    if len(find_array) == 0:
        return

    command = find_array[0]
    lighthouse.add_item(command, "urxvt -e zsh -c %s" % command)