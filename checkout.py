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

import merge

def checkout(project_root,
        repo_directory,
        merge_commit_id = False,
        foreign_repo_name = False):
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
        meta_dictionary = pathing.read_manifest_file(man_file)
    else:
        # TODO handle this more gracefully.
        print( "Error: couldn't find project \"%\" in repo." % project_id )
        exit(-1)
    copy_files(
            project_root,
            repo_directory,
            meta_dictionary['file_association_list'],
            foreign_repo_name,
            merge_commit_id)

def copy_files(project_root,
        repo_directory,
        file_association_list,
        foreign_repo_name = False,
        foreign_merge_commit_id = False):
    project_path_one_down, _ = os.path.split(project_root)
    for association in file_association_list:
        relative_path, repo_hash = os.path.split(association)
        copy_path = os.path.join(project_path_one_down, relative_path)
        original_path = os.path.join(
                os.path.join(repo_directory, "repo343"), association)
        copy_path_one_down, _ = os.path.split(copy_path)
        if not os.path.exists(copy_path_one_down):
            os.makedirs(copy_path_one_down)
        if( os.path.exists(copy_path)):
            # this file already exists, so revert to merge behavior if allowed
            if( foreign_merge_commit_id != False ):
                merge.merge_file(
                        project_root,
                        repo_directory,
                        copy_path,
                        original_path,
                        foreign_repo_name,
                        foreign_merge_commit_id)
        else:
            shutil.copyfile(original_path, copy_path)
        

