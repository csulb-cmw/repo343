#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 cknapp <cknapp@mbp.local>
#
# Distributed under terms of the MIT license.

import os
import commit

"""

"""
def init(argv):
    cwd = os.getcwd()

    # create manifests folder
    if os.path.exists(cwd + "/repo343/manifests"):
        print( "Error: manifests directory exists." )
        exit()
    os.makedirs(cwd + "/repo343/manifests" )

    #do the first commit
    commit.commit( "initial", cwd + "/repo343/manifests", "none" )

def create_repo_directory( current_working_dir ):
    """Creates a new repo directory, or errors and exits if it exists already."
    :current_working_dir: The current working directory
    """

    if os.path.exists(current_working_dir + "/repo343"):
        print( "Error: repo exists." )
        exit()
    os.makedirs(current_working_dir + "/repo343")


