from gendiff.formatters import plain, pretty, json


def choose(stylish):
    formatters = {
        'plain': plain,
        'pretty': pretty,
        'json': json,
    }
    try:
        if not stylish:
            return pretty
        return formatters[stylish]
    except KeyError:
        raise ValueError(f'Format {stylish} does not exist')
