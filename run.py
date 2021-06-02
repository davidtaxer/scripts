#! /usr/bin/env python3

import os
import requests

#get current working directory
cwd = os.getcwd()

#path to .txt files for this script
path = cwd + "/data/feedback"

#create a list of items in path
items = [f for f in os.listdir(path) if os.path.isfile( os.path.join(path, f) )]

#itterate through files in the directory
#for files in os.listdir(path):
print(items)
