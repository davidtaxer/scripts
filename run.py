#! /usr/bin/env python3

import os
import requests

#get current working directory
cwd = os.getcwd()

#path to .txt files for this script
path ="/data/feedback/"

# create a list of items in path
items = os.listdir(path)

# uncomment print line to check if items variable
# creats a list of files in path correctly

#print(items)

#itterate through files in the directory and store as a dictionary


for file in items:
        with open (path + file) as info:
                data = info.read().split('\n')
                file_dict = {'title':data[0], 'name':data[1], 'date':data[2], "feedback":data[3]}
                response = requests.post("http://35.202.95.65/feedback/", json=file_dict)
                print(response.status_code)


#print(list_of_files)
