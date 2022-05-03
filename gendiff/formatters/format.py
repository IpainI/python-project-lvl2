from gendiff.formatters import plain, pretty


def choose(formatter):
    formatters = {
        'plain': plain,
        'pretty': pretty,
    }
    try:
        return formatters[formatter]
    except KeyError:
        raise ValueError(f'Format {formatter} does not exist')
