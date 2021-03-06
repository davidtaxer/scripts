#!/usr/bin/env python3

import re
import operator
import csv

per_user = {}
error = {}

with open ("syslog.log") as file:
    for line in file.readlines():
        pattern = r": (ERROR|INFO) ([\w ']*)\[?\#?[\d]*?\]? \(([\w]*.?[\w]*?)\)"
        m = re.search(pattern, line)
        m_type = m.group(1)
        message = m.group(2)
        user = m.group(3)

        ErrCount = [0]
        InfoCount = [0]

        if m_type == "INFO":
            if user not in per_user:
                per_user[user] =  InfoCount
            per_user[user] = InfoCount + 1


        if m_type == "ERROR":
            if user not in per_user:
                per_user[user] = ErrCount
            per_user[user]  = ErrCount + 1
            if message not in error:
                error[message] = 0
            error[message] += 1


error = dict(sorted(  error.items(),
                            key=operator.itemgetter(1),
                            reverse=True))
per_user = dict(sorted(per_user.items()))

print("Error : Count")
print(error)
print("")
for user in per_user:
    print(user, per_user[user])
print(per_user[user], ErrCount, InfoCount )
print("")
print("Info count is: " + str(InfoCount))
