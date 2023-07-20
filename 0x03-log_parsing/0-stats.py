#!/usr/bin/env python3

import sys

def print_statistics(total_size, status_codes):
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        print(f"{code}: {count}")

def process_lines():
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            line = line.strip()

            # Parse the line using the specified format
            parts = line.split()

            if len(parts) != 9 or parts[4] != '"GET' or not parts[5].startswith("/projects/"):
                continue

            status_code = parts[7]
            file_size = int(parts[8])
            #print(status_code)

            # Update total file size
            total_size += file_size
            #print(total_size)

            # Update status code count
            if status_code.isdigit():
                status_codes[status_code] = status_codes.get(status_code, 0) + 1

            # Print statistics after every 10 lines
            if i % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        pass

    # Print final statistics
    print_statistics(total_size, status_codes)

process_lines()
