#!/usr/bin/env python3

import multiprocessing
import subprocess
import os
from multiprocessing import Pool
import re
import time
import shutil

start = time.perf_counter()

def confirm():
    gogo = input("Continue? yes/no\n")
    global exit_condition
    if gogo == 'yes':
        exit_condition = 0
        return exit_condition
    elif gogo == "no":
        exit_condition = 1
        return exit_condition
    else:
        print("Please answer with yes or no.")
        confirm()

confirm()
if exit_condition == 1:
        print("Aborting!")
        exit(1)

src = "/media/david/SSD-FILES"
dest = "/media/david/BACKUP-TEST"


#def main(directory):
print("Syncing Data from (source){} to (destination){}".format(src, dest))
print('')

if __name__ == "__main__":

    directories = []

    for root, dirs, files in os.walk(src):
        for d in dirs:
            print(d)
            directories.append(d)

        break
    len_d = len(directories)
    print('')
    print('Backed up '+ str(len_d) + ' directories')
    print('')

    pool = Pool(multiprocessing.cpu_count())
    pool.apply(subprocess.call, args=(["rsync", "-arq", src, dest],))

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
