#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
"""

from sys import stdin


def main():
    """
    Print the statistcs
    """

    size = 0
    count = 0
    status_code = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }

    try:

        for line in stdin:

            args = line.split()
            if len(args) > 2:

                if args[-2] in status_code:
                    status_code[args[-2]] += 1

                size += int(args[-1])

            count += 1

            if not count % 10:
                print('File size: {}'.format(size))

                for key, value in sorted(status_code.items()):
                    if value:
                        print('{}: {}'.format(key, value))
    except KeyboardInterrupt:
        pass
    finally:
        print('File size: {}'.format(size))

        for key, value in sorted(status_code.items()):
            if value:
                print('{}: {}'.format(key, value))


if __name__ == '__main__':
    main()
