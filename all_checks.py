#!/usr/bin/env python3
import os
import sys

def check_reboot():
    """Returns True if the computer has a pending reboot"""
    return os.path.exist("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending reboot.")
        sys.exit(1)

main()
