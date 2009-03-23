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
    except IndexError:
        _usage()
        return

    runner = deepdir.DeepDirRunner(
        deepdir.run_ctags_action
        , deepdir.dir_name_is_package_dir
        , deepdir.CPlusPlusFiletype()
    )
    runner.start_walking(rootpath)


if __name__ == '__main__':
    main()
