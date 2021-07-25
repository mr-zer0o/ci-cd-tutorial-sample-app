#PYENV_HOME=$WORKSPACE/.sample1/
#if [ –d $PYENV_HOME ]; then
#   rm –rf $PYENV_HOME
#fi
#
#virtualenv —no–site–packages $PYENV_HOME
#. $PYENV_HOME/bin/activate
#pip install –r envs/req.txt



#!/bin/bash
PYENV_HOME=$WORKSPACE/venv/
rm –rf $PYENV_HOME
if [ –d $PYENV_HOME ]; then
   rm –rf $PYENV_HOME
fi

export WORKSPACE=`pwd`
# Create/Activate virtualenv
virtualenv venv
. $WORKSPACE/venv/bin/activate
# Install Requirements
pip install -r requirements.txt
# Run tests
python manage.py test