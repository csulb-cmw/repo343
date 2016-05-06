#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 cknapp <cknapp@mbp.local>
#
# Distributed under terms of the MIT license.
import os

"""
Some loose functions related to getting the path to important repo documents
"""

def get_project_name(project_root):
    _, project_name = os.path.split( project_root )
    return project_name    

def get_manifest_directory(repo_directory):
    """ :returns: the path the manifest file
    """
    return os.path.join( repo_directory, "repo343", "manifests" )

def get_project_most_recent_commit_id(project_root, repo_directory):
    """ The most recent commit is stored in the manifests folder in a file
    called "most_recent_commit".  The file should always have exactly one line,
    which is the id of the most recent commit, if it exists at all.  This
    function get's that value.
    
    :returns: the most recent commit id, or nothing if it doesn't exist.
    """
    mrc_file_name = get_project_name(project_root) + ".most_recent_commit"
    mrc_file_path = os.path.join(
            get_manifest_directory(repo_directory), mrc_file_name)
    if os.path.exists(mrc_file_path):
        mrc_file = open(mrc_file_path, 'r')
        return mrc_file.readline()
    # return nothing TODO what's the pythonic nothing/null?

def set_project_most_recent_commit_id(project_root, repo_directory, commit_id):
    """ The most recent commit is stored in the manifests folder in a file
    called "most_recent_commit".  The file should always have exactly one line,
    which is the id of the most recent commit, if it exists at all.  This
    function sets that value.

    :commit_id: This will be written as the new most recent commit id
    """
    mrc_file_name = get_project_name(project_root) + ".most_recent_commit"
    mrc_file_path = os.path.join(
            get_manifest_directory(repo_directory), mrc_file_name)

    mrc_file = open(mrc_file_path, 'w')
    mrc_file.write(commit_id)
    # return nothing TODO what's the pythonic nothing/null? 

def convert_abs_file_path_into_abs_repo_file_path(
        abs_file_path, project_root, repo_directory):
    relative_file_path = abs_file_path[len(project_root)+1:]
    return os.path.join(
            repo_directory,
            'repo343',
            get_project_name(project_root),
            relative_file_path )

def convert_abs_repo_path_into_relative_repo_file_path(
        abs_repo_path, project_root):
    return abs_repo_path[len(project_root)+9:] # len("/repo343/") == 6
    
def append_string_to_file(path, suffix):
    """appendes a string to the file name in a path, leaving file extension
    intact

    :path: TODO
    :suffix: TODO
    :returns: TODO

    """
    head, filename = os.path.split(path)
    split_filename = filename.split('.')
    #TODO this bugs when a file name contains anything other then exactly one '.'
    return os.path.join(head, split_filename[0]+suffix+'.'+split_filename[1])


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

def read_manifest_file(man_file):
    """TODO: Docstring for parse_header.

    :man_file: TODO
    :returns: TODO

    """
    #process_file
    meta_dictionary = {}
    line = man_file.readline().rstrip()
    while line != '=================================':
        split_line = line.split(' ')
        meta_dictionary[ split_line[0] ] = split_line[1]
        line = man_file.readline().rstrip()
    # now read the comment which might be multi_line
    #TODO read the comment file
    line = man_file.readline().rstrip()
    while line != '=================================':
        # read file path, hash pairs
        line = man_file.readline().rstrip()
    
    # read file association list
    file_association_list = []
    line = man_file.readline().rstrip()
    while len(line) != 0:
        file_association_list.append(line)
        line = man_file.readline().rstrip()
    
    meta_dictionary['file_association_list'] = file_association_list
    return meta_dictionary

def create_history_list(repo_directory, commit_id):
    """Creates a complete linear history for a commit id 
    :repo_directory: The repository base folder
    """
    history_list = []
    commit_id

    while commit_id != "initial":
        history_list.append(commit_id)
        man_file = os.path.join(
                get_manifest_directory(repo_directory), commit_id)
        man_file_data = read_manifest_file( file(man_file) )
        commit_id = man_file_data['previous_commit_id']
    return history_list

def find_youngest_grandfather(hist1, hist2):
    common = set(hist1).intersection(set(hist2))
    if len(common) > 0:
        return sorted(common)[0]
    return None


