from gendiff.formatters import formatters

import argparse
import json
import yaml


def pars(path):
    extension = path.split('.')[-1]
    with open(file_path, mode='r', encoding='utf8') as content:
        if extension == 'json':
            return json.loads(content.read())
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
    formatter = formatters.choose(out_format)
    result = formatter.render(pars(file1), pars(file2))
    print(result)
  
  
