# repo343
Part one of the CECS-343 VCS project.

# team CMW
* Cory Knapp (knapp.cory@gmail.com) [Team lead]
* Mukesh Sehdev (sehdev.mukesh@yahoo.com)
* William Perez (billyreaper@yahoo.com)

# introduction
This is part one our version control system, which only implements the
create repo command, which functions under only certain conditions.

# Usage instructions
## External Requirements
This program requires a python instalation to run.  Further, these
instructions assume a unix-like environment.

## Installation and Setup
This doesn't need installed in any particular location.  Additionally,
this software can be installed by using the git `clone` command with the
URL `https://github.com/csulb-cmw/repo343` as the first argument.

## Usage
The create repo command can be invoked using
`python \path\to\script\directory\repo343 create` or 
`python \path\to\script\directory\repo343 init`
and should be invoked while in the root directory of the project to be
commited to the new repo.  If permission to execute the file is given via
the `chmod +x \path\to\script\directory\repo343` then they python portion
of the previous commands can be ommited.
