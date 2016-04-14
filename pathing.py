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

def get_project_root():
    """ :returns: The repo root for the cwd.
    """
    return os.getcwd() # TODO add search for root if we're in a sub directory

def get_manifest_directory();
    """ :returns: the path the manifest file
    """
    return os.path.join( get_project_root(), "repo434", "manifests" )

def get_project_most_recent_commit_id():
    """ The most recent commit is stored in the manifests folder in a file
    called "most_recent_commit".  The file should always have exactly one line,
    which is the id of the most recent commit, if it exists at all.  This
    function get's that value.
    
    :returns: the most recent commit id, or nothing if it doesn't exist.
    """
    mrc_file_path = os.path.join(get_manifest_directory(), "most_recent_commit")
    if os.path.exists(mrc_file_path):
        mrc_file = open(mrc_file_path, 'r')
        return mrc_file.readline()
    # return nothing TODO what's the pythonic nothing/null? 

def set_project_most_recent_commit_id(commit_id):
    """ The most recent commit is stored in the manifests folder in a file
    called "most_recent_commit".  The file should always have exactly one line,
    which is the id of the most recent commit, if it exists at all.  This
    function sets that value.

    :commit_id: This will be written as the new most recent commit id
    """
    mrc_file_path = os.path.join(get_manifest_directory(), "most_recent_commit")
    mrc_file = open(mrc_file_path, 'w')
    mrc_file.write(commit_id)
    # return nothing TODO what's the pythonic nothing/null? 
