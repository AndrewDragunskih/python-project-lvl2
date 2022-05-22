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
    print('Difference between file1.json and file2.json:')
    print(generate_diff('file1.json', 'file2.json'))
    print('Difference between file1.yaml and file2.yml:')
    print(generate_diff('file1.yaml', 'file2.yml'))


if __name__ == '__main__':
    main()
