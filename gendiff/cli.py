#!usr/bin/env python3
import argparse

import json

import yaml


def parse(content, extension):
    if extension == 'json':
        return json.loads(content)
    elif content in ('yaml', 'yml'):
        return yaml.safe_load(content)
    raise ValueError(f'Files with extension {extension} are not supported')


def pars_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str,
                        help='This is the first file')
    parser.add_argument('second_file', type=str,
                        help='This is the second file')
    parser.add_argument('-f', '--format', type=format,
                        help='set format of output')
    args = parser.parse_args()
    formatter = args.format
    return args.first_file, args.second_file, formatter
