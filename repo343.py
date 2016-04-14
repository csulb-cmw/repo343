#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 cknapp <cknapp@mbp.local>
#
# Distributed under terms of the MIT license.

import sys

help_string = """
usage: repo343 <command>

These are the supported commands used in various situations:
    init    initialize a new repo for the current working directory.
            Synonymies: create
"""

repo343_version = "0.0.1"

def main():
    """Program main function
    """
    if len(sys.argv) == 1:
        print_help()
        exit()
    if len(sys.argv) == 2:
        if sys.argv[1] == 'create' or sys.argv[1] == 'init':
            call_init()
        else if sys.argv[1] == 'commit':
            call_commit()
        else:
            print( "We don't understand command \""+sys.argv[1]+"\"" )
            print_help()

def print_help():
    """Prints the help info
    """
    print( help_string )
    
def call_init():
    """call the initialize repo script
    """
    import init
    init.init(sys.argv)
    
def call_commit():
    """process args for a commit message, and call it
    """
    import commit
    import pathing
    # process the args
    # did the user specify a commit message?
    if '-m' in sys.argv:
        # the commit message follows the -m TODO check for bounds because if
        # '-m' is the last arg, it's crash.
        commit_message = sys.argv[ sys.argv.index[ '-m'] + 1 ]
    else:
        commit_message = ""
    commit.commit(commit_message,
            get_manifest_directory(),
            get_last_commit_name_from_manifest()


main() # finally, call main
