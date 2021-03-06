#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 cknapp <cknapp@mbp.local>
#
# Distributed under terms of the MIT license.

import os
import commit
import pathing

"""

"""
def init(project_root, repo_directory):
    """perform a repo initialization
    """

    # create manifests folder
    partial_path_to_manifest = pathing.get_manifest_directory(repo_directory)

    if not os.path.exists(partial_path_to_manifest):
        os.makedirs(partial_path_to_manifest)

    #do the first commit
    commit.commit("initial" ,project_root, repo_directory)

def create_repo_directory( current_working_dir ):
    """Creates a new repo directory, or errors and exits if it exists already."
    :current_working_dir: The current working directory
    """

    if os.path.exists(os.path.join(current_working_dir, "repo343")):
        print( "Error: repo exists." )
        exit()
    os.makedirs(os.path.join(current_working_dir, "repo343"))
