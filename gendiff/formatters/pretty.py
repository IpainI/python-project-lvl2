from gendiff.formatters.json import gen_diff

SPACES = '  '


def render(file1, file2):
    result = gen_diff(file1, file2)
    return generate_pretty(result)


def generate_pretty(tree, count=1):
    new_tree = []
    spaces = SPACES * count
    for key, value in tree.items():
        item_type = value.get('type')
        item_value = value.get('value')
        if item_type == 'CHILD':
            new_tree.extend([
                '{}  {}: {{'.format(spaces, key),
                generate_pretty(item_value, count + 2),
                '{}}}'.format(spaces + SPACES)
            ])
        elif item_type == 'CHANGED':
            new_tree.extend([
                '{}+ {}: {}'.format(spaces, key,
                                    get_value(value.get('d2_value'), count)),
                '{}- {}: {}'.format(spaces, key,
                                    get_value(value.get('d1_value'), count))
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
    if count == 1:
        new_tree = ['{'] + new_tree + ['}']
    return '\n'.join(new_tree)

#
# def gen_sub_tree(tree, count):
#     res = list()
#     res.append('|')
#     for key, value in tree.items():
#         indent = SPACES * (count + 3)
#         formatted_value = get_value(value, count + 1)
#         res.append('{}{}| {}'.format(indent, key, formatted_value))
#     return '\n'.join(res)


# def check_simple(value, count):
#     if isinstance(value, dict):
#         return gen_sub_tree(value, count+1)
#     return value


def get_value(value, count):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    if isinstance(value, dict):
        intend = count + 2
        res = '{\n'
        for k, v in value.items():
            res += '{}  {}: {}\n'.format(SPACES * intend, k, get_value(v, intend))
        res += SPACES * count + '  }'
        return res
    return value
