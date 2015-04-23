from multiprocessing import Manager
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
        self._man = Manager()
        self._items = self._man.list()

    def add_item(self, name, command, priority=10):  # 0 is highest
        item = (priority, escape(name), escape(command))
        self._items.append(item)
        self.flush()

    def flush(self):
        print "".join(["{{{1}|{2}}}".format(*item) for item in sorted(self._items)])
        sys.stdout.flush()

    def clear(self):
        self._items = self._man.list()