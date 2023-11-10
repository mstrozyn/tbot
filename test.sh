#!/bin/bash

if [ -z "$1" ]
  then
    echo "No test suite name provided!"
    echo "Usage example: ./`basename "$0"` uboot"
  else
    newbot -k -c config.board tests.$1.all
fi
