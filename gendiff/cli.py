from gendiff.formatters import formatters

import argparse
import json
import yaml


def pars(content):
    extension = content.split('.')[-1]
    with open(content, 'r') as path:
        if extension == 'json':
            return json.loads(path)
        elif extension == 'yml':
            return yaml.safe_load(path)


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
    formatter = formatters.choose(out_format)
    result = formatter.render(pars(file1), pars(file2))
    print(result)
  
  
