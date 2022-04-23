from gendiff.scripts.parsing import pars_args


def gen_sub_tree(d1, d2):
    keys = list(d1.keys() | d2.keys())
    return {key: gen_tree(key, d1, d2) for key in sorted(keys)}


def get_value_type(elem_value):
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
            'value': get_value_type(value2),
        }
    elif value2 is None:
        tree = {
            'type': "REMOVED",
            'value': get_value_type(value1),
        }
    elif isinstance(value1, dict) and isinstance(value2, dict):
        tree = {
            'type': "CHILD",
            'value': gen_sub_tree(value1, value2),
        }
    elif value1 == value2:
        tree = {
            'type': "UNCHANGED",
            'value': get_value_type(value1),
        }
    elif value1 != value2:
        tree = {
            'type': "CHANGED",
            'd1_value': get_value_type(value1),
            'd2_value': get_value_type(value2),
        }
    return tree


def generate_ast():
    file_1, file_2, out_format = pars_args()
    tree = gen_sub_tree(file_1, file_2)
    return tree, out_format
