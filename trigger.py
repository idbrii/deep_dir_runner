#! /usr/bin/env python

"""
A trigger to determine when deepdirrunner should perform an action.
"""

import os

def dir_name_is_package_dir(path):
    """
    dir_name_is_package_dir(str) --> bool
    Returns true if the directory name is packages

    >>> dir_name_is_package_dir('packages')
    True
    >>> dir_name_is_package_dir('basekit')
    True
    >>> dir_name_is_package_dir('dime')
    False
    """
    dirname = os.path.basename(path)
    return dirname == 'packages' or dirname == 'basekit'


def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()

