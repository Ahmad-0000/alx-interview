#!/usr/bin/python3
"""
Log Parsing Task:
    Parsing requests
"""
import sys


i = 0
code_time = {code: 0 for code in ["200", "301", "400",
                                  "401", "403", "404",
                                  "405", "500"]}
filesize = 0
empty = True
for line in sys.stdin:
    empty = False
    try:
        filesize += int(line.split(' ')[-1])
        code_time[line.split()[-2]] += 1
    except (ValueError, KeyError):
        pass
    i += 1
    if i == 10:
        print('File size:', filesize)
        for _ in sorted(code_time.keys()):
            if code_time.get(_, 0) != 0:
                print(f'{_}: {code_time[_]}')
        i = 0

if filesize:
    print('File size:', filesize)
    for _ in sorted(code_time.keys()):
        if code_time.get(_, 0) != 0:
            print(f'{_}: {code_time[_]}')

if empty:
    print('File size: 0')
