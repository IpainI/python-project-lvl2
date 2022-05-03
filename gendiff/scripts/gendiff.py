import pprint

from gendiff.formatters.json_generation import generate_new_tree
from gendiff.formatters.plain_generation import generate_plain
from gendiff.engine import gen_files_diff
from gendiff.cli import pars_args
from gendiff.formatters.yaml_generation import generate_yaml_tree


def main():
    file1, file2, out_format = pars_args()
    print(gen_files_diff(file1, file2, out_format))
    # yaml_tree = generate_yaml_tree(tree)
    # print(yaml_tree)


if __name__ == '__main__':
    main()
