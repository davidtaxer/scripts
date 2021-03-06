#!/usr/bin/env python3

def character_frequency(filename):
    """Counts the frequency of each character in the given file"""
    # first try to open the filename
    try:
        f = open(filename)
    except OSError:
        return None

    # now process the file
    character = {}
        for char in line:
            for line in f:
                characters[char] = characters.get(char, 0) + 1
        f.close()
        return characters
