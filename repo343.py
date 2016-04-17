#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 cknapp <cknapp@mbp.local>
#
# Distributed under terms of the MIT license.

import sys
import os

help_string = """
usage: repo343 <command>

These are the supported commands used in various situations:
    init    initialize a new repo for the current working directory.
            Synonymies: create
"""

repo343_version = "0.0.1"

# program globals

def main():
    """Program main function
    """
    # some parameters are going to be program wide
    project_root = os.path.abspath(get_argv_option('-p'))
    repo_directory = os.path.abspath(get_argv_option('-r'))
    
    print project_root
    print repo_directory

    if 'create' in sys.argv or 'init' in sys.argv:
        call_init(project_root, repo_directory)
    elif 'commit' in sys.argv:
        call_commit(project_root, repo_directory)
    elif 'checkout' in sys.argv:
        call_checkout(project_root, repo_directory)
    else:
        print( 'no command found' )
        print_help()

def get_argv_option( option_prefix ):
    """Returns the argument that follows the supplied prefix in the argv"""
    try:
        index =  sys.argv.index(option_prefix) + 1 
    except Exception as e:
        return #not found   
    if index < len(sys.argv):
        return sys.argv[index]
    return #nothing

def print_help():
    """Prints the help info
    """
    print( help_string )
    
def call_init(project_root, repo_directory):
    """call the initialize repo script
    """
    import init
    init.init(project_root, repo_directory)
    
def call_commit(project_root, repo_directory):
    """process args for a commit message, and call it
    """
    import commit
    import pathing
    # process the args
    # did the user specify a commit message?
    commit_message = get_argv_option( '-m' )
    if not commit_message:
        commit_message = ""
    commit.commit(commit_message, project_root, repo_directory)

def call_checkout(project_root, repo_directory):
    import checkout
    checkout.checkout(project_root, repo_directory)

main() # finally, call explicitly main
