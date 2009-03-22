import deepdir


def _usage():
    print \
"""
    Usage: %s path-to-root
    Example: %s ~/code/someproject
"""


def main():
    import sys
    try:
        rootpath = sys.argv[1]
    except:
        _usage()
        return

    runner = deepdir.DeepDirRunner(deepdir.echoPathAction, deepdir.dirNameIsPackageDir)
    runner.start_walking(rootpath)


if __name__ == '__main__':
    main()
