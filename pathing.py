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
    
