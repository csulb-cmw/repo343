#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 cknapp <cknapp@mbp.local>
#
# Distributed under terms of the MIT license.

import sys
import os
import shutil
import pathing
import string
"""

"""

def ask_user_repo_name(project_root, repo_directory):
    """ find active repos and ask user which one they would like
    :arg1: TODO
    :returns: TODO

    """

    man_file_path = pathing.get_manifest_directory(repo_directory)

    repo_name_list = []
    for _, _, files in os.walk(man_file_path):
        for f in files:
            if f.split('.')[-1] == 'most_recent_commit':
                repo_name_list.append(f.split('.')[0])
    id_menu_map = {}# we're gonna store what we print out so we can referance
                    # back 
    selection_options = '1234567890%s' % string.lowercase
    index = 0;
    for e in repo_name_list:
        selection_char = selection_options[index]
        id_menu_map[selection_char] = e
        print( "%c\t%s" % (selection_char, e))
        index = index+1

    #get index selection from user
    user_selection = raw_input(
            'enter the letter/number of the foreign repo: ').rstrip()
    #check to see if user selection is in range
    if user_selection in id_menu_map.keys():
        print id_menu_map[user_selection]
        return id_menu_map[user_selection]
    print 'invalid selection... canceling merge.'
    exit()

def ask_user_for_commit_id(project_id, repo_directory):
    """Display a all past repos and ask the user which one to use.
    :returns: User selection
    """
    
    #get the head of the repo_directory
    mrc_file_path = os.path.join(
            repo_directory, "repo343", "manifests", project_id + ".most_recent_commit")
    print(mrc_file_path)
    if os.path.exists(mrc_file_path ):
        mrc_file = open(mrc_file_path, 'r')
        most_recent = mrc_file.readline().rstrip()
    else:
        print(mrc_file_path+" is not a valid repo name")
        exit()
    print( most_recent );
    commit_id_list = pathing.create_history_list(repo_directory, most_recent)
    
    id_menu_map = {}# we're gonna store what we print out so we can referance
                    # back 

    selection_options = '1234567890%s' % string.lowercase
    index = 0;
    for e in commit_id_list:
        selection_char = selection_options[index]
        id_menu_map[selection_char] = e
        print( "%c\t%s" % (selection_char, e))
        index = index+1

    #get index selection from user
    user_selection = raw_input(
            'enter the letter/number of the commit: ').rstrip()
    
    #check to see if user selection is in range
    if user_selection in id_menu_map.keys():
        print id_menu_map[user_selection]
        return id_menu_map[user_selection]
    print 'invalid selection... canceling merge.'
    exit();

def merge_file(project_root,
        repo_directory,
        project_destination,
        repo_path,
        foreign_repo_name,
        foreign_merge_commit_id):
    """TODO: Docstring for merge_file.

    :arg1: TODO
    :returns: TODO

    """    


    #first, check if there is a conflict
    project_file_checksum = pathing.calculate_check_sum(project_destination)
    repo_file_checksum = pathing.calculate_check_sum(repo_path)

    if project_file_checksum == repo_file_checksum:
        print("no conflict")
        return
    print("conflict!!")

    #history for foreign
    f_merge_history = pathing.create_history_list(
            repo_directory, foreign_merge_commit_id)
    proj_merge_history = pathing.create_history_list(
            repo_directory,
            pathing.get_project_most_recent_commit_id(
                project_root, repo_directory))
    
    grandfather_id = pathing.find_youngest_grandfather(
        f_merge_history, proj_merge_history)

    # figure project_destination_tree_file_path [MT]
    project_destination_tree_file_path = pathing.append_string_to_file(
            project_destination, '_MT')
    # figure repo_destination_repo_path [MR]
    repo_destination_repo_path = pathing.append_string_to_file(
        project_destination, '_MR')
    # figure grandpa_destination_repo_path [MR]
    grandpa_destination_repo_path = pathing.append_string_to_file(
        project_destination, '_MG')

    # figure project_source_tree_file_path [MT]
    project_source_tree_file_path = project_destination

    #copy the repo to the MR path
    shutil.copyfile(
            repo_path,
            repo_destination_repo_path
            )

    #rename the MT file
    os.rename(project_source_tree_file_path, project_destination_tree_file_path)
 

    pass
