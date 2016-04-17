#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 cknapp <cknapp@mbp.local>
#
# Distributed under terms of the MIT license.

"""

"""

import pathing
import os
import shutil

def checkout(project_root, repo_directory):
    """TODO: Docstring for checkout.

    :project_root: TODO
    :repo_directory: TODO
    :returns: TODO

    """
    
    #defaults to checking out the most recent
    project_id = pathing.get_project_most_recent_commit_id(
            project_root, repo_directory)
    
    man_file_path = os.path.join(
            pathing.get_manifest_directory(repo_directory),
            project_id)
    if os.path.exists(man_file_path):
        man_file = open(man_file_path, 'r')
        meta_dictionary = process_manifest_file(man_file)
    else:
        # TODO handle this more gracefully.
        print( "Error: couldn't find project \"%\" in repo." % project_id )
        exit(-1)
    copy_files(
            project_root, repo_directory, meta_dictionary['file_association_list'])

def process_manifest_file(man_file):
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

def copy_files(project_root, repo_directory, file_association_list):
    project_path_one_down, _ = os.path.split(project_root)
    for association in file_association_list:
        relative_path, repo_hash = os.path.split(association)
        copy_path = os.path.join(project_path_one_down, relative_path)
        original_path = os.path.join(
                os.path.join(repo_directory, "repo343"), association)
        copy_path_one_down, _ = os.path.split(copy_path)
        if not os.path.exists(copy_path_one_down):
            os.makedirs(copy_path_one_down)
        shutil.copyfile(original_path, copy_path)
        
