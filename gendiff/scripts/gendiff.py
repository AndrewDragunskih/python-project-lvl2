"""Some description."""
import argparse

from gendiff.formater.json import json_output
from gendiff.formater.plain import plain
from gendiff.formater.stylish import stylish
from gendiff.gendiff import generate_diff


def main():
    """Run generate_diff."""
    dscr = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=dscr)
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output',
        default='stylish',
    )
    parser.add_argument('first_file', nargs='?')
    parser.add_argument('second_file', nargs='?')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    if args.format == 'stylish':
        print(stylish(diff))
    elif args.format == 'plain':
        print(plain(diff))
    elif args.format == 'json':
        json_output(diff, args.first_file, args.second_file)
    else:
        print(diff)


if __name__ == '__main__':
    main()
