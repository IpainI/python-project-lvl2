from gendiff.formatters import plain, pretty, json


def choose(out_format):
    formatters = {
        'plain': plain,
        'pretty': pretty,
        'json': json,
        'stylish': pretty,
    }
    if not out_format:
        return pretty
    return formatters[out_format]
