from multiprocessing import Lock
import sys

MAX_OUTPUT = 100 * 1024


def escape(string):
    string = string.replace("{", "\{")
    string = string.replace("}", "\}")
    string = string.replace("|", "\|")
    string = string.replace("\n", " ")
    return string


class Lighthouse(object):
    def __init__(self):
        self._items = []
        self._items_lock = Lock()

    def add_item(self, name, command):
        with self._items_lock:
            item = "{%s|%s}" % (escape(name), escape(command))
            self._items.append(item)
            self.flush()

    def flush(self):
        print "".join([item for item in self._items])
        sys.stdout.flush()

    def clear(self):
        with self._items_lock:
            self._items = []