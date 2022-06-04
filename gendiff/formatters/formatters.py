from gendiff.formatters import plain, pretty, json


def choose(out_format):
    formatters = {
        'plain': plain,
        'pretty': pretty,
        'json': json,
    }
    try:
        if not out_format:
            return pretty
        return formatters[out_format]
    except KeyError:
        raise ValueError(f'Format {out_format} does not exist')
