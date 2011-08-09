import os
import sys
import tacklebox
from shutil import copy
import stat


class TackleBox(object):

    hooks = [
        'applypatch-msg',
        'pre-applypatch',
        'post-applypatch',
        'pre-commit',
        'prepare-commit-msg',
        'commit-msg',
        'post-commit',
        'pre-rebase',
        'post-checkout',
        'post-merge',
        'pre-receive',
        'update',
        'post-receive',
        'post-update',
        'pre-auto-gc',
        'post-rewrite',
    ]

    def __init__(self):
        """
        Creates an instance of ``TackleBox`` and checks if the current
        working directory is part of a git repository.
        """
        GIT_DIR = os.environ.get('GIT_DIR', '.git')
        orig_path = os.path.realpath(os.getcwd())
        while True:
            path = os.path.realpath(os.getcwd())
            if os.path.isdir(os.path.join(path, GIT_DIR)):
                break
            os.chdir("..")
            if os.path.realpath(os.getcwd()) == '/':
                sys.stderr.write("%s is not a git repository.\n" % orig_path)
                sys.exit(1)
        self.hooks_dir = os.path.join(path, GIT_DIR, 'hooks')

    def create_hook(self, hook):
        """
        Copies the hook.py file from _tacklebox module and places it as the
        git hook file with execute permissions.
        """
        path = os.path.join(os.path.dirname(tacklebox.__file__), 'hook.py')
        hook_path = os.path.join(self.hooks_dir, hook)
        copy(path, hook_path)
        os.chmod(hook_path, stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR | stat.S_IROTH | stat.S_IRGRP)

    def create_hook_dirs(self, test_waters=False):
        """
        Iterates over the possible hooks and creates directories to house their
        scripts.
        """
        for hook in self.hooks:
            # Create the hook directory in the form _<hook>, e.g. _post-commit
            try:
                os.mkdir(os.path.join(self.hooks_dir, "_%s" % hook))
            except OSError:
                pass
            else:
                self.create_hook(hook)

    def test_waters(self):
        for hook in self.hooks:
            hook_exists = os.path.isfile(os.path.join(self.hooks_dir, hook))
            if hook_exists:
                sys.stderr.write("Found existing hook for %s, aborting.\n" % hook)
                sys.exit(1)

    def create(self):
        self.test_waters()
        self.create_hook_dirs()
        print "Initialized hook directories."
