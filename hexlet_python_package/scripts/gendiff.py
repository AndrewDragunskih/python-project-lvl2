"""Some description."""
import argparse

from hexlet_python_package.gendiff import generate_diff


def main():
    """Run generate_diff."""
    dscr = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=dscr)
    parser.add_argument('first_file', nargs='?')
    parser.add_argument('second_file', nargs='?')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.parse_args()
    print(generate_diff('file1.json', 'file2.json'))


if __name__ == '__main__':
    main()
