"""Some description."""
import argparse

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.'
    )
parser.add_argument('first_file',nargs='?')
parser.add_argument('second_file',nargs='?')
parser.add_argument('-f', '--format', 
    help='set format of output')
parser.parse_args()


def main():
    """Some desription."""


if __name__ == '__main__':
    main()
