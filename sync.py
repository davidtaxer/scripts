#!/usr/bin/env python

import subprocess, os
from multiprocessing import Pool
import re

src = "/media/david/SSD-FILES"


def run():
    dest = re.sub("(/media/david/USB DISK2)", r"\1"+"_backup",src)
    print("Moving Data from {} to {}".format(src,dest))
    subprocess.call(["rsync", "-zavh", src, dest])


if __name__ == "__main__":
  dir_list = []
  for root, dirs, files in os.walk(src, topdown=False):
      for name in dirs:
          dir_list.append(os.path.join(root, name))
  p = Pool(len(dir_list))
  p.map(run, dir_list)
