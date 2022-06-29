"""Some description."""
import argparse

from gendiff.gendiff import generate_diff
from gendiff.open_files import open_file


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
    first_file = open_file(args.first_file)
    second_file = open_file(args.second_file)
    print(generate_diff(first_file, second_file, args.format))


if __name__ == '__main__':
    main()
