# repo343
Part two of the CECS-343 VCS project.

# team CMW
* Cory Knapp (knapp.cory@gmail.com) [Team lead]
* Mukesh Sehdev (sehdev.mukesh@yahoo.com)
* William Perez (billyreaper@yahoo.com)

# introduction
This is part two of our version control system, which implements the create,
commit, and checkout functions

# Usage instructions
## External Requirements
This program requires a python instalation to run.  Further, these
instructions assume a unix-like environment.

## Installation and Setup
This doesn't need installed in any particular location.  Additionally,
this software can be installed by using the git `clone` command with the
URL `https://github.com/csulb-cmw/repo343` as the first argument.

## Usage
### create function
The create repo command can be invoked using
`python \path\to\script\directory\repo343 create` or 
`python \path\to\script\directory\repo343 init`
The command requires two parameters: the path to the directory that's to be
stored in the repository, and a path to the repository folder, denoted by 
prefix arguments `-p` and `-r` respectivly.  For example:
`repo343 init -p project/path -r repo/path`.

### commit function
The create repo command can be invoked using
`python \path\to\script\repo343 commit` 
The command requires two parameters: the path to the directory that's to be
commited in the repository, and a path to the repository folder, denoted by 
prefix arguments `-p` and `-r` respectivly.  For example:
`repo343 commit -p project/path -r repo/path`.  Note that differant repositories
must have unique names, and coalitions will result in projects being merged.

### checkout function
The create repo command can be invoked using
`python \path\to\script\repo343 checkout` 
The command requires two parameters: the path to a directory which is to become
the new root of the project branch, and a path to the repository folder, denoted by 
prefix arguments `-p` and `-r` respectivly.  For example:
`repo343 checkout -p project/path -r repo/path`.  The name of the top directory
needs to match the name of an existing repository.  In the previous example,
the command would check out an existing project called `path` from the
repository located at `repo/path`.

### merge function
Merge one repository into another
`python \path\to\script\repo343 merge` 
The command requires two parameters: the path to a directory which is to become
the new root of the project branch, and a path to the repository folder, denoted by 
prefix arguments `-p` and `-r` respectivly.

When the merge function is run, the user is presented with a list of projects
that are being stored in the repository directory supplied by the `-r` option.
If the user enters anything other then the supplied options, the merge is
canceled.  The user is then shown a list of commits assosated with that brance.
When a selection is made, the files from the foreign repo will be copied into
the project when no conflicts accure, and when they do accure it's copy files
with modiffied file names, `_MT` being appended to the exisiting file, `_MR`
being appened to the repository version, and `_MG` to the most recent common
ancestor file, if they share a common ancestor.
