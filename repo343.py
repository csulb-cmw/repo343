#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 cknapp <cknapp@mbp.local>
#
# Distributed under terms of the MIT license.

import sys

"""

"""

def main():
    """Program main function
    """
    if len(sys.argv) == 1:
        print_help()
        exit()
    if len(sys.argv) == 2:
        if sys.argv[1] == "create" or sys.argv[1] == "init":
            call_init()
        else:
            print( "We don't understand command \""+sys.argv[1]+"\"" )
            print_help()

def print_help():
    """Prints the help info
    """
    print( "Help info." ) # TODO add help/man info

def call_init():
    import init
    init.init(sys.argv)
    

main() # finally, call main
