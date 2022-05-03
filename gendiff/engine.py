from gendiff.formatters import format
from gendiff.files import get_file_content


def gen_files_diff(file1, file2, format_='plain'):
    content1 = get_file_content(file1)
    content2 = get_file_content(file2)
    formatter = format.choose(format_)
    diff = gen_diff(content1, content2)
    return formatter.render(diff)


def gen_diff(content1, content2):
    keys = list(content1.keys() | content2.keys())
    return {key: gen_tree(key, content1, content2) for key in sorted(keys)}


def convert_value(elem_value):
    if elem_value is True:
        return 'true'
    if elem_value is False:
        return 'false'
    return elem_value


def gen_tree(key, d1, d2):
    value1 = d1.get(key)
    value2 = d2.get(key)
    if value1 is None:
        tree = {
            'type': "ADDED",
            'value': convert_value(value2),
        }
    elif value2 is None:
        tree = {
            'type': "REMOVED",
            'value': convert_value(value1),
        }
    elif isinstance(value1, dict) and isinstance(value2, dict):
        tree = {
            'type': "CHILD",
            'value': gen_diff(value1, value2),
        }
    elif value1 == value2:
        tree = {
            'type': "UNCHANGED",
            'value': convert_value(value1),
        }
    elif value1 != value2:
        tree = {
            'type': "CHANGED",
            'd1_value': convert_value(value1),
            'd2_value': convert_value(value2),
        }
    return tree
