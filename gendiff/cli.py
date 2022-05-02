#!usr/bin/env python3
import argparse
import yaml
import json


def text_format(path):
    format = path.split('.')[-1]
    if format == 'json':
        dictionary = json.load(open(path))
    elif format == 'yaml' or 'yml':
        dictionary = yaml.safe_load(open(path))
    return dictionary


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
    return text_format(args.first_file), text_format(args.second_file), formatter
