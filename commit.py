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
    man_file_path = os.path.join(manifest_dir_path, date_string)
    man_file = open(man_file_path, 'w')

    # write any meta data
    man_file.write('date ' + date_string +'\"')
    man_file.write('previous_manifest_id ' + previous_manifest_id + '\n')
    man_file.write('=================================\n')
    man_file.write(commit_code + "\n")
    man_file.write('=================================\n')

    project_root = get_project_root()
    #the repo name is the same as the name of the directory containing it's root
    _, repo_name = os.path.split(project_root)

    for subdir, dirs, files in os.walk(project_root):
        for file in files:
            path = os.path.join(subdir, file)
            if not ignore(path):
                process_file(
                        project_root, man_file, path,
                        os.path.join(
                            project_root,"repo343",repo_name, file) )

    pass

def get_project_root():
    """ :returns: The repo root for the cwd.
    """
    return os.getcwd(); # TODO add search for root if we're in a sub directory

def process_file( project_root, man_file, file_path, repo_directory_path ):
    """Where the magic happens 

    :project_root: Root of project directory
    :man_file: Root to manifest file handle
    :file_path: path of the file to process
    :repo_directory_path: path to project root

    """

    # check if the leaf folder exists; create it if not
    if not os.path.exists(repo_directory_path):
        os.makedirs( repo_directory_path )

    check_sum = calculate_check_sum( file_path )
    # copy the file to the leaf folder
    copy_destination_path = os.path.join(repo_directory_path, str(check_sum))
    shutil.copyfile(file_path, copy_destination_path)

    #we don't want to record the absolute path to our copy, because it would
    #make it hard to move the project to a new directory or new computer.  I'm
    #not saying you CAN move a repo, but this isn't the reason you can't.
    #
    #So we need to get reduce something like this:
    #   /path/to/repo/PROJECT/text.txt  <== 
    #to something like:
    #   text.txt
    #Warning: the below only works for flat directories 
    _, file_name = os.path.split( file_path )
    man_file.write(file_name + '\t' + str(check_sum)+'\n')

def ignore(path):
    """ We don't have to implement the functionality to ignore paths yet, but
    as it turns out it's super useful for debugging when our python script is
    producing .pyc paths we don't want tracked, and OUR repo is in a git repo
    we don't want tracked.

    :path path of the path we're checking for ignorance.
    :returns true if it's to be ignored, false otherwise"""

    # make sure we're not backing up the repo
    # currently, it just ignores anything that has a parent directory that's
    # called 'repo343.' this isn't ideal 
    path_remander, path_component = os.path.split(path)
    while path_component:
        print path_component + '    ' + path_remander
        if path_component == 'repo343':
            return True
        path_remander, path_component = os.path.split(path_remander)

    #ignore files that start with a '.', as a UNIX convention, and also because
    #sometimes other software drops .files without tell the user.
    path_remander, path_component = os.path.split(path)
    if path_component[0] == '.':
        return True

    #ignore some file types we know we'll never want to back up
    #for my friends who are new to python the underscore in the next line means
    #we're ignoring an unwanted return value.  splitext returns a name and an
    #extension, and we only care about the extension.
    _, extention = os.path.splitext(path)
    ignored_types = ['pyc', 'o']
    if extention in ignored_types:
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
