#! /usr/bin/env python

import re
import os


def echoPathAction(fullpath, filetype):
    """
    action(str) --> None
    Launches some action on the given directory

    >>> someName = 'directory'
    >>> echoPathAction(someName, None)
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


class CPlusPlusFiletype(object):
    """
    This class represents the C/C++ filetype
    """

    def __init__(self):
        """
        Constructor.
        """
        self.__extensions = ['c', 'cpp', 'h']
        self.__extensionRE = self._compileExtensionRE()

    def _compileExtensionRE(self):
        """
        _compileExtensionRE(self) --> SRE_object
        Creates the compiled RE for C/C++ filetype
        """
        # search for any file ending in extensions
        reExpression = reduce( lambda x,y: x +'$|'+ y, self.__extensions )
        reExpression += '$'

        return re.compile(reExpression)

    def isFileMyType(self, filename):
        """
        isFileMyType(self, str) --> bool
        Checks if the input file is for c++

        >>> ft = CPlusPlusFiletype()
        >>> ft.isFileMyType("main.cpp")
        True
        >>> ft.isFileMyType("extension.h")
        True
        >>> # We're not interested in generating tags for python
        >>> ft.isFileMyType("cppreader.py")
        False
        """
        return None is not self.__extensionRE.search(filename)


    def ctagsCommand(self):
        """
        ctagsCommand(self) --> str
        Returns the ctags command for building a tag file for this filetype.
        """
        return 'ctags --languages=c,c++ -R .'



class DeepDirRunner(object):
    """
    Walks a directory to run an action on directories
    """

    def __init__(self, action, trigger, filetype):
        """
        Constructor.

        action -- a function that performs the action
        trigger -- a function that checks if we're ready to do the action
        """
        assert action is not None
        assert trigger is not None
        assert filetype is not None
        self._do_action = action
        self._should_trigger_action = trigger
        self.__filetype = filetype
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
                self._do_action(dirpath, self.__filetype)
                self.paths.append(dirpath)
                del dirnames    # don't go any further

            else:
                for filename in filenames:
                    if self.__filetype.isFileMyType(filename):
                        print "Found a code file that we're" \
                                +" not running action on: %s" % filename


def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()

