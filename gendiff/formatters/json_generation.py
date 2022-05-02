SPACES = '   '


def generate_new_tree(tree, count=0):
    new_tree = []
    spaces = SPACES * count
    for key, value in tree.items():
        item_type = value.get('type')
        item_value = value.get('value')
        if item_type == 'CHILD':
            new_tree.extend([
                '{}  {}: {{'.format(spaces, key),
                generate_new_tree(item_value, count + 2),
                '{}}}'.format(spaces + SPACES)
            ])
        elif item_type == 'CHANGED':
            new_tree.extend([
                '{}+ {}: {}'.format(spaces, key,
                                    get_value(value.get('d1_value'))),
                '{}- {}: {}'.format(spaces, key,
                                    get_value(value.get('d2_value')))
            ])
        if item_type == 'REMOVED':
            new_tree.append('{}- {}: {}'.format(spaces, key,
                                                get_value(item_value, count)))
        if item_type == 'ADDED':
            new_tree.append('{}+ {}: {}'.format(spaces, key,
                                                get_value(item_value, count)))
        if item_type == 'UNCHANGED':
            new_tree.append('{}  {}: {}'.format(spaces, key,
                                                get_value(item_value, count)))
    if count == 0:
        new_tree = ['{'] + new_tree + ['}']
    return '\n'.join(new_tree)


def gen_sub_tree(tree, count):
    res = list()
    res.append('{')
    for key, value in tree.items():
        res.extend([
            '{}{}: {}'.format(SPACES * (count + 3), key, value),
            '{}}}'.format(SPACES * (count + 1)),
        ])
    return '\n'.join(res)


def get_value(value, count=1):
    if isinstance(value, dict):
        return gen_sub_tree(value, count)
    return value
