import pprint


from gendiff import generate_diff
from gendiff.cli import pars_args


def main():
    file1, file2, out_format = pars_args()
    tree = generate_diff(file1, file2, out_format)
    if out_format == 'json':
        pprint.pprint(tree)
    else:
        print(tree)


if __name__ == '__main__':
    main()
