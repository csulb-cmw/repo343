#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 cknapp <cknapp@mbp.local>
#
# Distributed under terms of the MIT license.
import os
import shutil
from time import gmtime, strftime

"""

"""

def commit(commit_code, manifest_dir_path, previous_manifest_id):
    """perform a repo commit

    :commit_code: human readable commit description.
    :manifest_dir_path: path to the repo manifest directory
    :previous_manifest_id: id of the last commit

    """
    date_string = strftime("%Y-%m-%d_%H:%M:%S", gmtime())

    # create a file for writing the manifest data
    man_file = open(manifest_dir_path+"/"+date_string, 'w')
    
    # write any meta data
    man_file.write('date ' + date_string +'\"')
    man_file.write('previous_manifest_id ' + previous_manifest_id + '\n')
    man_file.write('=================================\n')
    man_file.write(commit_code + "\n")
    man_file.write('=================================\n')
    cwd = os.getcwd()
    repo_name = cwd.split('/')[-1]
    for subdir, dirs, files in os.walk( os.getcwd() ):
        for file in files:
            path = os.path.join(subdir, file)
            handle_path( repo_name, get_repo_root(), man_file, path )


    pass

def get_repo_root():
    """ :returns: The repo root for the cwd.
    """
    return os.getcwd(); # TODO add search for root if we're in a sub directory

def handle_path( repo_name, repo_root, man_file, path ):
    """Checks if the repo is responsible for this file, and commits it if so.

    :repo_name: Repo name
    :repo_root: Root of project directory
    :man_file: Root to manifest file handle
    :path: path of the file to process

    """
    relative_path = path[1+len(repo_root):]
    if ignore( path, repo_root+"/repo343/" ):
        return

    process_file( repo_root, man_file, path, repo_root+"/repo343/"+repo_name+"/"+relative_path )

def process_file( repo_root, man_file, file_path, repo_directory_path ):
    """Where the magic happens 

    :repo_root: Root of project directory
    :man_file: Root to manifest file handle
    :file_path: path of the file to process
    :repo_directory_path: path to project root

    """

    # check if the leaf folder exists; create it if not
    if not os.path.exists(repo_directory_path):
        os.makedirs( repo_directory_path )

    check_sum = calculate_check_sum( file_path )
    # copy the file to the leaf folder
    shutil.copyfile( file_path, repo_directory_path+"/"+str(check_sum) )

    relative_path = file_path[1+len(repo_root):]    
    man_file.write( relative_path + "\t" + str(check_sum)+"\n" )
    

def ignore( path, repo_directory_path ):
    """ We don't have to implement the functionality to ignore paths yet, but
    as it turns out it's super useful for debugging when our python script is
    producing .pyc paths we don't want tracked, and OUR repo is in a git repo
    we don't want tracked.

    :path path of the path we're checking for ignorance.
    :returns true if it's to be ignored, false otherwise"""

    # make sure we're not backing up the repo
    split_path = path.split( '/' )
    if repo_directory_path == path[0:len(repo_directory_path)]:
        return True

    dot_split = path.split( '.' )
    if split_path[-1][0] == '.':
        return True
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
