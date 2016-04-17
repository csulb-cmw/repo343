# repo343
Part one of the CECS-343 VCS project.

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
