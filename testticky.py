#!/usr/bin/env python3

import re
import operator
import csv

type_map = {'ERROR': 1, 'INFO': 0}
per_user = {}
error = {}

with open ("syslog.log") as file:
    for line in file.readlines():
        pattern = r": (ERROR|INFO) ([\w ']*)\[?\#?[\d]*?\]? \(([\w]*.?[\w]*?)\)"
        m = re.search(pattern, line)
        m_type = m.group(1)
        message = m.group(2)
        user = m.group(3)

        if user not in per_user:
                per_user[user] =  [0,0]
        per_user[user][type_map[m_type]] += 1

        if m_type == "ERROR":
            if message not in error:
                error[message] = 0
            error[message] += 1



error = dict(sorted(  error.items(),
                            key=operator.itemgetter(1),
                            reverse=True))
per_user = dict(sorted(per_user.items()))

with open ('error_message.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["Error", "Count"])
        for key, value in error.items():
            writer.writerow([key, value])

with open ('user_statistics.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["Username", "INFO", "ERROR"])
    for key, value in per_user.items():
        writer.writerow([key, per_user[user][type_map['INFO']], per_user[user][type_map['ERROR']]])
