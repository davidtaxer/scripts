#!/usr/bin/env python3

import multiprocessing
import subprocess
import os
from multiprocessing import Pool
import re
import time
import shutil


def confirm():
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
if exit_condition == 1:
        print("Aborting!")
        exit(1)

start = time.perf_counter()

src = "/media/david/SSD-FILES"
dest = "/media/david/USB STICK"


#def main(directory):
print('')
print("Syncing Data from (source){} to (destination){}".format(src, dest))
print('')

if __name__ == "__main__":

    directories = []

    for root, dirs, files in os.walk(src):
        for directory in dirs:
            print(directory)
            directories.append(directory)

        break
    len_d = len(directories)
    print('')
    print('Backing up '+ str(len_d) + ' directories')
    print('')

    pool = Pool(multiprocessing.cpu_count())
    pool.apply(subprocess.call, args=(["rsync", "-arq", src, dest, "--delete"],))

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
