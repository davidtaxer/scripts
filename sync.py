#!/usr/bin/env python3

import time
import concurrent.futures

import subprocess, os
from multiprocessing import Pool
import re

start = time.perf_counter()
src = "/media/david/SSD-FILES/checks"
dest = "/media/david/SSD-FILES/BACKUP-TEST"

def run():
    print("Moving Data from {} to {}".format(src,dest))
    subprocess.call(["rsync", "-zavh", src, dest])

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
