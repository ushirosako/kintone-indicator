#!/bin/bash

CURRENT_DIR=$(cd $(dirname $0) && pwd)
HOME_DIR=$(dirname $CURRENT_DIR)
LOGGING_DIR=${HOME_DIR}/libs

export PYTHONPATH=$LOGGING_DIR:$PYTHONPATH

cd $CURRENT_DIR
python main.py
