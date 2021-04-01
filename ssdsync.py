#!/usr/bin/env python3

import multiprocessing
import subprocess, os
from multiprocessing import Pool
import re
import time

start = time.perf_counter()

src = "/media/david/SSD-FILES"
dest = "/media/david/BACKUP-TEST"


def main():
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
