import argparse
import subprocess
import psutil
import os


def add_parser_arguments(parser, arguments):
    """ Adds lots of command line arguments """
    for argument in arguments:
        parser.add_argument('-' + argument)


def main():
    parser = argparse.ArgumentParser(description='Mirror of the arguments for the python command line')
    add_parser_arguments(parser, 'bBdEiIOqsSuvVWx?')
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()

# python [-bBdEhiIOqsSuvVWx?] [-c command | -m module-name | script | - ] [args]