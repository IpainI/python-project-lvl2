
SPACES = '    '


def get_new_tree(d):
    meta = {}
    for key, value in d.items():
        item_type = value.get('type')
        item_value = value.get('value')

        if item_type == 'CHILD':
            new_value = get_new_tree(item_value)
            meta['  ' + key] = new_value

        elif item_type == 'ADDED':
            meta['+ ' + key] = item_value

        elif item_type == 'REMOVED':
            meta['- ' + key] = item_value

        elif item_type == 'CHANGED':
            value1 = value.get('d1_value')
            value2 = value.get('d2_value')
            meta['+ ' + key] = value1
            meta['- ' + key] = value2

        elif item_type == 'UNCHANGED':
            meta['  ' + key] = item_value
    return meta


def printing_tree(d, c):
    for key, value in d.items():
        if isinstance(value, dict):
            print(SPACES * c, '{}: '.format(key))
            printing_tree(value, c + 1)
        else:
            print(SPACES * c, '{}: {}'.format(key, value))


def print_json(new_tree):
    for key, value in new_tree.items():
        if isinstance(value, dict):
            print(f'{key}: ')
            printing_tree(new_tree.get(key), 1)
        else:
            print(SPACES, '{}: {}'.format(key, value))

