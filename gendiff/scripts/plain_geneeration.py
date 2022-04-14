def check_value(something):
    if isinstance(something, dict):
        return 'complex value'
    return something


def get_keys_list(tree, helper=''):
    plain = []
    keys = list(tree.keys())
    for key in sorted(keys):
        plain.append(get_plain_tree(tree[key], key + helper))
    return plain


def try_again_get_plain(tree, helper=''):
    if not isinstance(tree, dict):
        return str(tree)

    plain = []
    for key, value in tree.items():
        item_type = key.get('type')

        if item_type == 'CHILD':
            string = try_again_get_plain(value.get('value'), key)
            return plain.append(string)


def get_plain_tree(tree, helper):
    plain = []
    for key in tree.keys():
        item_type = tree.get('type')
        item_value = tree.get('value')
        if item_type == 'CHILD':
            helper = helper + '.' + key
            plain.append(get_keys_list(item_value, helper))
            return plain
        elif item_type == 'ADDED':

            plain.append('Property {} was added with value: {}'.format(helper, check_value(item_value)))
            return plain
        elif item_type == 'REMOVED':

            plain.append('Property {} was removed'.format(helper))
            return plain
        elif item_type == 'CHANGED':

            value1 = tree.get('d1_value')
            value2 = tree.get('d2_value')
            plain.append('Property {} was updated from: {} to: {}'.format(helper,
                                                                          check_value(value1), check_value(value2)))
            return plain