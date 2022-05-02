import pprint

from gendiff.formatters.json_generation import generate_new_tree
from gendiff.formatters.plain_generation import generate_plain
from gendiff.engine import gen_diff
from gendiff.cli import pars_args
from gendiff.formatters.yaml_generation import generate_yaml_tree


def main():
    file1, file2, out_format = pars_args()
    tree = gen_diff(file1, file2)
    if not out_format:
        pprint.pprint(tree)
    elif out_format == 'plain':
        plain_tree = generate_plain(tree)
        print(plain_tree)
    elif out_format == 'json':
        new_tree = generate_new_tree(tree)
        print(new_tree)
    yaml_tree = generate_yaml_tree(tree)
    print(yaml_tree)


if __name__ == '__main__':
    main()
