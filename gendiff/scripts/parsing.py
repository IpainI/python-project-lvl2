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
    format1, format2 = text_format(args.first_file, args.second_file)
    if format1 and format2 == 'json':
        dictionary1 = json.load(open(args.first_file))
        dictionary2 = json.load(open(args.second_file))
        print(format1, format2)
    elif format1 and format2 == 'yaml' or 'yml':
        dictionary1 = yaml.safe_load(open(args.first_file))
        dictionary2 = yaml.safe_load(open(args.second_file))
    return dictionary1, dictionary2


def main():
    d1, d2 = pars_args()
    tree = gen_sub_tree(d1, d2)
#    pprint.pprint(tree)
#    print(json.dumps(tree, indent=2))
    new_tree = get_new_tree(tree)
 #   for keys in new_tree.keys():
  #      print(f'{keys}: ')
  #      printing_tree(new_tree.get(keys), 1)
    plain = get_keys_list(tree)
    for i in range(len(plain)):
        print(plain[i])


if __name__ == '__main__':
    main()
