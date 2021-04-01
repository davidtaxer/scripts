#!/usr/bin/env python3

import subprocess, os
from multiprocessing import Pool
import re

src = "/media/david/SSD-FILES/scripts/checks"


def run(directory):
    src = directory
    dest = "/media/david/BACKUP-TEST"
    print("Moving Data from {} to {}".format(src,dest))
    subprocess.call(["rsync", "-arq", src, dest])


if __name__ == "__main__":
  dir_list = []
  for root, dirs, files in os.walk(src, topdown=False):
      for name in dirs:
          dir_list.append(os.path.join(root, name))
  p = Pool(len(dir_list))
  p.map(run, dir_list)
