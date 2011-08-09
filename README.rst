Git TackleBox
=============

Git only calls one script if it is named the same as the hook.  This tool allows
you to run multiple scripts in a plug and play fashion by creating an
executable that iterates over scripts within a directory, passing along
command line arguments to each script.

Usage::

    $ mkdir repo && cd repo
    $ git init
    Initialized empty Git repository in /path/to/repo/.git/
    $ tacklebox init
    Initialized hook directories.
    $ cd .git/hooks && rm *.sample
    $ ls -1
    _applypatch-msg
    applypatch-msg
    _commit-msg
    commit-msg
    _post-applypatch
    post-applypatch
    _post-checkout
    post-checkout
    _post-commit
    post-commit
    _post-merge
    post-merge
    _post-receive
    post-receive
    _post-rewrite
    post-rewrite
    _post-update
    post-update
    _pre-applypatch
    pre-applypatch
    _pre-auto-gc
    pre-auto-gc
    _pre-commit
    pre-commit
    _prepare-commit-msg
    prepare-commit-msg
    _pre-rebase
    pre-rebase
    _pre-receive
    pre-receive
    update
    _update

As you can see, there is a script for the hook and a directory that contains
any scripts you wish to run for that hook event.

TODO:

    * Write tests


