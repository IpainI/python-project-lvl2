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
  

def gendiff(file_path_1, file_path_2, out_format='pretty')
    formatter = formatters.choose(output_format)
    return formatter.render(parese(file_path_1), parese(file_path_2))
  
