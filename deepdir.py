#! /usr/bin/env python

import re
import os


def isCodeTypeFile(filename):
    """
    isCodeTypeFile(str) --> bool
    Returns whether the provided filename should have tags generated for it

    >>> isCodeTypeFile("main.cpp")
    True
    >>> isCodeTypeFile("extension.h")
    True
    >>> # We're not interested in generating tags for python
    >>> isCodeTypeFile("cppreader.py")
    False
    """
    return None is not re.search("\.cpp|\.h", filename)


def echoPathAction(fullpath):
    """
    action(str) --> None
    Launches some action on the given directory

    >>> someName = 'directory'
    >>> echoPathAction(someName)
    0
    """
    return os.system("echo "+ fullpath)


def dirNameIsPackageDir(path):
    """
    dirNameIsPackageDir(str) --> bool
    Returns true if the directory name is packages

    >>> dirNameIsPackageDir('packages')
    True
    >>> dirNameIsPackageDir('basekit')
    True
    >>> dirNameIsPackageDir('dime')
    False
    """
    dirname = os.path.basename(path)
    return dirname == 'packages' or dirname == 'basekit'


class DeepDirRunner(object):
    """
    Walks a directory to run an action on directories
    """

    def __init__(self, action, trigger):
        """
        Constructor.

        action -- a function that performs the action
        trigger -- a function that checks if we're ready to do the action
        """
        assert action is not None
        assert trigger is not None
        self._do_action = action
        self._should_trigger_action = trigger
        self.paths = []


    def start_walking(self, rootpath):
        """
        start_walking(DeepDirRunner, str) --> None
        Begin walking the directory, checking for triggers, and running actions.
        """
        self._walk(rootpath)

        print 'Ran the action on these paths:',
        for p in self.paths:
            print p,
        print


    def _walk(self, rootpath):
        """ Internal version of start_walking() """
        for dirpath, dirnames, filenames in os.walk(rootpath):
            if self._should_trigger_action(dirpath):
                print '!!!!!!!!!! trigger !!!!!!!!!!'
                self._do_action(dirpath)
                self.paths.append(dirpath)
                del dirnames    # don't go any further

            else:
                for filename in filenames:
                    if isCodeTypeFile(filename):
                        print "Found a code file that we're" \
                                +" not running action on: %s" % filename


def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()

