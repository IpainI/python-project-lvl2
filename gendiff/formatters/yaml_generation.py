SPACES = "    "


def gen_yaml_tree(tree, count=0):
    new_tree = []

    for key, value in tree.items():
        item_value = value.get('value')
        item_type = value.get('type')
        if item_type == 'ADDED':
            new_tree.append('{}+ {}: \n{} {}'.format(SPACES * count, key,
                                                     SPACES * (count+2),
                                                     check_value(item_value, count)))
        if item_type == 'REMOVED':
            new_tree.append('{}- {}: \n{} {}'.format(SPACES * count, key,
                                                     SPACES * (count+2),
                                                     check_value(item_value, count)))
        if item_type == 'CHANGED':
            new_tree.append('{}+ {}: \n{} {}'.format(SPACES * count, key,
                                                     SPACES * (count+2),
                                                     check_value(value.get('d1_value'), count)))
            new_tree.append('{}- {}: \n{} {}'.format(SPACES * count, key,
                                                     SPACES * (count+2),
                                                     check_value(value.get('d2_value'), count)))
        elif item_type == 'CHILD':

            new_tree.extend(['{}  {}: \n{} {}'.format(SPACES * count, key, SPACES * count,
                            gen_yaml_tree(item_value), count+1)])
        if item_type == 'UNCHANGED':
            new_tree.append('{}  {}: \n{}  {}'.format(SPACES * count, key,
                                                      SPACES * (count+2),
                                                      check_value(item_value, count)))
    return '\n'.join(new_tree)


def check_value(value, count):
    if isinstance(value, dict):
        new_tree = []
        for key, value in value.items():
            new_tree.append('{}{}: \n {} {}'.format(SPACES * count, key,
                                                    SPACES * (count+1),
                                                    check_value(value, count+1)))
        return '\n'.join(new_tree)
    return value


# new type of output


def generate_yaml_tree(tree, count=1):
    new_tree = []
    spaces = SPACES * count
    for key, value in tree.items():
        item_type = value.get('type')
        item_value = value.get('value')
        if item_type == 'CHILD':
            new_tree.extend([
                '{}  {}: '.format(spaces, key),
                generate_yaml_tree(item_value, count + 2),
                '{}'.format(spaces + SPACES)
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

    return '\n'.join(new_tree)


def gen_sub_tree(tree, count):
    res = list()
    for key, value in tree.items():
        res.extend([
            '{}{}: {}'.format(SPACES * (count + 3), key, value),
            '{}'.format(SPACES * (count + 1)),
        ])
    return '\n'.join(res)


def get_value(value, count=1):
    if isinstance(value, dict):
        return gen_sub_tree(value, count)
    return value
