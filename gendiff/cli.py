from gendiff.formatters import formatters

import argparse
import json
import yaml


def parse(content):
    extension = content.split('.')[-1]
    if extension == 'json':
        return json.loads(content)
    elif extension == 'yml':
        return yaml.safe_load(content)


def pars_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str,
                        help='This is the first file')
    parser.add_argument('second_file', type=str,
                        help='This is the second file')
    parser.add_argument('-f', '--format', type=str,
                        help='set format of output')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
  

def main():
    file1, file2, out_format = pars_args()
    if not out_format:
        out_format = 'pretty'
    formatter = formatters.choose(out_format)
    return formatter.render(parse(file1), parse(file2))
  
  
