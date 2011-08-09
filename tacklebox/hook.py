#!/usr/bin/env python

import os
import sys
import subprocess


def run_hooks():
    hook = os.path.basename(__file__)
    hooks_dir = os.path.join(os.path.dirname(__file__), "_%s" % hook)
    hooks = os.listdir(hooks_dir)
    hooks.sort()
    for h in hooks:
        exe_path = os.path.join(hooks_dir, h)
        args = []
        if len(sys.argv) > 1:
            args = sys.argv[1:]
        retcode = subprocess.call([exe_path] + args)
        if retcode > 0:
            sys.exit(retcode)


if __name__ == "__main__":
    run_hooks()
