def render(d1, d2):
    keys = list(d1.keys() | d2.keys())
    return {key: gen_tree(key, d1, d2) for key in sorted(keys)}


def gen_diff(d1, d2):
    keys = list(d1.keys() | d2.keys())
    return {key: gen_tree(key, d1, d2) for key in sorted(keys)}


def gen_tree(key, d1, d2):
    value1 = d1.get(key)
    value2 = d2.get(key)
    if key in d2 and key not in d1:
        tree = {
            'type': "ADDED",
            'value': value2,
        }
    elif key in d1 and key not in d2:
        tree = {
            'type': "REMOVED",
            'value': value1,
        }
    elif isinstance(value1, dict) and isinstance(value2, dict):
        tree = {
            'type': "CHILD",
            'value': gen_diff(value1, value2),
        }
    elif value1 == value2:
        tree = {
            'type': "UNCHANGED",
            'value': value1,
        }
    elif value1 != value2:
        tree = {
            'type': "CHANGED",
            'd1_value': value1,
            'd2_value': value2,
        }
    return tree
