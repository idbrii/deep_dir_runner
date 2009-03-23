#! /usr/bin/env python

"""
Several different kinds of actions that can be performed by deepdirrunner.
"""

import os


def echo_path_action(fullpath, filetype=None):
    """
    echo_path_action(str, Filetype) --> None
    Launches some action on the given directory

    >>> someName = 'directory'
    >>> echo_path_action(someName, None)
    0
    """
    return os.system("echo "+ fullpath)


def remove_tags_file(fullpath, filetype=None):
    """
    remove_tags_file(str, Filetype) --> None
    Cleans the tags file from fullpath
    """
    tagsPath = os.path.join(fullpath, 'tags')
    return os.system("rm "+ tagsPath)


def run_ctags_action(fullpath, filetype):
    """
    run_ctags_action(str, Filetype) --> None
    Launches ctags for the filetype on the given directory
    """
    return os.system( 'cd '+ fullpath +'; '+ filetype.get_ctags_command() )



def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()

