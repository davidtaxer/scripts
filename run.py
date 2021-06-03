#! /usr/bin/env python3

import os
import requests

#get current working directory
cwd = os.getcwd()

#path to .txt files for this script
path = cwd + "/data/feedback/"

# create a list of items in path
#items = [f for f in os.listdir(path) if os.path.isfile( os.path.join(path, f) )]
items = os.listdir(path)

# (uncomment print line to check if items variable creats a list
#  of files in path correctly)

print(items)

#itterate through files in the directory
for file in items:
    with open (path + file) as info:
        data = info.read().split('\n')
        dict = {'title':data[0], 'name':data[1], 'date':data[2], 'feedback':data[3]}


print(dict)
