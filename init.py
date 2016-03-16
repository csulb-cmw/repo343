#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 cknapp <cknapp@mbp.local>
#
# Distributed under terms of the MIT license.

import os
import shutil
"""

"""
def init(argv):
    cwd = os.getcwd( )
    create_repo_directory( cwd )
    for subdir, dirs, files in os.walk( os.getcwd() ):
        for file in files:
            path = os.path.join(subdir, file)
            handle_path( cwd, path )


def create_repo_directory( current_working_dir ):
    """Creates a new repo directory, or errors and exits if it exists already."
    :current_working_dir: The current working directory
    """

    if os.path.exists(current_working_dir + "/repo343"):
        print( "Error: repo exists." )
        exit()
    os.makedirs(current_working_dir + "/repo343")


def handle_path( current_working_dir, path ):
    """TODO: Docstring for handle_path.

    :current_working_dir: TODO
    :path: TODO
    :returns: TODO
    """

    relative_path = path[1+len(current_working_dir):]
    if( ignore( path ) ):
        return
    process_file( path, current_working_dir+"/repo343/"+relative_path )

def process_file( file_path, repo_directory_path ):
    """Where the magic happens 

    :file_path: TODO
    :repo_directory_path: TODO
    :returns: TODO

    """
    # check if the leaf folder exists; create it if not
    if not os.path.exists(repo_directory_path):
        os.makedirs( repo_directory_path )

    check_sum = calculate_check_sum( file_path )
    # copy the file to the leaf folder
    shutil.copyfile( file_path, repo_directory_path+"/"+str(check_sum) )
    

def ignore( path ):
    """ We don't have to implement the functionality to ignore paths yet, but
    as it turns out it's super useful for debugging when our python script is
    producing .pyc paths we don't want tracked, and OUR repo is in a git repo
    we don't want tracked.

    :path path of the path we're checking for ignorance.
    :returns true if it's to be ignored, false otherwise"""

    if path[0] == '.':
        return True
    dot_split = path.split( '.' )
    if( dot_split[-1] == "pyc" ):
        return True
    return False

def calculate_check_sum( filename ):
    file = open(filename, 'rb')
    sum = 1
    byte = file.read(1)
    while len(byte) > 0:
        sum += ord(byte)        
        byte = file.read(1)
    return sum % 256
