import os
import re
from xdg import BaseDirectory, DesktopEntry, IconTheme


def get(lighthouse, query):
    desktop_entry = find_desktop_entry(query)
    exec_path = get_xdg_exec(desktop_entry)
    icon = get_icon(desktop_entry)
    name = desktop_entry.getName()

    menu_entry = "%%I%s%%%s" % (icon, name) if icon else name

    lighthouse.add_item(menu_entry, exec_path)


def find_desktop_entry(cmd):
    desktop_files = []
    desktop_dirs = list(BaseDirectory.load_data_paths('applications'))
    for d in desktop_dirs:
        desktop_files += [os.path.join(d, name) for name in os.listdir(d)]

    matches = []
    for file_ in desktop_files:
        if cmd in file_:
            matches.append(file_)

    desktop_file = matches[0]
    desktop_entry = DesktopEntry.DesktopEntry(desktop_file)
    return desktop_entry


def get_icon(desktop_entry):
    icon_name = desktop_entry.getIcon()
    if not icon_name:
        return
    else:
        icon_path = IconTheme.getIconPath(icon_name)
        return icon_path


def get_xdg_exec(desktop_entry):
    exec_spec = desktop_entry.getExec()
    # The XDG exec string contains substitution patterns.
    exec_path = re.sub("%.", "", exec_spec).strip()
    return exec_path

# Plugin stuff
instance = None
