#!/bin/bash
base=`dirname $0`
export PATH=$PATH:/usr/local/bin
default_target=
if [ -z "$*" ]
    then
      default_target=atests
fi
pybot -c regression -L debug --variablefile "$base/osx_vars.py" --pythonpath "$base/src/" $default_target "$@"
