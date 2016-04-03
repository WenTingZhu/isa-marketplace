#!/bin/bash

# this file will clean up your local repo by
# 1) removing all  migrations
# 2) removing all cache
# 3) removing all .pyc files

# usage (from isa-marketplace/ directory):        bash clean.sh
# may require you to enter in your password


find ./ -name __pycache__ | awk '{print "sudo rm -rf "$1}' | sh

find ./ -name migrations | awk '{print "sudo rm -rf "$1}' | sh

find ./ -name *.pyc | awk '{print "sudo rm -rf "$1}' | sh
