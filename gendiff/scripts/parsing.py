#!usr/bin/env python3
import argparse
import yaml
import json


def text_format(path1, path2):
    return path1.split('.')[-1], path2.split('.')[-1]


def pars_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='This is the first file')
    parser.add_argument('second_file', type=str, help='This is the second file')
    parser.add_argument('-f', '--format', type=format, help='set format of output')
    args = parser.parse_args()
    out_format = args.format
    format1, format2 = text_format(args.first_file, args.second_file)
    if format1 and format2 == 'json':
        dictionary1 = json.load(open(args.first_file))
        dictionary2 = json.load(open(args.second_file))
    elif format1 and format2 == 'yaml' or 'yml':
        dictionary1 = yaml.safe_load(open(args.first_file))
        dictionary2 = yaml.safe_load(open(args.second_file))
    return dictionary1, dictionary2, out_format

