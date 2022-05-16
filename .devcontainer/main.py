#!/usr/bin/env python3
"""
Daemon that watches for new files, processes them and commits them to the
specified git repositories as new Hugo posts.
"""

import glob
import re
import os
import sys
import yaml


def read_config(configfile='config.yml'):
    """
    Read configuration and return config object
    """
    with open(configfile, encoding="utf-8") as file:
        _config = yaml.load(file, Loader=yaml.FullLoader)
        return _config


def create_dir(directory):
    """
    Create directory or raise an exception
    """
    try:
        os.mkdir(directory)
    except IOError as exc:
        raise RuntimeError('Failed to create directory') from exc


def preflight_check(configobj):
    """
    "Preflight check" when we start the script. Making sure that the file and
    folder structure is present and we are good to go
    """
    _basedir = configobj['basedir']
    _pubdir = configobj['pubdir']
    _blogs = configobj['blogs']

    for directory in _basedir, _pubdir:
        create_dir(directory)

    for _blog in _blogs:
        _fullpath = os.path.join(_basedir, _blog)
        create_dir(_fullpath)


def analyse_post():
    """
    Analyse the Markdown text file and return metadata, title, tags and content
    """
    print('fixme')


def main():
    """
    Go time! Let's rock
    """
    print("I'm running!")


if __name__ == '__main__':
    config = read_config()
    preflight_check(config)
    main()
