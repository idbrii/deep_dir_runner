#! /usr/bin/env python

"""
Different filetypes that provide functionality to check filenames for
type match and to get the ctags command to build a tag file for that
language.
"""

import re


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



def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()

