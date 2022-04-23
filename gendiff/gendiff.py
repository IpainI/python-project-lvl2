import pprint

from gendiff.scripts.json_generation import generate_new_tree
from gendiff.scripts.plain_geneeration import generate_plain
from gendiff.engine import generate_ast


def main():
    tree, out_format = generate_ast()
    if not out_format:
        pprint.pprint(tree)
    elif out_format == 'plain':
        plain_tree = generate_plain(tree)
        print(plain_tree)
    elif out_format == 'json':
        new_tree = generate_new_tree(tree)
        print(new_tree)


if __name__ == '__main__':
    main()
