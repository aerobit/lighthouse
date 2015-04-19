#!/usr/bin/python2.7
from multiprocessing import Process
from lighthouse import Lighthouse
import plugins
import sys


# Load modules
modules = []
for name in plugins.__all__:
    __import__("plugins.%s" % name)
    modules.append(sys.modules["plugins.%s" % name])

lh = Lighthouse()
processes = []

while True:
    user_input = sys.stdin.readline()
    user_input = user_input[:-1]

    # Clear results
    lh.clear()
    for process in processes:
        process.terminate()

    # We don't handle empty strings
    if user_input == '':
        lh.flush()
        continue

    for module in modules:
            p = Process(target=module.get, args=(lh, user_input))
            p.start()
            processes.append(p)

    # Other options
    lh.add_item("google '%s'" % user_input, "xdg-open \"http://google.com/search?q=%s\"" % user_input)

    lh.add_item("execute %s" % user_input, user_input)

    lh.add_item("run '%s' in a shell" % user_input, "urxvt -e %s" % user_input)

    # Is this python?
    try:
        out = eval(user_input)
        if type(out) != str and str(out)[0] == '<':
            pass  # We don't want gibberish type stuff
        else:
            lh.add_item("python: " + str(out), "urxvt -e python2 -i -c 'print " + user_input + "'")
    except Exception as e:
        pass