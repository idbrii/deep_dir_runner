#! /usr/bin/env python

import os

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

