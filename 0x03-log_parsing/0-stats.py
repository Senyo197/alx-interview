#!/usr/bin/python3
"""Script to process logs and compute metrics."""

import sys

# Initialize cache to count occurrences of each status code
cache = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0,
         '500': 0}
total_size = 0
counter = 0


def print_metrics():
    """Function to print the metrics."""
    print('File size: {}'.format(total_size))
    for key in sorted(cache.keys()):
        if cache[key] != 0:
            print('{}: {}'.format(key, cache[key]))


try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 2:
                continue

            # Parse status code and file size
            code = parts[-2]
            size = parts[-1]

            # Validate and process status code and file size
            if code in cache:
                cache[code] += 1
            total_size += int(size)
            counter += 1

            # Print metrics every 10 lines
            if counter == 10:
                print_metrics()
                counter = 0

        except (IndexError, ValueError):
            # Skip lines that don't have the expected format
            continue

except KeyboardInterrupt:
    # Print metrics upon keyboard interruption
    print_metrics()
    raise

finally:
    # Print final metrics at the end of input
    print_metrics()
