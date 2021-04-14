#!/usr/bin/env python3

import csv
import datetime
import requests

FILE_URL="http://marga.com.ar/employees-with-date.csv"

def get_file_content(url):
    """Download the file from url and
    convert columns into sorted dictionary."""

    dates_dict = {}

    with requests.get(url, stream=True) as dict:
        lines = (line.decode('utf-8') for line in dict.iter_lines())
        reader = csv.reader(lines)
        next(reader)
        for row in reader:
            dates_dict[row[3]] = [row[0] + " " + row[1]]
            print(dict(sorted(dates_dict.items())))

    return dict(sorted(dates_dict.items()))




get_file_content(FILE_URL)
