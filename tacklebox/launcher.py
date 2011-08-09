import sys
from tacklebox import TackleBox


def main():
    # Todo: add more robust option parsing
    if sys.argv[1] == 'init':
        tacklebox = TackleBox()
        tacklebox.create()
    else:
        sys.stderr.write("%s is not a valid option.\n" % sys.argv[1])
        sys.exit(1)
