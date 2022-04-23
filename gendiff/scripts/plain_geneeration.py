def check_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    return value


def generate_plain(tree, nest=''):
    if not isinstance(tree, dict):
        return str(tree)

    new_tree = []

    for key, value in tree.items():
        parents = check_parents(nest, key)
        item_type = value.get('type')

        if item_type == 'ADDED':
            message = "Property '{}' was added with value: '{}'".format(parents, check_value(value.get('value')))
        if item_type == 'REMOVED':
            message = "Property '{}' was removed".format(parents)
        if item_type == 'CHILD':
            message = generate_plain(value.get('value'), parents)
        if item_type == 'CHANGED':
            message = "Property '{}' was updated. From '{}' to '{}'".format(parents, check_value(value.get('d1_value')),
                                                                            check_value(value.get('d2_value')))
        elif item_type == 'UNCHANGED':
            continue

        new_tree.append(message)
    return '\n'.join(new_tree)


def check_parents(parent, value):
    if parent == '':
        return value
    return '{}.{}'.format(parent, value)






