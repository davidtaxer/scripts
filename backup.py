#!/usr/bin/env python3

import os
import shutil
import time

from sh import rsync

# Functions

def check_dir_exist(os_dir):
    if not os.path.exists(os_dir):
        print(os_dir, "does not exist.")
        exit(1)

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


# Specify what and where to backup.
backup_path = input("What should be backed up today?\n")
#backup_path = "/media/david/SSD-FILES/scripts/checks"
check_dir_exist(backup_path)
print("Okay", backup_path, "will be saved.")
time.sleep(3)

backup_to_path = input("Where to backup?\n")
#backup_to_path = "/media/david/BACKUP-TEST"
check_dir_exist(backup_to_path)
print("Okay", backup_to_path, "exists.")



# Do the actual backup
print("Doing the backup now!")
confirm()
if exit_condition == 1:
        print("Aborting!")
        exit(1)

rsync("-auhv", "--delete", "--exclude=lost+found", "--exclude=/sys", "--exclude=/tmp", "--exclude=/proc",
  "--exclude=/mnt", "--exclude=/dev", "--exclude=/backup", backup_path, backup_to_path)
