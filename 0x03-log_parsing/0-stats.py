#!/usr/bin/python3

"""reads stdin line by line and computes metrics"""

import sys



def main():
    """reads stdin line by line and computes metrics"""
    current_dict = {}
    for num in [200, 301, 400, 401, 403, 404, 405, 500]:
        current_dict[str(num)] = 0

    file_size = 0
    count = 0
    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                break

            st = r'\[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
            pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - ' + st

            
    except KeyboardInterrupt as e:
        print(f"File size: {file_size}")
        for key, value in sorted(current_dict.items(), key=lambda x: x):
            print(f"{key}: {value}")
        print(e)


if __name__ == "__main__":
    main()
