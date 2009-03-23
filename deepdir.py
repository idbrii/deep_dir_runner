#! /usr/bin/env python

import re
import os


##########
## Actions

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


##########
## Triggers

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


##########
## Filetypes

class CPlusPlusFiletype(object):
    """
    This class represents the C/C++ filetype
    """

    def __init__(self):
        """
        Constructor. Init file extension array and regex
        """
        self.__extensions = ['c', 'cpp', 'h']
        self.__extensionRE = self._compile_extension_regex()


    def _compile_extension_regex(self):
        """
        _compile_extension_regex(self) --> SRE_object
        Creates the compiled RE for C/C++ filetype
        """
        # search for any file ending in extensions
        reExpression = reduce( lambda x,y: x +'$|'+ y, self.__extensions )
        reExpression += '$'

        return re.compile(reExpression)


    def is_file_my_type(self, filename):
        """
        is_file_my_type(self, str) --> bool
        Checks if the input file is for c++

        >>> ft = CPlusPlusFiletype()
        >>> ft.is_file_my_type("main.cpp")
        True
        >>> ft.is_file_my_type("extension.h")
        True
        >>> # We're not interested in generating tags for python
        >>> ft.is_file_my_type("cppreader.py")
        False
        """
        return None is not self.__extensionRE.search(filename)


    def get_ctags_command(self):
        """
        get_ctags_command(self) --> str
        Returns the ctags command for building a tag file for this filetype.
        """
        return 'ctags --languages=c,c++ -R .'



##########
## Main Class

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
                    if self.__filetype.is_file_my_type(filename):
                        print "Found a code file that we're" \
                                +" not running action on: %s" % filename


def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()

