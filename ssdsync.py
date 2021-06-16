#!/usr/bin/env python3

import multiprocessing
import subprocess
import os
from multiprocessing import Pool
import re
import time
import shutil


def confirm():
    """asks for confirmation if the user wants to run the program"""
    gogo = input("Continue? y/n\n")
    global exit_condition
    if gogo == 'y':
        exit_condition = 0
        return exit_condition
    elif gogo == "n":
        exit_condition = 1
        return exit_condition
    else:
        print("Please answer with y or n.")
        confirm()

confirm()
# exit with the message "Aborting" printed to the screen.
if exit_condition == 1:
        print("Aborting!")
        exit(1)

# start the time couner for backup time calculation
start = time.perf_counter()

# source and destination
src = "/media/david/SSD-FILES"
dest = "/media/david/USB STICK1"

# message for user stating syncing fron sourece to destination
print('')
print("Syncing Data from (source){} to (destination){}".format(src, dest))
print('')

if __name__ == "__main__":
    # create list of directories
    directories = []
    # traverse the directories
    for root, dirs, files in os.walk(src):
        for directory in dirs:
            print(directory)
            directories.append(directory)

        break
    len_d = len(directories)
    # message for user of how many directories are being backed up
    print('')
    print('Backing up '+ str(len_d) + ' directories')
    print('')

    pool = Pool(multiprocessing.cpu_count())
    pool.apply(subprocess.call, args=(["rsync", "-arq", src, dest, "--delete"],))

# finish time counter for backup time message
finish = time.perf_counter()

# message for user telling how long the backup took
print(f'Finished in {round(finish-start, 2)} second(s)')
