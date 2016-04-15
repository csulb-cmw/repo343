#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 cknapp <cknapp@mbp.local>
#
# Distributed under terms of the MIT license.
"""Commit
Performs tasks related to performing the `commit` command.
"""

import os
import shutil
from time import gmtime, strftime
import pathing

def commit(commit_message, project_root, repo_directory):
    """perform a repo commit

    :commit_message: human readable commit description.
    :manifest_dir_path: path to the repo manifest directory
    :previous_commit_id: id of the last commit

    """
    date_string = strftime("%Y-%m-%d_%H-%M-%S", gmtime())

    previous_commit_id = pathing.get_project_most_recent_commit_id(
            project_root, repo_directory)
    if not previous_commit_id:
        previous_commit_id = "initial"

    # create a file for writing the manifest data
    man_file_path = os.path.join(
            pathing.get_manifest_directory(repo_directory), date_string)
    man_file = open(man_file_path, 'w')


    # write any meta data
    man_file.write('date ' + date_string +'\n')
    man_file.write('previous_commit_id ' + previous_commit_id + '\n')
    man_file.write('=================================\n')
    man_file.write(commit_message + "\n")
    man_file.write('=================================\n')

    #the repo name is the same as the name of the directory containing it's root

    #for my friends who are new to python the underscore in the next line means
    #we're ignoring an unwanted return value.  splitext returns a name and an
    #extension, and we only care about the extension.
    _, repo_name = os.path.split(project_root)

    for subdir, _, files in os.walk(project_root):
        for project_file in files:
            path = os.path.join(subdir, project_file)
            if not ignore(path):
                process_file(man_file, path, project_root, repo_directory)

    # finally, record this as the most recent commit
    pathing.set_project_most_recent_commit_id(
            project_root, repo_directory, date_string)

def process_file(man_file, file_path, project_root, repo_directory):
    """Where the magic happens
    :man_file: Root to manifest file handle
    :file_path: path of the file to process
    :repo_directory_path: path to project root

    """

    repo_directory_path = pathing.convert_abs_file_path_into_abs_repo_file_path(
                file_path, project_root, repo_directory)
    # check if the leaf folder exists; create it if not
    if not os.path.exists(repo_directory_path):
        os.makedirs(repo_directory_path)
    check_sum = calculate_check_sum(file_path)
    # copy the file to the leaf folder
    copy_destination_path = os.path.join(repo_directory_path, str(check_sum))
    
    shutil.copyfile(file_path, copy_destination_path)

    #we don't want to record the absolute path to our copy, because it would
    #make it hard to move the project to a new directory or new computer.  I'm
    #not saying you CAN move a repo, but this isn't the reason you can't.
    #
    #So we need to get reduce something like this:
    #   /path/to/repo/PROJECT/text.txt
    #to something like:
    #   text.txt
    
    _, file_name = os.path.split(file_path)
    rp = pathing.convert_abs_repo_path_into_relative_repo_file_path(
            copy_destination_path, project_root)
    man_file.write(rp + '\t' + str(check_sum)+'\n')

def ignore(path):
    """ We don't have to implement the functionality to ignore paths yet, but
    as it turns out it's super useful for debugging when our python script is
    producing .pyc paths we don't want tracked, and OUR repo is in a git repo
    we don't want tracked.

    :path path of the path we're checking for ignorance.
    :returns true if it's to be ignored, false otherwise"""

    # Whatever the root of of you filesystem is, clearly that shouldn't be
    # ignored, even if it's a dumb idea to repo it.  Functionally, this is the
    # base case, for when we test if a parent directory should be ignored.
    # If a parent is ignored, it's children should be as well.
    if os.path.ismount(path):
        return False

    # make sure we're not backing up the repo
    # currently, it just ignores anything that has a parent directory that's
    # called 'repo343.' this isn't ideal
    path_remainder, path_component = os.path.split(path)
    if path_component == 'repo343':
        return True

    #ignore files that start with a '.', as a UNIX convention, and also because
    #sometimes other software drops .files without tell the user.
    if path_component[0] == '.':
        return True

    #ignore some file types we know we'll never want to back up
    _, extention = os.path.splitext(path)
    ignored_types = ['.pyc', '.o']
    if extention in ignored_types:
        return True

    #finally a file should be ignored if it's parent is ignored.
    return ignore(path_remainder)

def calculate_check_sum(file_path):
    """Calculate a file's check sum

    :file_path: the path to the file to be summed.
    """

    check_file = open(file_path, 'rb')
    check_sum = 1
    byte = check_file.read(1)
    while len(byte) > 0:
        check_sum += ord(byte)
        byte = check_file.read(1)
    return check_sum  % 256

