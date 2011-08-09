import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "git-tacklebox",
    version = "0.0.1",
    description = "A tool to setup a git repo to be able to execute multi scripts for a single git hook.",
    long_description = read('README.rst'),
    url = 'http://github.com/sebleier/git-tacklebox',
    license = 'BSD',
    author = 'Sean Bleier',
    author_email = 'sebleier@gmail.com',
    packages = ['tacklebox'],
    entry_points = {
        'console_scripts': ['tacklebox = tacklebox.launcher:main']
    }
)
