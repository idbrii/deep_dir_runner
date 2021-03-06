#! /usr/bin/env python

"""
Walks a directory tree and performs an action when a trigger is hit.

Currently setup to build or clean ctags info from a packages or basekit folder.

Usage: %s path-to-root
Example: %s ~/code/someproject
"""

import sys

import deepdir
import action
import trigger
import filetype


def _usage():
    print __doc__


def main():
    import sys
    try:
        rootpath = sys.argv[1]
        if rootpath == '--help':
            raise ValueError()
    except (IndexError, ValueError):
        _usage()
        return

    runner = deepdir.DeepDirRunner(
        action.run_ctags_action
        , trigger.dir_name_is_package_dir
        , filetype.CPlusPlusFiletype()
    )
    runner.start_walking(rootpath)


if __name__ == '__main__':
    main()
