#!/bin/bash

# Uninstall all Python versions
sudo rm -rf /Library/Frameworks/Python.framework/Versions/*

sudo rm -rf /Applications/Python*

sudo rm -rf /usr/local/bin/python*

hash -r
