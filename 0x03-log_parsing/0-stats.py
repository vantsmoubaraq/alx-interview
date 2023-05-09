#!/usr/bin/python3

"""reads stdin line by line and computes metrics"""

import sys
import re

readin = sys.stdin

current_dict = {}
for num in [200, 301, 400, 401, 403, 404, 405, 500]:
    current_dict[str(num)] = 0


file_size = 0
count = 0
try:
    while readin:
        line = sys.stdin.readline()

        string = r'\[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
        pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - ' + string

        match = re.match(pattern, line)
        if not match:
            continue

        status_code = str(match.group(3))

        if status_code in current_dict:
            count += 1
            current_dict[status_code] += 1
            file_size += int(match.group(4))

        if count == 10:
            print(f"File size: {file_size}")
            for key, value in sorted(current_dict.items(), key=lambda x: x):
                print(f"{key}: {value}")
            count = 0
except KeyboardInterrupt as e:
    print(f"File size: {file_size}")
    for key, value in sorted(current_dict.items(), key=lambda x: x):
        print(f"{key}: {value}")
    print(e)
