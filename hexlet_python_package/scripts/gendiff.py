"""Some description."""
import argparse
from hexlet_python_package.gendiff import generate_diff

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
    print('File1 path (absolute):\n    /home/andrew/python-project-lvl2/file1.json')
    print('File2 path (absolute):\n    /home/andrew/python-project-lvl2/file2.json')
    print(generate_diff('/home/andrew/python-project-lvl2/file1.json', '/home/andrew/python-project-lvl2/file2.json'))
    print('\nFile1 path:\n    file1.json')
    print('File2 path:\n    file2.json')
    print(generate_diff('file1.json', 'file2.json'))

if __name__ == '__main__':
    main()
